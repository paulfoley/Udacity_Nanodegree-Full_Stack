## Example of SELECT using psycopg2

# Import Database
import psycopg2

# Connect to the database
connection = psycopg2.connect(database="chinook", user="postgres", password="Postgres101", port="5432")

# Create the Cursor
cursor = connection.cursor()

# Query
query = "SELECT Customer.FirstName FROM Customer LIMIT 10;"
cursor.execute(query)
results = cursor.fetchall() #Can also .fetchone()

# Print Results
print(results)

# Close Connection - Note: ALWAYS CLOSE THE CONNECTION
connection.close()