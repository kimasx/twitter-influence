# -*- coding: utf-8 -*-
"""
Twitter API Setup
"""

import yaml, tweepy

# Get credentials data from yaml file
conf = yaml.load(open('./twitter-influence/credentials.yaml'))
cons_key = conf['consumer']['key']
cons_secret = conf['consumer']['secret']
acc_key = conf['access_token']['key']
acc_secret = conf['access_token']['secret']

# Use tweepy to authorize API access
auth = tweepy.OAuthHandler(cons_key, cons_secret)
auth.set_access_token(acc_key, acc_secret)
api = tweepy.API(auth)

if (not api):
    print('Issues connecting to Twitter API')
