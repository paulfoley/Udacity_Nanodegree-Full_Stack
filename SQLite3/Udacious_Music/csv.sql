# Examples of using sqlite3 commands to create a Table from a CSV

# Export a CSV
sqlite> .mode csv
sqlite> .output newFile.csv
sqlite> SELECT * FROM myTable;
sqlite> .exit

# Import a CSV
$ sqlite3 new.db # <--- If you'd like your csv's in a new database remember to make it first.
sqlite> CREATE TABLE myTable() # <--- Build your schema!
sqlite> .mode csv
sqlite> .import newFile.csv myTable