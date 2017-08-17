# Example of Setting up a Postgres database using Psycopg2

# Import Database
import psycopg2

# Connect to the Database
connection = psycopg2.connect(database="development", user="postgres", password="Postgres101", port="5432")

# Create the Cursor
cursor = connection.cursor()

# Query
query = "INSERT INTO Coders (CoderId, Name) VALUES(1, 'Paul Foley');"
cursor.execute(query)

# Commit to the Database
connection.commit()

# Query
query = "SELECT Name FROM Coders LIMIT 10;"
cursor.execute(query)
results = cursor.fetchall() #Can also .fetchone()

# Print Results
print(results)

# Close the Connection - Note: ALWAYS CLOSE THE CONNECTION
connection.close()

