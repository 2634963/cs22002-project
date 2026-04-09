import flask

from api.makePayment import call as makePayment
from api._databaseConnection import database, connection
from api._getAuthToken import verifyAuthToken

def call(args):
    if "authToken" not in args["cookies"]:
        return flask.Response("please sign in", 401)

    if not verifyAuthToken(args["cookies"]["authToken"]):
        return flask.Response("please sign in", 401)

    if "postId" not in args["args"]:
        return flask.Response("no postID", 400)

    if "cardNumber" not in args["args"]:
        return flask.Response("no card number", 400)

    if "expireMonth" not in args["args"]:
        return flask.Response("no expiry month", 400)

    if "expireYear" not in args["args"]:
        return flask.Response("no expiry year", 400)

    if "ccv" not in args["args"]:
        return flask.Response("no ccv", 400)

    args["args"] = dict(args["args"])

    args["args"]["paymentAmountPence"] = 100

    response = makePayment(args)

    if response == 200:
        # payment success
        paymentId = database.execute("select count(*) from extraInfoAccess").fetchall()[0][0]
        userId = database.execute(f"select userId from authTokens where authTokenString='{args["cookies"]["authToken"]}'").fetchall()[0][0]

        database.execute(f"insert into extraInfoAccess (paymentID, userID, postID) values ('{paymentId}', '{userId}', '{args["args"]["postId"]}')")

        connection.commit()

    else:
        # payment unsuccess
        return flask.Response("payment failed", 400)

    return flask.Response("success", 200)
