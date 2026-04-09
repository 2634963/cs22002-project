from api._databaseConnection import database
from api._getAuthToken import getAuthToken

import flask

print(__file__ + " has nothing to do with the database and must be updated")

def call(args):
    if "username" not in args["args"]:
        return flask.Response("no username", 400)

    if "password" not in args["args"]:
        return flask.Response("no password", 400)

    response = flask.Response("this is some data that is the body of the response please treat it very carefully", 501)

    response.set_cookie("authToken", getAuthToken(args["args"]["username"]))

    return response
