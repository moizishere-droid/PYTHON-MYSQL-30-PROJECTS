#  How do you insert a single record into the 'employees' table with values id=1, name='John',
# age=30, and position='Manager' in Python?

import mysql.connector
mydatabase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "haseeb725",
    database = "employees"
)
my_cursor = mydatabase.cursor()
query = ("""insert into employees (name,age,position) values(%s,%s,%s)""")
values = [("john",30,"Manager"),("moiz",34,"HR"),("ANAS",50,"SALES")]
# my_cursor.execute(query,values)
my_cursor.executemany(query,values)
print("row addes" , my_cursor.rowcount)
my_cursor.close()
mydatabase.close()    