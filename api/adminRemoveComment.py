from api._databaseConnection import database

import flask

print(__file__ + " has nothing to do with the database and must be updated")

# this endpoint is for an admin removing a comment from a post, which they may give a reason for

def call(args):
    return flask.Response(status=501)
