from api._databaseConnection import database

import flask

print(__file__ + " has nothing to do with the database and must be updated")

# this endpoint is for a user removing one of their own comments, without the ability to give a reason

def call(args):
    return flask.Response(status=501)
