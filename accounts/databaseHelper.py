import mysql.connector
 
dataBase = mysql.connector.connect(
  host ="127.0.0.1",
  user ="user",
  passwd ="admin"
)
 
# preparing a cursor object
cursorObject = dataBase.cursor()
 
# creating database
cursorObject.execute("CREATE DATABASE CustomersDB")