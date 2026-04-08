import mysql
import mysql.connector

databaseConnection = mysql.connector.connect(host="localhost", user="root", password="password")
database = databaseConnection.cursor()

try:
    print("using an existing database")
    database.execute("use fessUpDatabase")
    database.execute("drop database fessUpDatabase")
    database.execute("create database fessUpDatabase")
except mysql.connector.errors.ProgrammingError:
    print("making a new database")
    database.execute("create database fessUpDatabase")

database.execute("use fessUpDatabase;")


with open("./deploy/schema.sql", "r") as schemaFile:
    fullFile = ""
    for line in schemaFile.readlines():
        fullFile += line

    database.execute(fullFile)
