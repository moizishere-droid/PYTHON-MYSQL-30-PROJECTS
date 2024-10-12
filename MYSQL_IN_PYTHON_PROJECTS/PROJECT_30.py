# Write a Python program to perform a left join between 'employees' and 'departments' and show
# all employees even if they don't belong to a department


import mysql.connector
mydatabase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "haseeb725",
    database = "employees"
)
cursor = mydatabase.cursor()


# Perform LEFT JOIN
left_join_query = """
SELECT employees.name, departments.department_name
FROM employees
LEFT JOIN departments ON employees.department_id = departments.id
"""

cursor.execute(left_join_query)

# Fetch and print results
print("\nLEFT JOIN Results:")
for row in cursor.fetchall():
    print(row)

cursor.close()
mydatabase.close()