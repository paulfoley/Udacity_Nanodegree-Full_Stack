Project returns 1) The most popular articles 2) The most popular authors and 3) Shows days on which there were more then 1% load errors.

To get started, follow these instructions:

A) Create the database with the articles, authors, and log tables:
	- Navigate to the folder with the "newsdata.sql" files
	- Type "psql -d news -f newsdata.sql" into the command line 

B) Create the necessary views for the log_analysis.py script to work:
	- Enter "psql news" in the terminal
	- Then copy and paste the following SQL commands below:

-- SQL Commands
-- Creates a View 'log_count' 
DROP VIEW IF EXISTS log_count;
CREATE VIEW log_count AS SELECT log.path as article_path, count(log.path) as total FROM log, articles WHERE log.path = '/article/' || articles.slug GROUP BY log.path ORDER BY total DESC;

-- Creates a View 'author_count'
DROP VIEW IF EXISTS author_count;
CREATE VIEW author_count AS SELECT articles.author as author_id, sum(log_count.total) as total FROM log_count, articles WHERE log_count.article_path = '/article/' || articles.slug GROUP BY articles.author;

-- Creates a View 'errors'
DROP VIEW IF EXISTS errors;
CREATE VIEW errors AS SELECT date_trunc('day', time) as day, COUNT(status) as total FROM log WHERE status = '404 NOT FOUND' GROUP BY day ORDER BY day ASC;

-- Creates a View 'log_dates'
DROP VIEW IF EXISTS log_dates;
CREATE VIEW log_dates AS SELECT date_trunc('day', time) as day, COUNT(status) as total FROM log GROUP BY day ORDER BY day ASC;

C) Run the script!
	- In the command line enter "python log_analysis.py"