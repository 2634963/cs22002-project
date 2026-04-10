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

print("\n========================================================\n")

testSuccessDict = {}

testSuccessDict["making posts"] = makingPosts.test()
print("\n========================================================\n")
testSuccessDict["getting posts"] = gettingPosts.test()

print("\n========================================================\n")
testSuccessDict["making comments"] = makingComments.test()
print("\n========================================================\n")
testSuccessDict["getting comments"] = gettingComments.test()
print("\n========================================================\n")

testSuccessDict["purchasing extra information"] = purchaseExtraInformation.test()
print("\n========================================================\n")
testSuccessDict["getting extra information"] = getExtraInformation.test()
