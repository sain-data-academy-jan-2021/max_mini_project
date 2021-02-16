import pymysql
import os
from dotenv import load_dotenv

load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")

# Establish a database connection
connection = pymysql.connect(
  host,
  user,
  password,
  database
)

# A cursor is an object that represents a DB cursor,
# which is used to manage the context of a fetch operation.
cursor = connection.cursor()

# Execute SQL query
cursor.execute('SELECT product_id, drink, type, price, status FROM products')

# Gets all rows from the result
rows = cursor.fetchall()
for row in rows:
  print(f'Id: {int(row[0])}, Product: {str(row[1])}, Type: {str(row[2])}, Price: {int(row[3])}, Status: {str(row[4])}')

# Can alternatively get one result at a time
# while True:
#   row = cursor.fetchone()
#   if row == None:
#     break
#   print(f'First Name: {str(row[0])}, Last Name: {row[1]}, Age: {row[2]}')

# Closes the cursor so will be unusable from this point 
cursor.close()

# Closes the connection to the DB, make sure you ALWAYS do this
connection.close()