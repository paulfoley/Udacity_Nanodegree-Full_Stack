-- SQL Commands To Create Views
-- Create a View 'log_count' 
DROP VIEW IF EXISTS log_count;
CREATE VIEW log_count AS SELECT log.path as article_path, count(log.path) as total FROM log, articles WHERE log.path = '/article/' || articles.slug GROUP BY log.path ORDER BY total DESC;

-- Create a View 'author_count'
DROP VIEW IF EXISTS author_count;
CREATE VIEW author_count AS SELECT articles.author as author_id, sum(log_count.total) as total FROM log_count, articles WHERE log_count.article_path = '/article/' || articles.slug GROUP BY articles.author;

-- Create a View 'errors'
DROP VIEW IF EXISTS errors;
CREATE VIEW errors AS SELECT date_trunc('day', time) as day, COUNT(status) as total FROM log WHERE status = '404 NOT FOUND' GROUP BY day ORDER BY day ASC;

-- Create a View 'log_dates'
DROP VIEW IF EXISTS log_dates;
CREATE VIEW log_dates AS SELECT date_trunc('day', time) as day, COUNT(status) as total FROM log GROUP BY day ORDER BY day ASC;