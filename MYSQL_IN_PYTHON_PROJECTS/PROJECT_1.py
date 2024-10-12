# Write a Python program to create a new MySQL database named 'employees'

import mysql.connector
mydatabase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "haseeb725"
)
my_cursor = mydatabase.cursor()
query = ("create database employees")
my_cursor.execute(query)
my_cursor.close()
mydatabase.close()    