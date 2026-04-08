from api._databaseConnection import database

print(__file__ + " has nothing to do with the database and must be updated")

import requests
import flask

PAYMENT_PROCESSOR_URL = "http://127.0.0.1:3001"

def call(args):
    # ensure that all of the arguments required are present, else return 400 bad request
    if "cardNumber" not in args["args"]:
        return flask.Response("no card number", 400)

    if "expireMonth" not in args["args"]:
        return flask.Response("no expiry month", 400)

    if "expireYear" not in args["args"]:
        return flask.Response("no expiry year", 400)

    if "ccv" not in args["args"]:
        return flask.Response("no ccv", 400)

    if "paymentAmountPence" not in args["args"]:
        return flask.Response("no payment amount", 400)

    # every argument exists, make the call to the payment processor
    response = requests.get(PAYMENT_PROCESSOR_URL, {"cardNumber":args["args"]["cardNumber"], "expireMonth":args["args"]["expireMonth"], "expireYear":args["args"]["expireYear"], "ccv":args["args"]["ccv"], "paymentAmountPence":args["args"]["paymentAmountPence"]})

    # and return what it said
    return flask.Response(status=200) if (200 <= response.status_code < 300) else flask.Response(status=400)
