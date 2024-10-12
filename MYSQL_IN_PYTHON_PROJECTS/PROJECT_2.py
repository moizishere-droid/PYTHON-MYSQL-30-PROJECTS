# How would you modify the program to check if the database already exists before creating it?

import mysql.connector
mydatabase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "haseeb725"
)
my_cursor = mydatabase.cursor()
query = ("create database if not exists employees")
my_cursor.execute(query)
my_cursor.close()
mydatabase.close()    