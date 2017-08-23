'''Implementation of a Swiss-system tournament'''

# Imports
import psycopg2

def connect():
    """ 
    Connect to the PostgreSQL database.
    Returns a database connection and cursor.
    """
    try:
        connection = psycopg2.connect("dbname={}".format('tournament'))
        cursor = connection.cursor()
        return connection, cursor
    except:
        print("Connection to the Database Failed")

def deleteMatches():
    """Remove all the match records from the database."""
    connection, cursor = connect()

    query = "DELETE FROM matches;"
    cursor.execute(query)
    connection.commit()
    connection.close()

def deletePlayers():
    """Remove all the player records from the database."""
    connection, cursor = connect()

    query = "DELETE FROM players;"
    cursor.execute(query)
    connection.commit()
    connection.close()

def countPlayers():
    """Returns the number of players currently registered."""
    connection, cursor = connect()

    query = "SELECT count(id) as num FROM players;"
    cursor.execute(query)
    results = cursor.fetchone()
    results = int(results[0])
    connection.close()
    return results

def registerPlayer(name):
    """
    Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    connection, cursor = connect()

    query = "INSERT INTO players (name) VALUES (%s);"
    cursor.execute(query, (name,))
    connection.commit()
    connection.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    connection, cursor = connect()

    query_matches = """
                    SELECT players.id AS id, players.name AS name, view_wins.wins AS wins, view_played.played AS matches 
                    FROM players, view_wins, view_played 
                    WHERE players.Id = view_wins.id AND players.Id = view_played.id 
                    ORDER BY wins DESC;
                    """
    cursor.execute(query_matches)
    standings = cursor.fetchall()

    connection.close()
    
    return standings


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    connection, cursor = connect()
    
    query = "INSERT INTO matches (winner, loser) VALUES (%s, %s);"
    cursor.execute(query, (winner,loser,))
    connection.commit()
    connection.close() 
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    connection, cursor = connect()

    standings = playerStandings()

    match = []
    matches =[]

    for player in standings:
        match.append(player[0])
        match.append(player[1])
        if len(match) >= 4:
            matches.append(match)
            match = []

    connection.close()

    return matches
