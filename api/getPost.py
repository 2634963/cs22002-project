from api._databaseConnection import database

import flask

print(__file__ + " has nothing to do with the database and must be updated")

def call(args):
    return flask.Response(status=501)
