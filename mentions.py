# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 12:31:40 2018

@author: sunkim
"""
from apisetup import api
from pgsetup import conn, cur
from tweepy.cursor import Cursor
import datetime

top_100 = [
    # 'MileyCyrus',
    # 'NialOfficial',
    # 'Drake',
    # 'iamsrk',
    # 'SrBachchan',
    # 'KevinHart4real',
    # 'BeingSalmanKhan',
    # 'LilTunechi',
    # 'wizkhalifa',
    # 'Louis_Tomlinson',
    # 'Harry_Styles',
    # 'LiamPayne',
    # 'Pink',
    # 'onedirection',
    # 'aliciakeys',
    # 'KAKA',
    # 'chrisbrown',
    # 'EmmaWatson',
    # 'ConanOBrien',
    # 'kanyewest'
]

query = "INSERT INTO mentions VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

startTime = datetime.datetime(2018,9,3,0,0,0)
#endTime = datetime.datetime(2018,9,3,0,0,0)

for usr in top_100:
    mentioned_user = api.get_user(screen_name=usr)
    q = '@' + mentioned_user.screen_name
    print(mentioned_user.screen_name)
    for tweet in Cursor(api.search, q=(q+'-filter:retweets'), since=startTime, tweet_mode='extended').items(500):
        data = {
            'id': tweet.id,
            'date': tweet.created_at,
            'text': tweet.full_text,
            'in_reply_to_status_id': tweet.in_reply_to_status_id,
            'user_id': tweet.user.id,
            'handle': tweet.user.screen_name,
            'mentioned_user_id': mentioned_user.id,
            'mentioned_user_handle': mentioned_user.screen_name
        }
        print(data)
        try:
            cur.execute(query, (
                data['id'],
                data['date'],
                data['text'],
                data['in_reply_to_status_id'],
                data['user_id'],
                data['handle'],
                data['mentioned_user_id'],
                data['mentioned_user_handle']
            ))
            conn.commit()
        except:
            conn.rollback()
            print('Rollback: Already exists...')