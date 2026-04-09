import secrets

print(__file__ + " has nothing to do with the database and must be updated")

# THIS ASSUMES THAT THE SIGN IN WAS SUCCESSFUL
def getAuthToken(username):
    tokenString = ""

    for i in range(32):
        tokenString += chr(ord('a') + secrets.SystemRandom().randint(0, 25))

    return tokenString
