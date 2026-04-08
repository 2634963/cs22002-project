import bcrypt

def hashPassword(plaintext):
    return bcrypt.hashpw(plaintext.encode("utf-8"), bcrypt.gensalt())

def verifyPassword(plaintext, hashedBytes):
    return bcrypt.checkpw(plaintext.encode("utf-8"), hashedBytes)
