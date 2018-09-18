# -*- coding: utf-8 -*-
"""
PostgreSQL Setup
"""
import yaml
import psycopg2 as pg2

conf = yaml.load(open('./twitter-influence/credentials.yaml'))

password = conf['user']['password']
user_name = conf['user']['name']

conn = pg2.connect(database='tweets', password=password, user=user_name)
cur = conn.cursor()

""" Create table for all tweets from user timeline """
# cur.execute("""
#     CREATE TABLE tweets(
#         id bigint PRIMARY KEY,
#         date date,
#         text text,
#         is_quote boolean,
#         is_reply boolean,
#         quoted_twt_id bigint,
#         in_reply_to_status_id bigint,
#         retweets_count bigint,
#         favorites_count bigint,
#         handle text,
#         user_id bigint,
#         collected_on date
#     )
# """)


""" Create table for top twitter users """
#cur.execute(""" 
#    CREATE TABLE users(
#            id bigint PRIMARY KEY,
#            name text,
#            handle text,
#            location text,
#            verified boolean,
#            description text,
#            followers_count bigint,
#            following_count bigint,
#            tweets_count bigint,
#            likes_count bigint,
#            listed_count bigint,
#            date_queried date
#    )
#""")
#


""" Create table for mentions of a user """
# cur.execute("""
#     CREATE TABLE mentions(
#         id bigint PRIMARY KEY,
#         date date,
#         text text,
#         in_reply_to_status_id bigint,
#         user_id bigint,
#         handle text,
#         mentioned_user_id bigint,
#         mentioned_user_handle text
#     )
# """
# )
# conn.commit()