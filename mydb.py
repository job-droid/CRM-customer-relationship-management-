import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '7390'
)

cursorObject = database.cursor()
cursorObject.execute("CREATE DATABASE DCRM_db")

print("Database Created")