from api._databaseConnection import database
from api._getAuthToken import makeAuthToken, verifyAuthToken
from api._passwordHashes import verifyPassword

import flask

print(__file__ + " has nothing to do with the database and must be updated")

def call(args):
    if "username" not in args["args"]:
        return flask.Response("no username", 400)

    if "password" not in args["args"]:
        return flask.Response("no password", 400)

    userList = database.execute(f"select * from users where username='{args["args"]["username"].lower()}'").fetchall()

    response = None

    # will be empty if no such username exists
    if userList:
        if verifyPassword(args["args"]["password"], bytes(userList[0][2][2:-1], "utf-8")):
            response = flask.Response("success", 200)

            authTokenList = database.execute(f"select * from authTokens where userID={userList[0][0]}").fetchall()

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
