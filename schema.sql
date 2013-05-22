DROP DATABASE IF EXISTS hacker_news;
CREATE DATABASE hacker_news;
USE hacker_news;
CREATE TABLE IF NOT EXISTS articles (
    article_id INTEGER NOT NULL AUTO_INCREMENT,
    submission_date DATETIME DEFAULT NULL,
    title TEXT DEFAULT NULL,
    url TEXT DEFAULT NULL,
    PRIMARY KEY (article_id)
);
CREATE TABLE IF NOT EXISTS votes (
    vote_id INTEGER NOT NULL AUTO_INCREMENT,
    article_id INTEGER DEFAULT NULL,
    vote SMALLINT DEFAULT NULL,
    PRIMARY KEY (vote_id)
);
INSERT INTO articles (submission_date, title, url) VALUES
    ('2013-05-22 12:01:00', 'Reddit', 'http://www.reddit.com/'),
    ('2013-05-22 09:35:01', 'Digg', 'http://digg.com/'),
    ('2013-05-22 10:34:41', 'CNN', 'http://www.cnn.com/');
INSERT INTO votes (article_id, vote) VALUES
    (1, 1), (2, 1), (3, 1), (3, 1), (1, 1), (1, 1), (2, -1);
