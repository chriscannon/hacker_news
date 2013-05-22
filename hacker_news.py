from flask import Flask
from flask import render_template
import MySQLdb
from contextlib import closing
from datetime import datetime
app = Flask(__name__)

class NewsArticle:
    def __init__(self, url, title, age, votes):
        self.url = url
        self.title = title
        self.age = age
        self.votes = votes
        self.score = self.score(self.votes, self.age)

    def __lt__(self, other):
        return self.score < other.score
    
    def score(self, votes, age):
        """
        Calculate the score (a.k.a. rank) for each URL.
        I found this formula in a post from Paul Graham: 
        https://news.ycombinator.com/item?id=231209
        """
        return float(votes - 1)/((age + 2) ** 1.5)

@app.route("/")
def populate_news():
    articles = []
    with closing(MySQLdb.connect(host="localhost", user="root", passwd="",
                                 db="hacker_news")) as connection:
        with closing(connection.cursor()) as cursor:
            cursor.execute("SELECT articles.title, articles.url, " +
                            "articles.submission_date, " +
                            "SUM(votes.vote) AS total_votes " +
                            "FROM articles " +
                            "INNER JOIN votes " +
                            "ON articles.article_id = votes.article_id " +
                            "GROUP BY articles.url")
            for row in cursor.fetchall():
                diff = datetime.now() - row[2]
                age = diff.days * 24 + diff.seconds // 3600
                articles.append(NewsArticle(row[1], row[0], age, row[3]))

    return render_template('index.html', articles=sorted(articles, 
        reverse=True))


if __name__ == "__main__":
    app.run(debug=True)
