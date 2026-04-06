import flask

app = flask.Flask(__name__)

import api

def getFile(filePath: str, relative: bool=True) -> str:
    if relative:
        filePath = "./" + filePath

    try:
        with open(filePath, "r") as openedFile:
            returnString = ""
            for line in openedFile.readlines():
                returnString += line
                returnString += '\n'

            return returnString

    except (FileNotFoundError, OSError) as e:
        print("\n============================================================================\n")
        print(e)
        print("\n============================================================================\n")
        return ""


@app.route("/", defaults={"path":""})
@app.route("/<path:path>")
def servePage(path):
    if not path:
        return getFile("/pages/main.html")

    if path == "./favicon.ico":
        return flask.Response(status=404)

    if path.split("/")[0] == "api":
        splitPath = path.split("/")

        if len(splitPath) == 1:
            return flask.Response(status=404)

        if splitPath[1] in api.endpoints:
            apiResponse = api.endpoints[splitPath[1]]["module"].call(flask.request.args)

            return flask.Response(status=apiResponse)

        return flask.Response(status=404)

    mimeType = "text/html"

    if path.split(".")[-1] == "css":
        mimeType = "text/css"

    return flask.Response(getFile(path), mimetype=mimeType)
