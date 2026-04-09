import secrets
from api._databaseConnection import database
import time

# THIS ASSUMES THAT THE SIGN IN WAS SUCCESSFUL
def makeAuthToken(userID):
    tokenString = ""

    for i in range(32):
        tokenString += chr(ord('a') + secrets.SystemRandom().randint(0, 25))

    database.execute(f"insert into authTokens (authTokenString, userID, createdTimestamp) values ('{tokenString}', '{userID}', '{int(time.time())}')")

    return tokenString

def verifyAuthToken(authToken):
    authTokenList = database.execute(f"select * from authTokens where authTokenString='{authToken}'").fetchall()

    if len(authTokenList) == 0:
        return False

    if int(time.time()) - authTokenList[0][1] > 86400:
        deleteAuthToken(authToken)
        return False

    return True

def deleteAuthToken(authToken):
    database.execute(f"delete from authTokens where authTokenString='{authToken}'")
