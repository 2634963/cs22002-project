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

#create table functions
def createPostTable(database, connection):
    createTable = 'CREATE TABLE IF NOT EXSTS posts (postID INTEGER PRIMARY KEY, posterID INTEGER, title TEXT, content TEXT, extraInfo TEXT NULL, approved INTEGER, FOREIGN KEY(posterID) REFERENCES users(userID))'
    database.execute(createTable)
    connection.commit()

def createUserTable(database, connection):
    createTable = 'CREATE TABLE IF NOT EXSTS users (userID INTEGER PRIMARY KEY, username TEXT, password TEXT, admin INTEGER, FOREIGN KEY(userID) REFERENCES users(userID))'
    database.execute(createTable)
    connection.commit()

def createExtraInfoAccessTable(database, connection):
    createTable = 'CREATE TABLE IF NOT EXSTS users (paymentID INTEGER PRIMARY KEY, userID INTEGER, postID INTEGER, FOREIGN KEY(userID) REFERENCES users(userID), FOREIGN KEY(postID) REFERENCES posts(postID))'
    database.execute(createTable)
    connection.commit()

def createCommentTable(database, connection):
    createTable = 'CREATE TABLE IF NOT EXSTS users (commentID INTEGER PRIMARY KEY, postID INTEGER, content TEXT, approved INTEGER, FOREIGN KEY(postID) REFERENCES posts(postID))'
    database.execute(createTable)
    connection.commit()

def createTables(database, connection):
    createPostTable(database, connection)
    createUserTable(database, connection)
    createExtraInfoAccessTable(database, connection)
    createCommentTable(database, connection)
    print("Tables Create / Exist")

#load datga fucntionss
def loadPostData(database, connection):
    with open("./data/posts.json", "r") as data:
        posts = json.load(data)
        for post in posts:
            database.execute("SELECT EXISTS(SELECT 1 FROM posts WHERE postID=?)", (post["postID"]))
            if database.fetchone()[0] == 0:
                database.execute("INSERT INTO posts (posterID, title, content, extraInfo, approved) VALUES (?, ?, ?, ?, ?)", (post["posterID"], post["title"], post["content"], post["extraInfo"], post["approved"]))
                print("post inserted")
            else:
                print(f"Post with ID {post['postID']} already exists")
    connection.commit()
    print("loaded post data")

def loadUserData(database, connection):
    with open("./data/users.json", "r") as data:
        users = json.load(data)
        for user in users:
            database.execute("SELECT EXISTS(SELECT 1 FROM users WHERE userID=?)", (user["userID"]))
            if database.fetchone()[0] == 0:
                database.execute("INSERT INTO users (username, password, admin) VALUES (?, ?, ?)", (user["username"], user["password"], user["admin"]))
                print("user inserted")
            else:
                print(f"User with ID {user['userID']} already exists")

database, connection = connectDb()

createTables(database, connection)

