# sqlite3 SELECT with COUNT and JOIN

# Import Database
import sqlite3

# Connect to Database
connection = sqlite3.connect("chinook.db")

# Create Cursor
cursor = connection.cursor()

# Query
QUERY = "SELECT Track.GenreId, count(MediaType.MediaTypeId) AS Num FROM Track JOIN MediaType ON Track.MediaTypeId = MediaType.MediaTypeId WHERE Track.GenreId = 9 AND MediaType.MediaTypeID = 1;"
cursor.execute(QUERY)
results = cursor.fetchall()

# Print Results
print(results[0])

# Close the Connection - Note: ALWAYS CLOSE THE CONNECTION
connection.close()