from api._databaseConnection import database

print(__file__ + " has nothing to do with the database and must be updated")

import requests

PAYMENT_PROCESSOR_URL = "http://127.0.0.1:3001"

def call(args):
    # ensure that all of the arguments required are present, else return 400 bad request
    if "cardNumber" not in args:
        return 400

    if "expireMonth" not in args:
        return 400

    if "expireYear" not in args:
        return 400

    if "ccv" not in args:
        return 400

    if "paymentAmountPence" not in args:
        return 400

    # every argument exists, make the call to the payment processor
    response = requests.get(PAYMENT_PROCESSOR_URL, {"cardNumber":args["cardNumber"], "expireMonth":args["expireMonth"], "expireYear":args["expireYear"], "ccv":args["ccv"], "paymentAmountPence":args["paymentAmountPence"]})

    # and return what it said
    return 200 if (200 <= response.status_code < 300) else 400
