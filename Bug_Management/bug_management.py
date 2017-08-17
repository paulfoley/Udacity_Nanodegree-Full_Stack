# Example of Setting up a Postgres database using Psycopg2

# Import Database
import psycopg2

# Connect to the Database
connection = psycopg2.connect("dbname=development")

# Create the Cursor
cursor = connection.cursor()

# Query
query = "INSERT INTO Coders (name, email) VALUES('Paul Foley', 'me@paulnicholasfoley.com');"
cursor.execute(query)

# Commit to the Database
connection.commit()

# Query
query = "INSERT INTO Programs (name, coder_id) VALUES ('Best App Ever', 1);"
cursor.execute(query)

# Commit to the Database
connection.commit()

# Query
query = "INSERT INTO Bugs (name, program_id, coder_id) VALUES('A Bad Bad Bug', 1, 1);"
cursor.execute(query)

# Commit to the Database
connection.commit()


# Query
query = "SELECT * FROM Bugs LIMIT 10;"
cursor.execute(query)
results = cursor.fetchall() # Can also .fetchone()

# Print Results
print("Bug Table")
print(results)

# Close the Connection - Note: ALWAYS CLOSE THE CONNECTION
connection.close()

