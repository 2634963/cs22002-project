# import all of the tests we will run
import accountCreationAndSignin
import adminApprovingComments
import adminApprovingPosts
import adminDenyingComments
import adminDenyingPosts
import adminGetApprovalList
import getExtraInformation
import gettingComments
import gettingPosts
import makingComments
import makingPosts
import purchaseExtraInformation

# remove the database file if it exists
import os
os.system("rm ./fessUpDatabase.db")

# check that a url was given
import sys
if len(sys.argv) < 2:
    print("usage: python " + __file__.split("\\")[-1] + " <server url>")
    print("e.g. " + __file__.split("\\")[-1] + " 127.0.0.1:3000")

    exit(-1)

if not sys.argv[1].startswith("http"):
    sys.argv[1] = "http://" + sys.argv[1]


if not accountCreationAndSignin.test():
    # cant test without an account
    print("cannot run remaining tests without an account")
    exit(-1)

testSuccessDict = {}

testSuccessDict["making posts"] = makingPosts.test()
testSuccessDict["getting posts"] = gettingPosts.test()

testSuccessDict["making comments"] = makingComments.test()
testSuccessDict["getting comments"] = gettingComments.test()

# testSuccessDict["purchasing extra information"] = purchaseExtraInformation.test()
# testSuccessDict["getting extra information"] = getExtraInformation.test()
