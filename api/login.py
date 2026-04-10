from api._databaseConnection import database
from api._getAuthToken import makeAuthToken, verifyAuthToken
from api._passwordHashes import verifyPassword

import flask

def call(args):
    if "username" not in args["args"]:
        return flask.Response("no username", 400)

    if "password" not in args["args"]:
        return flask.Response("no password", 400)

    # this returns a tuple, but we need it in a list for potential item assignment later
    userList = list(database.execute("select * from users where username=? ", (args["args"]["username"].lower(),)).fetchall())
    for i in range(len(userList)):
        userList[i] = list(userList[i])

    response = None

    # will be empty if no such username exists
    if userList:
        # at some point userList[0][2] changed from str to bytes
        # this is probably due to the formatting of the database request changing
        # however, to play it safe, check for it still being str, and fix if necessary before continuing
        if type(userList[0][2]) is not bytes:
            userList[0][2] = bytes(userList[0][2][2:-1], "utf-8")

        if verifyPassword(args["args"]["password"], userList[0][2]):
            response = flask.Response("success", 200)

            authTokenList = database.execute("select * from authTokens where userID=?", (userList[0][0],)).fetchall()

            authToken = ""

            if len(authTokenList):
                if verifyAuthToken(authTokenList[0][0]):
                    authToken = authTokenList[0][0]
                else:
                    authToken = makeAuthToken(userList[0][0])

            else:
                authToken = makeAuthToken(userList[0][0])

            response.set_cookie("authToken", authToken)
        else:
            response = flask.Response("invalid password", 400)

    else:
        response = flask.Response("no such user exists", 400)

    return response
