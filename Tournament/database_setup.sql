-- SQL Commands to setup 'tournament' database, with 'Players' and 'Matches' tables, and 'view_wins' and 'view_played' views
-- Create Database
DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;
\c tournament

-- Players Table
CREATE TABLE players (
	id SERIAL PRIMARY KEY,
	name TEXT
	);

-- Matches Table
CREATE TABLE matches (
	id SERIAL PRIMARY KEY NOT NULL,
	winner INTEGER REFERENCES players(id),
	loser INTEGER REFERENCES players(id)
	);

-- "view_wins" View
CREATE VIEW view_wins AS
SELECT players.id as id, count(matches.id) AS wins
FROM players LEFT OUTER JOIN matches
    ON players.id = matches.winner
GROUP BY players.id;

-- "view_played" View
CREATE VIEW view_played AS
SELECT players.Id AS id, count(matches.id) AS played
FROM players LEFT OUTER JOIN matches
    ON players.id = matches.winner OR players.id = matches.loser
GROUP BY players.id;