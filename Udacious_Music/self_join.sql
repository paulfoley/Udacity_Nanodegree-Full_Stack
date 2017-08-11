# Query to Self JOIN a table
SELECT a.id, b.id FROM table as a, table as b WHERE a.column1 = b.column1 AND a.column2 = b.column2 ORDER BY a.column1, a.column2;