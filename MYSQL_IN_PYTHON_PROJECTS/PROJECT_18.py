# How do you modify the program to order by salary in descending order?

import mysql.connector
mydatabase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "haseeb725",
    database = "employees"
)
my_cursor = mydatabase.cursor()
query = ("""select * from employees order by age desc """)
my_cursor.execute(query)
mydatabase.commit()
result = my_cursor.fetchall()
for a in result:
    print(a)
my_cursor.close()
mydatabase.close()   