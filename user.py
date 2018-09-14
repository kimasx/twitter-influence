# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 15:54:07 2018

@author: sunkim
"""

from tweepy.cursor import Cursor
import datetime

# With MongoDB
users = db.users

loc = None
descript = None
query = "INSERT INTO users VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

for user in top_100:
    usr = api.get_user(screen_name=user)
    data = {
        'id': usr.id,
        'name': usr.name,
        'handle': usr.screen_name,
        'location': usr.location,
        'verified': usr.verified,
        'description': usr.description,   
        'followers_count': usr.followers_count,
        'following_count': usr.friends_count,
        'tweets_count': usr.statuses_count,
        'likes_count': usr.favourites_count,
        'listed_count': usr.listed_count,
        'date_queried': datetime.datetime.today().strftime('%Y-%m-%d')
    }
    users.insert(data)

    # With Postgres
    cur.execute(query, (data['id'], 
                        data['name'],
                        data['handle'],
                        data['location'],
                        data['verified'],
                        data['description'],
                        data['followers_count'],
                        data['following_count'],
                        data['tweets_count'],
                        data['likes_count'],
                        data['listed_count'],
                        data['date_queried']
                        )
    )
    conn.commit()
    print(data)




#for follower in Cursor(api.followers, id=usr.id).items(2):
#    print(follower.id, follower.name)