import mysql.connector

def get_user(user_id):
  # Connect to the database
  conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="users"
  )
  cursor = conn.cursor()

  # Retrieve the user information
  query = "SELECT * FROM users WHERE id='" + user_id + "'"
  cursor.execute(query)
  user = cursor.fetchone()

  # Close the connection
  cursor.close()
  conn.close()

  return user

print(get_user("1"))
