#database
import sqlite3
import json

from api._passwordHashes import hashPassword

#connect to database
def connectDb():
    try:
        connection = sqlite3.connect("./fessUpDatabase.db", check_same_thread=False)
        database = connection.cursor()
        print("COnected Database")
        return database, connection
    except:
        print("Failed to connerct")

#create table functions
def createPostTable(database, connection):
    createTable = 'CREATE TABLE IF NOT EXISTS posts (postID INTEGER NOT NULL PRIMARY KEY, posterID INTEGER NOT NULL, title TEXT NOT NULL, content TEXT NOT NULL, extraInfo TEXT, approved INTEGER, FOREIGN KEY(posterID) REFERENCES users(userID))'
    database.execute(createTable)
    connection.commit()

def createUserTable(database, connection):
    createTable = 'CREATE TABLE IF NOT EXISTS users (userID INTEGER NOT NULL PRIMARY KEY, username TEXT NOT NULL, password TEXT NOT NULL, admin INTEGER NOT NULL, FOREIGN KEY(userID) REFERENCES users(userID))'
    database.execute(createTable)
    connection.commit()

def createExtraInfoAccessTable(database, connection):
    createTable = 'CREATE TABLE IF NOT EXISTS extraInfoAccess (paymentID INTEGER NOT NULL PRIMARY KEY, userID INTEGER NOT NULL, postID INTEGER NOT NULL, FOREIGN KEY(userID) REFERENCES users(userID), FOREIGN KEY(postID) REFERENCES posts(postID))'
    database.execute(createTable)
    connection.commit()

def createCommentTable(database, connection):
    createTable = 'CREATE TABLE IF NOT EXISTS comments (commentID INTEGER NOT NULL PRIMARY KEY, authorUserID INTEGER NOT NULL, postID INTEGER NOT NULL, content TEXT NOT NULL, approved INTEGER NOT NULL, FOREIGN KEY(postID) REFERENCES posts(postID))'
    database.execute(createTable)
    connection.commit()

def createAuthTokenTable(database, connection):
    createTable = 'CREATE TABLE IF NOT EXISTS authTokens (authTokenString TEXT NOT NULL PRIMARY KEY, createdTimestamp INTEGER NOT NULL, userID INTEGER NOT NULL, FOREIGN KEY(userID) REFERENCES users(userID))'
    database.execute(createTable)
    connection.commit()

def createTables(database, connection):
    createPostTable(database, connection)
    createUserTable(database, connection)
    createExtraInfoAccessTable(database, connection)
    createCommentTable(database, connection)
    createAuthTokenTable(database, connection)
    print("Tables Create / Exist")

#load datga fucntionss
def loadPostData(database, connection):
    with open("./api/jsons/postData.json", "r") as data:
        posts = json.load(data)
        for post in posts:
            database.execute("SELECT EXISTS(SELECT 1 FROM posts WHERE postID=?)", (post["postID"]))
            if database.fetchone()[0] == 0:
                database.execute(f"INSERT INTO posts (postID, posterID, title, content, extraInfo, approved) VALUES ('{post["postID"]}', '{post["posterID"]}', '{post["title"]}', '{post["content"]}', '{post["extraInfo"]}', '{post["approved"]}')")
                print("post inserted")
            else:
                print(f"Post with ID {post['postID']} already exists")
    connection.commit()
    print("loaded post data")

def loadUserData(database, connection):
    with open("./api/jsons/userData.json", "r") as data:
        users = json.load(data)
        for user in users:
            database.execute(f"SELECT EXISTS(SELECT 1 FROM users WHERE userID={user['userID']})")
            if database.fetchone()[0] == 0:
                database.execute(f"INSERT INTO users (userID, username, password, admin) VALUES ('{user["userID"]}', '{user["username"].lower()}', \"{hashPassword(user["password"])}\", '{user["admin"]}')")
                print("user inserted")
            else:
                print(f"User with ID {user['userID']} already exists")
    connection.commit()
    print("loaded user data")

def loadCommentData(database, connection):
    with open("./api/jsons/commentData.json", "r") as data:
        comments = json.load(data)
        for comment in comments:
            print(comment)
            database.execute(f"SELECT EXISTS(SELECT 1 FROM comments WHERE commentID='{comment["commentID"]}')")
            if database.fetchone()[0] == 0:
                database.execute(f"INSERT INTO comments (postID, authorUserID, content, approved, commentID) VALUES ('{comment["postID"]}', '{comment["authorUserID"]}', '{comment["content"]}', '{comment["approved"]}', '{comment["commentID"]}')")
                print("comment inserted")
            else:
                print(f"Comment with ID {comment['commentID']} already exists")
    connection.commit()
    print("loaded comment data")

def loadExtraInfoData(database, connection):
    with open("./api/jsons/extraInfoData.json", "r") as data:
        extraInfo = json.load(data)
        for info in extraInfo:
            database.execute(f"SELECT EXISTS(SELECT 1 FROM extraInfoAccess WHERE paymentID={info["paymentID"]})")
            if database.fetchone()[0] == 0:
                database.execute(f"INSERT INTO extraInfoAccess (paymentID, userID, postID) VALUES ('{info["paymentID"]}', '{info["userID"]}', '{info["postID"]}')")
                print("extra info access inserted")
            else:
                print(f"Extra info access with ID {info['paymentID']} already exists")
    connection.commit()
    print("loaded extra info access data")

def loadData(database, connection):
    loadPostData(database, connection)
    loadUserData(database, connection)
    loadCommentData(database, connection)
    loadExtraInfoData(database, connection)
    print("All data loaded")

#display ALLL data
def displayAllData(database):
    database.execute("SELECT * FROM posts")
    print("posts:")
    for post in database.fetchall():
        print(post)
    database.execute("SELECT * FROM users")
    print("users:")
    for user in database.fetchall():
        print(user)
    database.execute("SELECT * FROM comments")
    print("comments:")
    for comment in database.fetchall():
        print(comment)
    database.execute("SELECT * FROM extraInfoAccess")
    print("extra info access:")
    for access in database.fetchall():
        print(access)

def printJson():
    with open("./api/jsons/userData.json", "r") as data:
        users = json.load(data)
        for user in users:
            print(user["userID"])
    

database, connection = connectDb()

createTables(database, connection)

print(printJson())

loadData(database, connection)

displayAllData(database)

#TO DO: ADD QUERIES + CREATE DATA
