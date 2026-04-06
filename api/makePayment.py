import flask
import requests

PAYMENT_PROCESSOR_URL = "http://127.0.0.1:3001"

def call(args):
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

    response = requests.get(PAYMENT_PROCESSOR_URL, {"cardNumber":args["cardNumber"], "expireMonth":args["expireMonth"], "expireYear":args["expireYear"], "ccv":args["ccv"], "paymentAmountPence":args["paymentAmountPence"]})

    return 200 if (200 <= response.status_code < 300) else 400
