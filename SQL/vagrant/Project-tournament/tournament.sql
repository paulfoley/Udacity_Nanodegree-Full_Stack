## SQL Commands to setup 'tournament' database, with 'Players' and 'Matches' tables, and 'view_wins' and 'view_played' views
-- Create Database
DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;
\c tournament

-- Players Table
CREATE TABLE Players (
	Id SERIAL PRIMARY KEY,
	Name TEXT
	);

-- Matches Table
CREATE TABLE Matches (
	Id SERIAL PRIMARY KEY NOT NULL,
	Winner INTEGER REFERENCES Players(Id),
	Loser INTEGER REFERENCES Players(Id)
	);

-- Create VIEW "view_wins"
CREATE VIEW view_wins AS
SELECT players.id as id, count(matches.id) AS wins
FROM players LEFT OUTER JOIN matches
    ON players.id = matches.winner
GROUP BY players.id;

-- Create VIEW "view_played"
CREATE VIEW view_played AS
SELECT players.id AS id, count(matches.id) AS played
FROM players LEFT OUTER JOIN matches
    ON players.id = matches.winner OR players.id = matches.loser
GROUP BY players.id;