# Example of Python program that uses a DB-API Library to query a database

# Import Library for the Database
import sqlite3

# Connect to the Database
connection = sqlite3.connect('chinook.db')

# Create a Cursor - What actually runs queries and fetches results
cursor = connection.cursor()

# Query
query = "SELECT Album.Title FROM Album LIMIT 10"
cursor.execute(query)
results = cursor.fetchall() # Could also .fetchone()

# Print Results
print(results)

# Close the Connection
connection.close()