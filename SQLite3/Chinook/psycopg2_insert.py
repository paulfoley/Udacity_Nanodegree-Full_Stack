## Example of INSERT using psycopg2
#!/usr/bin/python

# Import Database
import psycopg2

# Connect to the Database
connection = psycopg2.connect(database="chinook", user="postgres", password="Postgres101", port="5432")

# Create the Cursor
cursor = connection.cursor()

# Query
query = "INSERT INTO Coders (CoderId, Name) VALUES(1, 'Paul Foley');"
cursor.execute(query)

# Commit to the Database
connection.commit()

# Close the Connection - Note: ALWAYS CLOSE THE CONNECTION
connection.close()
