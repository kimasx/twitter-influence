# -*- coding: utf-8 -*-
"""
Calculate user influence score

"""
""" 

SNP = (Ri + Rrt) / 2

Ri = Number of individual users who retweet content of A or mention user A / total number of followers of A

"""

import top_100
top_users = top_100.top_followers
from pgsetup import cur
from scipy import stats

mentions_q = "SELECT * FROM mentions WHERE mentioned_user_handle = %s;"

for topUsr in top_users:
    print(topUsr, type(topUsr))
    cur.execute(mentions_q, str(topUsr))
    # mentions = cur.fetchall()
    # num_mentions = len(mentions)