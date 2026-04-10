import flask

app = flask.Flask(__name__)

import api
import api._databaseConnection
import json

def userIsLoggedIn():
    if "authToken" not in flask.request.cookies:
        return False

    authToken = flask.request.cookies["authToken"]

    userIdList = api._databaseConnection.database.execute(f"select userID from authTokens where authTokenString='{authToken}'").fetchall()

    if len(userIdList) == 0:
        return False

    return True

def userIsAdmin():
    if "authToken" not in flask.request.cookies:
        return False

    authToken = flask.request.cookies["authToken"]

    userIdList = api._databaseConnection.database.execute(f"select userID from authTokens where authTokenString='{authToken}'").fetchall()

    if len(userIdList) == 0:
        return False

    userId = userIdList[0][0]

    adminValueList = api._databaseConnection.database.execute(f"select admin from users where userID='{userId}'").fetchall()

    if len(adminValueList) == 0:
        # this *shouldnt* be reachable but have it to fail safely
        return False

    adminValue = adminValueList[0][0]

    if adminValue == 0:
        return False

    return True

# function for getting a file, this way any file that exists in the /pages/
def getFile(filePath: str) -> (str | None):
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

            return returnString

    except (FileNotFoundError, OSError) as e:
        print("\n============================================================================\n")
        print(e)
        print("\n============================================================================\n")
        return None

# this is the function flask calls whenever a request is made
# it will use the above function to go and find, then serve, any page that exists
@app.route("/", defaults={"path":""}) # type: ignore
@app.route("/<path:path>", methods=["GET", "POST"]) # type: ignore
def servePage(path):
    requestArgs = {
        "args":flask.request.args,
        "cookies":flask.request.cookies
    }

    if flask.request.method != "GET":
        requestArgs["args"] = json.loads(flask.request.data)

    # blank path means main page
    if not path:
        if not userIsLoggedIn():
            return flask.Response(getFile("./pages/login.html"), 401)
        else:
            return getFile("./pages/main.html")

    # If a non admin attempts to access the admin dashboard, deny access
    elif (len(path.split("/")) >= 2) and path.split("/")[1] == "admin" and not userIsAdmin():
        return flask.Response(getFile("./pages/__adminDenial.html"), 404)

    # If a non logged-in user attempts to access anything, redirect them to login
    elif (path == "pages/post.html" or path == "pages/main.html") and not userIsLoggedIn():
        return flask.Response(getFile("./pages/login.html"), 401)

    # dont currently have a favicon
    elif (path == "./favicon.ico") or (path == "favicon.ico"):
        return flask.Response("no favicon yet", status=404)

    # disallow access to root directory
    elif len(path.split("/")) == 1:
        return flask.Response("invalid path", 401)

    elif path.split("/")[-1].startswith("__"):
            return flask.Response("no such page", 404)

    # api calls are handled separately to pages
    elif path.split("/")[0] == "api":
        splitPath = path.split("/")

        # /api with no further details
        if len(splitPath) == 1:
            return flask.Response("please use an endpoint", status=404)

        # if a page starts with "admin" then only an administrator account can access it
        elif splitPath[1].startswith("admin"):
            if not userIsAdmin():
                return flask.Response("you must be an admin to do that", 403)

        # if the requested endpoint exists
        elif splitPath[1] in api.endpoints:
            # call said endpoint and get its return code
            apiResponse = api.endpoints[splitPath[1]]["module"].call(requestArgs) # yes this is hacky but it works

            return apiResponse

        return flask.Response(status=404)

    # default media type is html
    mimeType = "text/html"

    # change it if necessary
    if path.split(".")[-1] == "css":
        mimeType = "text/css"
    elif path.split(".")[-1] == "js":
        mimeType = "text/javascript"

    page = getFile(path)

    if page == None:
        return flask.Response("no such page", 404)

    return flask.Response(page, mimetype=mimeType)
