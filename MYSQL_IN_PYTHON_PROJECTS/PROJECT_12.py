# . Write a Python program to select employees whose age is greater than 30

import mysql.connector

mydatabase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="haseeb725",
    database="employees"
)

my_cursor = mydatabase.cursor()

query = ("""select * from employees where age>=30""")
my_cursor.execute(query)
mydatabase.commit()
result = my_cursor.fetchall()

if result:
    for a in result:
        print(a)
else:
    print("No employees found with age >= 30")

my_cursor.close()
mydatabase.close()
