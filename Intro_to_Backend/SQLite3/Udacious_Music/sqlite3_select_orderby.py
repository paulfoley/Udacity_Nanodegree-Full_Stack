# Example of DB-API

#Import Database
import sqlite3

# Connect to the database
connection = sqlite3.connect("UdaciousMusic.db")

# Create the cursor
cursor = connection.cursor()

# Query
QUERY = "SELECT name, CoderId FROM Coders ORDER BY Name ASC;"
cursor.execute(QUERY)
rows = cursor.fetchall()

# Print Results
print(rows)

# Close the connection - Note: ALWAYS CLOSE THE CONNECTION
connection.close()