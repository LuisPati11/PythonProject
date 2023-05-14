import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='jobs',
    port='4306'
)

