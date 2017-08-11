# Example of SELECT query utilizing sqlite3 and printing as pandas DataFrame

# Import Database
import sqlite3
import pandas

# Connect to Database
connection = sqlite3.connect("chinook.db")

# Create Cursor
cursor = connection.cursor()

# Query
QUERY = "SELECT * FROM Invoice;"
cursor.execute(QUERY)
rows = cursor.fetchall()

# Print Results with pandas
df = pandas.DataFrame(rows)
df.columns = ['InvoiceId', "CustomerId", "InvoiceDate", "Billing Address", "Billing City", "Billing State", "Billing Country", "Billing Postal Code", "Total"]
print(df)

# Close the Database - Note: ALWAYS CLOSE THE DATABASE
connection.close()