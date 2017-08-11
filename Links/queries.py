from collections import namedtuple
import sqlite3

db = sqlite3.connect('link.db')

# Queries
def query_database_id():
    ## Get Link Votes For Link with Id 2
    cursor = db.execute('select * from links where id = 2')
    link = Link(*cursor.fetchone())
    
    return link.votes

def query_database_user():
    ## Query Datbase For User
    cursor = db.execute('select * from links where submitter_id = 62443 and votes > 1000')
    link = Link(*cursor.fetchone())
    
    return link.id

def query_database_sumbission_time():
    ## Query Database for Submission Time
    results = []
    cursor = db.execute('select id from links where submitter_id = 62443 order by submitted_time asc')
    results = [link[0] for link in cursor]
    
    return results

def build_link_index():
    ## Add in Link Index
    index = {}
    for link in links:
        index[link.id] = link
    
    return index

link_index = build_link_index()

def link_by_id(link_id):

    return link_index.get(link_id)

def add_new_link(link):
    links.append(link)
    link_index[link.id] = link

new_link = Link(50,1,1,1,'title','url')
add_new_link(new_link)

# Output
print(query_database_id())
print(query_database_user())
print(query_database_sumbission_time())
print(link_by_id(24))
print(links[-1])
print(link_by_id(50))