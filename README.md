Hacker News Re-Creation
========================

* Author: Christopher T. Cannon

Purpose
--------

This is an attempt to re-create a simple version of Hacker News
(https://news.ycombinator.com/). However, the real purpose is to brush up on
MySQL and Python, as well as using Flask and mysql-python for the first time.

Supported Platform
------------------

* Mac OS 10.8.3

Requirements
------------

* MySQL Server (brew install mysql)
* Flask (sudo pip install flask)
* mysql-python (sudo pip install mysql-python)

How to Run
-----------
    mysql.server start
    mysql -uroot < schema.sql
    python hacker_news.py
