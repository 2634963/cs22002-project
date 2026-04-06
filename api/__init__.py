import api.makePayment as makePayment
import api.attemptLogin as attemptLogin

endpoints = {
    "makePayment":{
        "requires":["cardNumber", "expireMonth", "expireYear", "ccv", "paymentAmountPence"],
        "module":makePayment
    },

    "attemptLogin":{
        "requires":["username", "password"],
        "module":attemptLogin
    }
}
