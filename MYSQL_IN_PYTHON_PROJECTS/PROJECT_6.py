# . Write a Python program to create a table 'projects' that has a foreign key reference to the dept_id 
# from the 'departments' table.

import mysql.connector
mydatabase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "haseeb725",
    database = "employees"
)
my_cursor = mydatabase.cursor()
create_table_query = """
        CREATE TABLE IF NOT EXISTS projects (
            project_id INT AUTO_INCREMENT PRIMARY KEY,
            project_name VARCHAR(255) NOT NULL,
            dept_id INT, FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
            ON DELETE CASCADE ON UPDATE CASCADE
        )
        """
my_cursor.execute(create_table_query)
mydatabase.commit()
my_cursor.close()
mydatabase.close()    