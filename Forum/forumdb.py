## Database functions, "Get" and "Add" for the web forum.

# Import Libraries
import time
import psycopg2

# Define Functions
def get_all_posts():
  '''Get posts from database.'''

  # Connect to Database and create Cursor
  connection = psycopg2.connect('dbname=forum')
  cursor = connection.cursor()

  # Query
  query = "SELECT time, content FROM posts ORDER BY time DESC"
  cursor.execute(query)

  # Create a "posts" dictionary
  posts = ({'content': str(row[1]), 'time': str(row[0])} for row in cursor.fetchall())
  
  # Close the Connection
  connection.close()

  #Return the "posts" dictionary
  return posts

def add_post(content):
  '''Add a post to the database.'''

  # Connect to Database and create Cursor
  connection = psycopg2.connect('dbname=forum')
  cursor = connection.cursor()

  # Query
  query = "INSERT INTO posts (content) VALUES (%s)"
  cursor.execute(query, (content,))

  # Commit to the Database
  connection.commit()

  # Close the Connection
  connection.close()
