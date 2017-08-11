## Example of SELECT using sqlite3

# Import the Database
import sqlite3

# Connect to the Database
connection = sqlite3.connect("chinook.db")

# Create the Cursor
cursor = connection.cursor()

# Query
QUERY = "SELECT Customer.FirstName FROM Customer LIMIT 10;"
cursor.execute(QUERY)
results = cursor.fetchall() # Can also .fetchone()

# Print Results
print (results)

# Close the connection - Note: ALWAYS CLOSE THE CONNECTION
connection.close()
