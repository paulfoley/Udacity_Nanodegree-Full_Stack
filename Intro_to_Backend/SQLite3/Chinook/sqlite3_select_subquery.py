## Examples of a Subquery with Group By

# Import the Database
import sqlite3

# Connect to the Database
connection = sqlite3.connect("chinook.db")

# Create the Cursor
cursor = connection.cursor()

# Query
QUERY = "SELECT avg(Max) FROM (SELECT max(Total) as Max FROM Invoice GROUP BY BillingCountry) AS maxes;"
cursor.execute(QUERY)
results = cursor.fetchall()

# Print Results
print(results[0][0])

# Close the connection - Note: ALWAYS CLOSE THE CONNECTION
connection.close()