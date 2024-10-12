# Write a Python program to update the position of the employee with id=2 to 'Senior Developer'.

import mysql.connector
mydatabase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "haseeb725",
    database = "employees"
)
my_cursor = mydatabase.cursor()
query = ("""UPDATE employees SET position = 'Senior Developer' WHERE id = 2'""")
my_cursor.execute(query)
mydatabase.commit()
result = my_cursor.fetchall()
for a in result:
    print(a)
my_cursor.close()
mydatabase.close()   