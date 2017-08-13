-- Tables for Chinook Database

-- Invoice Table
CREATE TABLE InvoiceLine (
	InvoiceLineId INTEGER PRIMARY KEY,
	InvoiceId INTEGER,
	TrackId INTEGER,
	UnitPrice REAL,
	Quantity INTEGER,
	FOREIGN KEY (InvoiceId) REFERENCES Invoice (InvoiceId),
	FOREIGN KEY (TrackId) REFERENCES Track (TrackId)
);

-- Album
CREATE TABLE Album (
	AlbumId INTEGER PRIMARY KEY,
	Title TEXT,
	ArtistId INTEGER,
	FOREIGN KEY (ArtistId) REFERENCES Artist (ArtistId)
);

