# -*- coding: utf-8 -*-
import sys
from tweepy import Stream
from tweepy.streaming import StreamListener

user_id = '813286'

class TimelineListener(StreamListener):
    def __init__(self, api):
        self.api = api
        super(tweepy.StreamListener, self).__init__()
        
    def on_status(self, tweet):
        #if (id == tweet.id_str):
#        try:
#            stream_data = {
#                    'id': tweet.id,
#                    'date': tweet.created_at,
#                    'text': tweet.retweeted_status.extended_tweet.full_text,
#                    'handle': tweet.user.screen_name,
#                    'location': tweet.user.location,
#                    'description': tweet.user.description
#            }
#            print(stream_data)
#            print('')
#        except AttributeError:
#            print(tweet.retweeted_status.extended_tweet['full_text'])
        print(tweet)
    def on_error(self, status):
        print(status)
    
    def on_timeout(self):
        sys.stderr.write("Timeout, sleeping for 60 seconds...\n")
        time.sleep(60)
        return
    def on_disconnect(self, notice):
        print ('bye')

listen = Stream(auth, TimelineListener(api), tweet_mode='extended')
listen.filter(follow=[user_id])