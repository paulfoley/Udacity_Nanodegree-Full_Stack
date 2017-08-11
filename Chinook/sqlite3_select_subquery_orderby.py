## Example of a Subquery with Order By

# Import the Database
import sqlite3

# Connect to the Database
connection = sqlite3.connect("chinook.db")

# Create the Cursor
cursor = connection.cursor()

# Query
QUERY = "SELECT Total FROM Invoice, (SELECT avg(Total) AS av FROM Invoice) AS avg_invoice WHERE Total > av ORDER BY Total ASC;"
cursor.execute(QUERY)
results = cursor.fetchall()

# Print Results
print(results)

# Close the Connection - Note: ALWAYS CLOSE THE CONNECTION
connection.close()