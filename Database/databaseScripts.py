import mysql.connector

hopedb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="yourpassword",
    database="hopedatacenter"
)

hopecursor = hopedb.cursor()

# Create Database
hopecursor.execute("CREATE DATABASE HOPEDataCenter")

# show database
hopecursor.execute("SHOW DATABASES")

for x in hopecursor:
  print(x)

# Create table
hopecursor.execute("CREATE TABLE products (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), price VARCHAR(255))")

# Rename Table
hopecursor.execute('RENAME TABLE customers TO products')

# show tables
hopecursor.execute("SHOW TABLES")

for x in hopecursor:
  print(x)

# Delete table
hopecursor.execute('DROP TABLE customers')

query = "INSERT INTO products (id, name, price) VALUES (%s, %s, %s)"
val = (12, "Tablet", "12000000")
hopecursor.execute(query, val)

hopedb.commit()

print(hopecursor.rowcount, "record inserted.")
