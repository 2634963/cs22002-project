import bcrypt

def hashPassword(plaintext):
    returnThis = bcrypt.hashpw(plaintext.encode("utf-8"), bcrypt.gensalt())
    print("1: ", returnThis)
    return returnThis

def verifyPassword(plaintext, hashedBytes):
    return bcrypt.checkpw(plaintext.encode("utf-8"), hashedBytes)
