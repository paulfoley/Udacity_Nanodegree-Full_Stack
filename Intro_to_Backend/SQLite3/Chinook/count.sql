# Example of Count Query's
SELECT count(*) FROM table; # Returns the the number of rows in the table
SELECT count(*) FROM animals WHERE species = 'gorilla'; # Returns the number of gorillas
SELECT species, count(*) AS number FROM animals GROUP BY species; # Returns each species name and the number of animals of that species

# Join Count
SELECT products.name, products.sku, count(sales.sku) AS number FROM products LEFT JOIN sales ON products.sku = sales.sku GROUP BY products.sku;
SELECT programs.name, count(bugs.description) AS number FROM programs LEFT JOIN bugs ON programs.filename = bug.filename GROUP BY programs.name ORDER BY number;