# Create a table examples
Create TABLE programs (
	id serial primary key,
	name text,
	filename text
);

Create TABLE bugs (
	id serial primary key,
	filename text,
	description text,
);

Create TABLE animals (
	id serial primary key,
	name text,
	species text
)

CREATE TABLE InvoiceLine (
	InvoiceLineId INTEGER PRIMARY KEY,
	InvoiceId INTEGER,
	TrackId INTEGER,
	UnitPrice REAL,
	Quantity INTEGER,
	FOREIGN KEY (InvoiceId) REFERENCES Invoice (InvoiceId),
	FOREIGN KEY (TrackId) REFERENCES Track (TrackId)
	);

CREATE TABLE Album (
	AlbumId INTEGER PRIMARY KEY,
	Title TEXT,
	ArtistId INTEGER,
	FOREIGN KEY (ArtistId) REFERENCES Artist (ArtistId)
	);

CREATE TABLE Coders (
	CoderId SERIAL PRIMARY KEY NOT NULL,
	Name Text
	);