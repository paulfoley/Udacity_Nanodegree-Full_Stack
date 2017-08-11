# sqlite3 SELECT with JOIN and Subquery

# Import Databases
import sqlite3

# Connect to a Database
connection = sqlite3.connect("chinook.db")

# Create Cursor
cursor = connection.cursor()

# Query
QUERY = "SELECT Genre.Name, count(Genre.Name) AS Total FROM Track JOIN Genre ON Track.GenreId = Genre.GenreId, (SELECT avg(Milliseconds) AS av FROM Track) as AVG_Track WHERE Milliseconds < av GROUP BY Genre.Name ORDER BY Total DESC;"
cursor.execute(QUERY)
results = cursor.fetchall()

# Print Results
print(results)

# Close the Connection
connection.close()