import api.makePayment as makePayment

endpoints = {
    "makePayment":{
        "requires":["cardNumber", "expireMonth", "expireYear", "ccv", "paymentAmountPence"],
        "module":makePayment
    }
}
