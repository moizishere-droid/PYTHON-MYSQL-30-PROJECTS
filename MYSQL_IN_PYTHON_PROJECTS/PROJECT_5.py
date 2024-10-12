# How do you add an additional column 'salary' to the 'employees' table in Python?

import mysql.connector
mydatabase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "haseeb725",
    database = "employees"
)
my_cursor = mydatabase.cursor()
query = ("""alter table employees add column salary int""")
my_cursor.execute(query)
my_cursor.close()
mydatabase.close()    