# Example of Setting up a Postgres database using Psycopg2

# Import Database
import psycopg2

# Connect to the Database
connection = psycopg2.connect(database="development", user="postgres", password="Postgres101", port="5432")

# Create the Cursor
cursor = connection.cursor()

# Query
query = "INSERT INTO Coders (id, name, email, me@paulnicholasfoley.com) VALUES(1, 'Paul Foley');"
cursor.execute(query)

# Commit to the Database
connection.commit()

# Query
query = "INSERT INTO Programs (id, name, coders_id) VALUES(1, 'Best App Ever', 1);"
cursor.execute(query)

# Commit to the Database
connection.commit()

# Query
query = "INSERT INTO Bugs (id, name, description, program_id, coders_id) VALUES(1, 'A Bad Bad Bug', 1, 1);"
cursor.execute(query)

# Commit to the Database
connection.commit()


# Query
query = "SELECT * FROM Bugs LIMIT 10;"
cursor.execute(query)
results = cursor.fetchall() #Can also .fetchone()

# Print Results
print(results)

# Close the Connection - Note: ALWAYS CLOSE THE CONNECTION
connection.close()

