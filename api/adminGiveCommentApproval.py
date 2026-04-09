from api._databaseConnection import database, connection

import flask

print(__file__ + " has nothing to do with the database and must be updated")

def call(args):
    if "commentId" not in args["args"]:
        return flask.Response("no comment id", 400)

    if "approved" not in args["args"]:
        return flask.Response("no approval", 400)

    if args["args"]["approved"] == 1:
        database.execute(f"update comments set approved where commendID='{args["args"]["commentId"]}'")
        connection.commit()

    elif args["args"]["approved"] == 0:
        database.execute(f"delete from comments where commendID='{args["args"]["commendId"]}'")
        connection.commit()

    else:
        return flask.Response("invalid approval value", 400)


    return flask.Response(status=200)
