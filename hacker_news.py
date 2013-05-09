from flask import Flask
import MySQLdb
from contextlib import closing

app = Flask(__name__)

@app.route("/")
def populate_news():
    articles = []
    with closing(MySQLdb.connect(host="localhost", user="root", passwd="", db="hacker_news")) as connection:
        with closing(connection.cursor()) as cursor:
            cursor.execute("SELECT * FROM articles")
            for row in cursor.fetchall():
                articles.append(row[2])

    return '<br/>'.join(articles)


def score(points, age):
    """
    Calculate the score (a.k.a. rank) for each URL.
    I found this formula in a post from Paul Graham: https://news.ycombinator.com/item?id=231209
    """
    return (points - 1)/(age + 2) ** 1.5


if __name__ == "__main__":
    app.run(debug=True)