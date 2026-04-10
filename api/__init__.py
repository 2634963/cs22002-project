# import every api endpoint file
import api.login                        as login
import api.log                          as log
import api.createPost                   as createPost
import api.adminViewPostApprovalList    as adminViewPostApprovalList
import api.adminSetPostApproval         as adminSetPostApproval
import api.viewPostList                 as viewPostList
import api.postComment                  as postComment
import api.adminRemoveComment           as adminRemoveComment
import api.adminRemovePost              as adminRemovePost
import api.viewPostWithComments         as viewPostWithComments
import api.getExtraInformation          as getExtraInformation
import api.adminGiveCommentApproval     as adminGiveCommentApproval
import api.signup                       as signup
import api.getUsernameFromUserId        as getUsernameFromUserId
import api.purchaseExtraInformation     as purchaseExtraInformation
import api.adminViewCommentApprovalList as adminViewCommentApprovalList

# a list of every endpoint that should be accessible to an end user
# an api function that isnt in this dict can still be called from other python files but will not be accessoible from /api/<endpoint>
endpoints = {
    "login":{
        #            string      string
        "requires":["username", "password"],
        "module":login
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

    "adminViewPostApprovalList":{
        "requires":[],
        "module":adminViewPostApprovalList
    },

    "adminViewCommentApprovalList":{
        "requires":[],
        "module":adminViewCommentApprovalList
    },

    "adminSetPostApproval":{
        #            string    bool
        "requires":["postId", "approved"],
        "module":adminSetPostApproval
    },

    "adminGiveCommentApproval":{
        #            string       bool
        "requires":["commentId", "approved"],
        "module":adminGiveCommentApproval
    },

    "viewPostList":{
        #            string
        "requires":["from", "to"],
        "module":viewPostList
    },

    "postComment":{
        #            string    string
        "requires":["postId", "content"],
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

    "viewPostWithComments":{
        #            string    string        string
        "requires":["postId", "startIndex", "endIndex"],
        "module":viewPostWithComments
    },

    "getExtraInformation":{
        #            string
        "requires":["postId"],
        "module":getExtraInformation
    },

    "signup":{
        #
        "requires":["username", "password"],
        "module":signup
    },

    "getUsernameFromUserId":{
        "requires":["userId"],
        "module":getUsernameFromUserId
    },

    "purchaseExtraInformation":{
        "requires":["postId", "cardNumber", "expireMonth", "expireYear", "ccv", "paymentAmountPence"],
        "module":purchaseExtraInformation
    }
}
