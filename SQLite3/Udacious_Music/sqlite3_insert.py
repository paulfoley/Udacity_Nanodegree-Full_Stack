## Example of INSERT using sqlite3

# Import the Database
import sqlite3

# Connect to the Database
connection = sqlite3.connect("UdaciousMusic.db")

# Create the Cursor
cursor = connection.cursor()

# Query
query = "INSERT INTO Coders (CoderId, Name) VALUES(1, 'Paul Foley');"
cursor.execute(query)

# Commit to the Database
connection.commit()

# Close the Connection - Note: ALWAYS CLOSE THE CONNECTION
connection.close()