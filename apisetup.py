# -*- coding: utf-8 -*-
"""
Twitter API Setup
"""

import tweepy

auth = tweepy.OAuthHandler('','')
auth.set_access_token('','')
api = tweepy.API(auth)

if (not api):
    print('Issues connecting to Twitter API')
