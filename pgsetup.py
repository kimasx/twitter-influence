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

# add replies column to existing buckets_tweets table
cur.execute("""
    ALTER TABLE buckets_tweets ADD COLUMN replies_num INT;
""")


""" Create table for all tweets from user timeline """
cur.execute("""
    CREATE TABLE tweets(
        id bigint PRIMARY KEY,
        date date,
        text text,
        is_quote boolean,
        is_reply boolean,
        quoted_twt_id bigint,
        in_reply_to_status_id bigint,
        retweets_count bigint,
        favorites_count bigint,
        handle text,
        user_id bigint,
        collected_on date
    )
""")

""" Create table for top twitter users """
cur.execute(""" 
   CREATE TABLE users(
           id bigint PRIMARY KEY,
           name text,
           handle text,
           location text,
           verified boolean,
           description text,
           followers_count bigint,
           following_count bigint,
           tweets_count bigint,
           likes_count bigint,
           listed_count bigint,
           date_queried date
   )
""")

""" Create table for mentions of a user """
cur.execute("""
    CREATE TABLE mentions(
        id bigint PRIMARY KEY,
        date date,
        text text,
        in_reply_to_status_id bigint,
        user_id bigint,
        handle text,
        mentioned_user_id bigint,
        mentioned_user_handle text
    )
""")

""" Create users table with buckets """
# cur.execute("""
#     CREATE TABLE buckets(
#         id text PRIMARY KEY,
#         name text,
#         handle text,
#         location text,
#         verified boolean,
#         description text,
#         followers_count bigint,
#         following_count bigint,
#         tweets_count bigint,
#         likes_count bigint,
#         listed_count bigint,
#         bucket text,
#         date_queried date
#     )
# """)

""" Create table for tweets by users in bucket """
# cur.execute("""
#     CREATE TABLE buckets_tweets(
#         id text PRIMARY KEY,
#         date date,
#         text text,
#         is_quote boolean,
#         is_reply boolean,
#         quoted_twt_id text,
#         in_reply_to_status_id text,
#         retweets_count bigint,
#         favorites_count bigint,
#         handle text,
#         user_id text,
#         collected_on date
#     )
# """)

""" Create table for mentions of a user in bucket """
# cur.execute("""
#     CREATE TABLE buckets_mentions(
#         id text PRIMARY KEY,
#         date date,
#         text text,
#         in_reply_to_status_id text,
#         user_id text,
#         handle text,
#         mentioned_user_id text,
#         mentioned_user_handle text
#     )
# """)

conn.commit()

cur.close()
conn.close()