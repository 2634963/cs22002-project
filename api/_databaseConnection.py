#database
import sqlite3
import json

#connect to database
def connectDb():
    try:
        connection = sqlite3.connect("./fessUpDatabase.db")
        database = connection.cursor()
        print("COnected Database")
        return database, connection
    except:
        print("Failed to connerct")


def createPostTable(database, connection):
    createTable = 'CREATE TABLE IF NOT EXSTS posts (postID INTEGER PRIMARY KEY, posterID INTEGER, title TEXT, content TEXT, extraInfo TEXT NULL, approved INTEGER)'
    database.execute(createTable)
    connection.commit()

def createUserTable(database, connection):
    createTable = 'CREATE TABLE IF NOT EXSTS users (userID INTEGER PRIMARY KEY, username TEXT, password TEXT, admin INTEGER)'
    database.execute(createTable)
    connection.commit()

def createExtraInfoAccessTable(database, connection):
    createTable = 'CREATE TABLE IF NOT EXSTS users (paymentID INTEGER PRIMARY KEY, userID INTEGER, postID INTEGER)'
    database.execute(createTable)
    connection.commit()

def createCommentTable(database, connection):
    createTable = 'CREATE TABLE IF NOT EXSTS users (commentID INTEGER PRIMARY KEY, postID INTEGER, content TEXT, approved INTEGER)'
    database.execute(createTable)
    connection.commit()

def createTables(database, connection):
    createPostTable(database, connection)
    createUserTable(database, connection)
    createExtraInfoAccessTable(database, connection)
    createCommentTable(database, connection)
    print("Tables Create / Exist")

def loadPostData(database, connection):
    print("Loading post data...")

database, connection = connectDb()

createTables(database, connection)

