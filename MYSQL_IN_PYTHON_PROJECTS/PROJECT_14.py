# Write a Python program to select employees who work as 'Engineer' using the WHERE clause.

import mysql.connector
mydatabase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "haseeb725",
    database = "employees"
)
my_cursor = mydatabase.cursor()
query = ("""select * from employees where position = 'Engineer' """)
my_cursor.execute(query)
mydatabase.commit()
result = my_cursor.fetchall()
for a in result:
    print(a)
my_cursor.close()
mydatabase.close()   