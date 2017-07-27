# sqlite3 SELECT with COUNT DISTINCT and JOIN

# Import Database
import sqlite3

# Connect to Database
connection = sqlite3.connect("chinook.db")

# Create Cursor
cursor = connection.cursor()

# Query
QUERY = "SELECT count(DISTINCT Customer.FirstName) AS Num FROM Customer JOIN Invoice ON Customer.CustomerId = Invoice.CustomerId JOIN InvoiceLine ON Invoice.InvoiceId = InvoiceLine.InvoiceId JOIN Track ON InvoiceLine.TrackId = Track.TrackId JOIN Genre ON Track.GenreId = Genre.GenreId WHERE Genre.Name = 'Jazz';"
cursor.execute(QUERY)
results = cursor.fetchall()

# Print Results
print(results[0][0])

# Close the Connection - Note: ALWAYS CLOSE THE CONNECTION
connection.close()