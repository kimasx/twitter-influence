# -*- coding: utf-8 -*-
"""
Twitter API Setup
"""

import tweepy

auth = tweepy.OAuthHandler('x9CyUqYlHRN30PkmLD8OqmXES','xmpm0KEbm5J9Z3Ab9BExN4x5RTV2syNYfoYCNHjisTZ5PQY4pV')
auth.set_access_token('1037370860942909440-C2V5XuoEnWIY4thusoMZexGr5kZ6lH','fZf6kL5do5uILJenpzlmWGGi8iytY8WFYwzxKfGdXIaj4')
api = tweepy.API(auth)

if (not api):
    print('Issues connecting to Twitter API')
