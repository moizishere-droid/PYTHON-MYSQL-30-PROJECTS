#  Write a Python program to create a table 'employees' with columns: id, name, age, and position.

import mysql.connector
mydatabase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "haseeb725",
    database = "employees"
)
my_cursor = mydatabase.cursor()
query = ("""create table if not exists employees ( id int auto_increment primary key
        , name varchar(255) not null
        , age int , position varchar(255) not null)""")
my_cursor.execute(query)
my_cursor.close()
mydatabase.close()    