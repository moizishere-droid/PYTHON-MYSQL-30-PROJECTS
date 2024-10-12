# How would you delete all employees who are older than 60 using Python?

import mysql.connector
mydatabase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "haseeb725",
    database = "employees"
)
my_cursor = mydatabase.cursor()
query = ("""delete employees where age>60""")
my_cursor.execute(query)
mydatabase.commit()
result = my_cursor.fetchall()
for a in result:
    print(a)
my_cursor.close()
mydatabase.close()   