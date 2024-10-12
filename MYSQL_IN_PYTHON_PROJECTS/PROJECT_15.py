# How would you select all employees whose names start with the letter 'A' using Python?

import mysql.connector
mydatabase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "haseeb725",
    database = "employees"
)
my_cursor = mydatabase.cursor()
user_input = input("Enter the name of the employees: ")
query = ("""select * from employees where name like %s """)
my_cursor.execute(query,("%"+user_input+"%",))
mydatabase.commit()
result = my_cursor.fetchall()
for a in result:
    print(a)
my_cursor.close()
mydatabase.close()   