# import every api endpoint file
import api.makePayment as makePayment
import api.attemptLogin as attemptLogin
import api.log as log

# a list of every endpoint that should be accessible to an end user
# an api function that isnt in this dict can still be called from other python files but will not be accessoible from /api/<endpoint>
endpoints = {
    "makePayment":{
        "requires":["cardNumber", "expireMonth", "expireYear", "ccv", "paymentAmountPence"],
        "module":makePayment
    },

    "attemptLogin":{
        "requires":["username", "password"],
        "module":attemptLogin
    },

    "log":{
        "requires":[],
        "module":log
    }
}
