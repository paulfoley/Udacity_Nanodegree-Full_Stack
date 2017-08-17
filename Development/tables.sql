-- Tables for User Database

-- Coders
CREATE TABLE Coders (
	id serial PRIMARY KEY NOT NULL,
	name text,
	email text

);

-- Program Table
Create TABLE Programs (
	id serial PRIMARY KEY,
	name text,
	coder_id int FOREIGN KEY REFERENCES Coders(id)
);

-- Bug Table
Create TABLE Bugs (
	id serial PRIMARY KEY,
	name text,
	description text,
	program_id int FOREIGN KEY REFERENCES Programs(id)
	coder_id int FOREIGN KEY REFERENCES Coders(id)