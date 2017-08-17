# Example of SQL using SQLite3

# Import Database
import sqlite3
import pandas

# Connect to Database
connection = sqlite3.connect("chinook.db")

# Create Cursor
cursor = connection.cursor()

# Queries
QUERY1 = """
	SELECT count(DISTINCT Customer.FirstName) AS Num
	FROM Customer
	JOIN Invoice ON Customer.CustomerId = Invoice.CustomerId
	JOIN InvoiceLine ON Invoice.InvoiceId = InvoiceLine.InvoiceId
	JOIN Track ON InvoiceLine.TrackId = Track.TrackId 
	JOIN Genre ON Track.GenreId = Genre.GenreId
	WHERE Genre.Name = 'Jazz';
"""
cursor.execute(QUERY1)
results1 = cursor.fetchall()
print(results1[0][0])


QUERY2 = """
	SELECT Track.GenreId, count(MediaType.MediaTypeId) AS Num
	FROM Track
	JOIN MediaType ON Track.MediaTypeId = MediaType.MediaTypeId
	WHERE Track.GenreId = 9 AND MediaType.MediaTypeID = 1;
"""
cursor.execute(QUERY2)
results2 = cursor.fetchall()
print(results2[0])

QUERY3 = """
	SELECT Genre.Name, count(Genre.Name) AS Total
	FROM Track
	JOIN Genre ON Track.GenreId = Genre.GenreId,
	(SELECT avg(Milliseconds) AS av FROM Track) as AVG_Track
	WHERE Milliseconds < av GROUP BY Genre.Name ORDER BY Total DESC;
"""
cursor.execute(QUERY3)
results3 = cursor.fetchall()
print(results3)

QUERY4 = """
	SELECT Track.Name, Genre.Name
	FROM Track
	JOIN Genre ON Track.GenreId = Genre.GenreId;
"""
cursor.execute(QUERY4)
results4 = cursor.fetchall()
print(results4)

QUERY5 = """
	SELECT * 
	FROM Invoice;
"""
cursor.execute(QUERY5)
rows = cursor.fetchall()
df = pandas.DataFrame(rows)
df.columns = ['InvoiceId', "CustomerId", "InvoiceDate", "Billing Address", "Billing City", "Billing State", "Billing Country", "Billing Postal Code", "Total"]
print(df)

QUERY6 = """
	SELECT Total
	FROM Invoice,
	(SELECT avg(Total) AS av FROM Invoice) AS avg_invoice
	WHERE Total > av ORDER BY Total ASC;
"""
cursor.execute(QUERY6)
results6 = cursor.fetchall()
print(results6)

QUERY7 = """
	SELECT avg(Max)
	FROM (SELECT max(Total) as Max
	FROM Invoice
	GROUP BY BillingCountry) AS maxes;
"""
cursor.execute(QUERY7)
results7 = cursor.fetchall()
print(results7[0][0])

QUERY8 = """
	SELECT Customer.FirstName
	FROM Customer
	LIMIT 10;
"""
cursor.execute(QUERY8)
results8 = cursor.fetchall()
print (results8)

QUERY9 = """
	SELECT Album.Title
	FROM Album
	LIMIT 10;
"""
cursor.execute(QUERY9)
results9 = cursor.fetchall()
print(results9)

# Close the Connection
connection.close()