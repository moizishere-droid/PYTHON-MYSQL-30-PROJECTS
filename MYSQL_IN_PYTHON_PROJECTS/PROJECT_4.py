# . How would you create a table 'departments' with columns: dept_id, dept_name using Python?

import mysql.connector
mydatabase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "haseeb725",
    database = "employees"
)
my_cursor = mydatabase.cursor()
query = ("""create table if not exists departments ( dept_id int auto_increment primary key
        , dept_name varchar(255) not null)""")
my_cursor.execute(query)
my_cursor.close()
mydatabase.close()    