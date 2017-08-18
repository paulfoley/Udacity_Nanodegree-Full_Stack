"""
Queries to determine:
1) Most Popular articles
2) Most Popular authors
3) Erros
"""

# Import database
import psycopg2

# Functions
def connect():
    """
    Connect to the PostgreSQL database.
    Returns a database connection and cursor.
    """
    try:
        connection = psycopg2.connect("dbname={}".format('news'))
        cursor = connection.cursor()
        return connection, cursor
    except:
        print("Connection to the Database Failed")


def popular_articles():
    # Returns the top 3 most popular articles
    connection, cursor = connect()

    query = """
            SELECT * 
            FROM log_count
            LIMIT 3;
            """
    cursor.execute(query)
    article_count = cursor.fetchall()
    connection.close()

    return article_count


def popular_authors():
    # Returns a list of the most popular authors
    connection, cursor = connect()

    query = """
            SELECT authors.name as name, author_count.total AS total
            FROM authors, author_count
            WHERE authors.id = author_count.author_id
            ORDER BY total DESC;"""
    cursor.execute(query)
    authors = cursor.fetchall()
    connection.close()

    return authors


def error_days():
    # Reports Days that have more then 1% errors
    connection, cursor = connect()

    query = """
            SELECT log_dates.day AS day,
            CAST(errors.total AS FLOAT) /
            CAST(log_dates.total AS FLOAT) AS percent
            FROM log_dates, errors WHERE log_dates.day = errors.day
            GROUP BY log_dates.day, errors.total, log_dates.total
            HAVING CAST(errors.total AS FLOAT) /
            CAST(log_dates.total AS FLOAT) >= .01
            ORDER BY day ASC;
            """
    
    cursor.execute(query)
    errors = cursor.fetchall()
    connection.close()

    return errors

# Run code and output
print("1. What are the most popular three articles of all time?")
articles = popular_articles()
for article in articles:
    start_index = article[0].find('/', 1)
    article_title_list = article[0][start_index+1:].split('-')
    article_title = ""
    for item in article_title_list:
        article_title += item
        article_title += " "
    print(article_title + " - " + str(article[1]) + " views")

print("2. Who are the most popular authors?")
authors = popular_authors()
for author in authors:
    print(author[0] + " - " + str(author[1]) + " views")

print("3. Which days had more then 1% errors?")
error_days = error_days()
for day in error_days:
    print(str(day[0].date()) + ": " + str(round(day[1]*100, 2)) + "% errors")
