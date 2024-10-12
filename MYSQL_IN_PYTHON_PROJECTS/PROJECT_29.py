# Write a Python program to join the 'employees' and 'departments' tables on dept_id and display
# employee names with their respective department names

import mysql.connector
mydatabase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "haseeb725",
    database = "employees"
)
my_cursor = mydatabase.cursor()

query = ("""SELECT employees.name, departments.dept_name
FROM employees
INNER JOIN departments ON employees.dept_id = dept_id
""")
my_cursor.execute(query)
mydatabase.commit()
result = my_cursor.fetchall()
for a in result:
    print(a)
my_cursor.close()
mydatabase.close()   