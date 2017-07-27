# sqlite3 SELECT with JOIN

# Import Database
import sqlite3

# Connect to the database
connection = sqlite3.connect("chinook.db")

# Create the Cursor
cursor = connection.cursor()

# Query
QUERY = "SELECT Track.Name, Genre.Name FROM Track JOIN Genre ON Track.GenreId = Genre.GenreId"
cursor.execute(QUERY)
results = cursor.fetchall()

# Print Results
print(results)

# Close the Connection - Note: ALWAYS CLOSE THE CONNECTION
connection.close()