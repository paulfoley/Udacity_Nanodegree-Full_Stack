-- Tables for User Database

-- Coders
CREATE TABLE Coders (
	id SERIAL PRIMARY KEY NOT NULL,
	Name Text
);

-- Program Table
Create TABLE Programs (
	id serial PRIMARY KEY,
	name text,
	filename text,
	coder_id int FOREIGN KEY REFERENCES Coders(id)
);

-- Bug Table
Create TABLE Bugs (
	id serial PRIMARY KEY,
	filename text,
	description text,
	program_id int FOREIGN KEY REFERENCES Programs(id)