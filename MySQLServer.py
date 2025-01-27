import mysql.connector

connection = mysql.connector.connect(
    user = 'alx_student',
    password = 'empty@password',
    host = '127.0.0.1',
    use_pure = True
)

cursor = connection.cursor()
try:
    cursor.execute("CREATE DATABASE alx_book_store")
    print("Database 'alx_book_store' created successfully!")
except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    cursor.close()
    connection.close()