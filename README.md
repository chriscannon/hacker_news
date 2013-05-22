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

Flask==0.9
Jinja2==2.7
MarkupSafe==0.18
MySQL-python==1.2.4
Werkzeug==0.8.3
wsgiref==0.1.2

How to Run
-----------

    mysql.server start
    mysql -uroot < schema.sql
    pip install -r requirements.txt
    python hacker_news.py
