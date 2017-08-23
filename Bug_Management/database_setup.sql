-- SQL Commands to setup 'development' database, with 'Coders', 'Programs' and 'Bugs' tables
-- Create Database
DROP DATABASE IF EXISTS development;
CREATE DATABASE development;
\c development

-- Coder Table
CREATE TABLE Coders (
	id serial PRIMARY KEY NOT NULL,
	name text,
	email text
);

-- Program Table
Create TABLE Programs (
	id serial PRIMARY KEY NOT NULL,
	name text,
	coder_id int REFERENCES Coders(id)
);

-- Bug Table
Create TABLE Bugs (
	id serial PRIMARY KEY NOT NULL,
	name text,
	description text,
	program_id int REFERENCES Programs(id),
	coder_id int REFERENCES Coders(id)
);