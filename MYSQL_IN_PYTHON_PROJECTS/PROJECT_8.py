# Write a Python program to insert multiple records into the 'departments' table.

import mysql.connector
mydatabase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "haseeb725",
    database = "employees"
)
my_cursor = mydatabase.cursor()
query = ("""insert into departments (dept_name) values (%s)""")
values = [("HR",),("CEO",),("COO",),("CHO",),("HOD",),("ENGR",),("MED",)]
my_cursor.executemany(query,values)
my_cursor.close()
mydatabase.close()    