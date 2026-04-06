import flask

app = flask.Flask(__name__)

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
        return getFile("pages/main.html")

    mimeType = "text/html"

    if path.split(".")[-1] == "css":
        mimeType = "text/css"

    return flask.Response(getFile(path), mimetype=mimeType)
