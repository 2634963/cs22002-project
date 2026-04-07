import flask

app = flask.Flask(__name__)

import api

# function for getting a file, this way any file that exists in the /pages/
def getFile(filePath: str) -> str:
    if filePath.startswith("/"):
        filePath = "." + filePath

    # put it in a try catch block so that if the file isnt found we can return an error message
    try:
        # open the file if it exists
        with open(filePath, "r") as openedFile:
            # read every line into one string
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

# this is the function flask calls whenever a request is made
# it will use the above function to go and find, then serve, any page that exists
@app.route("/", defaults={"path":""})
@app.route("/<path:path>")
def servePage(path):
    # blank path means main page
    if not path:
        return getFile("./pages/main.html")

    # dont currently have a favicon
    if (path == "./favicon.ico") or (path == "favicon.ico"):
        return flask.Response(status=404)

    # api calls are handled separately to pages
    if path.split("/")[0] == "api":
        splitPath = path.split("/")

        # /api with no further details
        if len(splitPath) == 1:
            return flask.Response(status=404)

        # if the requested endpoint exists
        if splitPath[1] in api.endpoints:
            # call said endpoint and get its return code
            apiResponse = api.endpoints[splitPath[1]]["module"].call(flask.request.args) # yes this is hacky but it works

            return flask.Response(status=apiResponse)

        return flask.Response(status=404)

    # default media type is html
    mimeType = "text/html"

    # change it if necessary
    if path.split(".")[-1] == "css":
        mimeType = "text/css"

    return flask.Response(getFile(path), mimetype=mimeType)
