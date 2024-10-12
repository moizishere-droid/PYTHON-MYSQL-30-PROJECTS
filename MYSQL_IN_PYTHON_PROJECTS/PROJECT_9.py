# How do you handle errors when trying to insert a duplicate id in the 'employees' table?

import mysql.connector

try:
    # Establish a connection to the MySQL database
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="employees"
    )
    
    cursor = connection.cursor()

    insert_query = "INSERT INTO employees (id, name) VALUES (%s, %s)"
    values = (1, 'John Doe')  # Trying to insert duplicate 'id'

    cursor.execute(insert_query, values)

    connection.commit()

except mysql.connector.Error as e:
    if e.errno == 1062:  # Error code for duplicate entry
        print("Error: Duplicate ID detected. Please use a unique ID.")
    else:
        print(f"Error: {e}")

finally:
    if cursor:
        cursor.close()
    if connection.is_connected():
        connection.close()