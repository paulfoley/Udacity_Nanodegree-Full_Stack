-- SQL Commands to setup 'tournament' database, with 'posts' table
-- Create Database
DROP DATABASE IF EXISTS forum;
CREATE DATABASE forum;
\c forum

-- Create posts Table
CREATE TABLE posts (
	id SERIAL PRIMARY KEY NOT NULL,
	content TEXT,
    time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
