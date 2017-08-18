from collections import namedtuple
import sqlite3

# Connect to Database
connection = sqlite3.connect('link.db')

# Create Cursor
cursor = connection.cursor()

# Make a Link class
Link = namedtuple('Link', ['id', 'submitter_id', 'submitted_time', 'votes', 'title', 'url'])

# Queries
def query_database_id():
    ## Get Link Votes For Link with Id 2
    query = """
            SELECT *
            FROM links
            WHERE id = 2;
            """
    cursor.execute(query)
    link = Link(*cursor.fetchone())
    
    return link.votes

def query_database_user():
    ## Query Datbase For User
    query = """
            SELECT *
            FROM links
            WHERE submitter_id = 62443 AND votes > 1000;
            """
    cursor.execute(query)
    link = Link(*cursor.fetchone())
    
    return link.id

def query_database_sumbission_time():
    ## Query Database for Submission Time
    results = []
    cursor.execute('select id from links where submitter_id = 62443 order by submitted_time asc')
    results = [link[0] for link in cursor]
    
    return results

# Output
print(query_database_id())
print(query_database_user())
print(query_database_sumbission_time())
