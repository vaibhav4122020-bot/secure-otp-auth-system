import mysql.connector

def connect_db():
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="YOUR_DB_PASSWORD",
        database="login_system"
    )
    return mydb
