# import every api endpoint file
import api.makePayment              as makePayment
import api.attemptLogin             as attemptLogin
import api.log                      as log
import api.createPost               as createPost
import api.adminGivePostApproval    as adminGivePostApproval
import api.getPost                  as getPost
import api.postComment              as postComment
import api.adminRemoveComment       as adminRemoveComment
import api.adminRemovePost          as adminRemovePost
import api.userRemoveComment        as userRemoveComment
import api.getComments              as getComments
import api.getExtraInfo             as getExtraInfo
import api.adminGiveCommentApproval as adminGiveCommentApproval
import api.createAccount            as createAccount

# a list of every endpoint that should be accessible to an end user
# an api function that isnt in this dict can still be called from other python files but will not be accessoible from /api/<endpoint>
endpoints = {
    "makePayment":{
        #            16d int       int            int           int    int
        "requires":["cardNumber", "expireMonth", "expireYear", "ccv", "paymentAmountPence"],
        "module":makePayment
    },

    "attemptLogin":{
        #            string      string
        "requires":["username", "password"],
        "module":attemptLogin
    },

    "log":{
        #           any number of args, interpreted as a string
        "requires":[],
        "module":log
    },

    "createPost":{
        #            string   string
        "requires":["title", "content"],
        "module":createPost
    },

    "adminGivePostApproval":{
        #            string    bool
        "requires":["postId", "approved"],
        "module":adminGivePostApproval
    },

    "adminGiveCommentApproval":{
        #            string       bool
        "requires":["commentId", "approved"],
        "module":adminGiveCommentApproval
    },

    "getPost":{
        #            string
        "requires":["postId"],
        "module":getPost
    },

    "postComment":{
        #            string    string    string
        "requires":["postId", "userId", "content"],
        "module":postComment
    },

    "adminRemoveComment":{
        #            string       string
        "requires":["commentId", "removalReason"],
        "module":adminRemoveComment
    },

    "adminRemovePost":{
        #            string    string
        "requires":["postId", "removalReason"],
        "module":adminRemovePost
    },

    "userRemoveComment":{
        #            string
        "requires":["commentId"],
        "module":userRemoveComment
    },

    "getComments":{
        #            string    string        string
        "requires":["postId", "startIndex", "endIndex"],
        "module":getComments
    },

    "getExtraInfo":{
        #            string
        "requires":["postId"],
        "module":getExtraInfo
    },

    "createAccount":{
        #
        "requires":["username", "password"],
        "module":createAccount
    }
}
