"""
Collect twitter data from selected usernames and store into Postgres tables
"""

import datetime, yaml
import pandas as pd
from tweepy.cursor import Cursor
from apisetup import api
import psycopg2 as pg2

conf = yaml.load(open('./twitter-influence/credentials.yaml'))
password = conf['user']['password']
user_name = conf['user']['name']
conn = pg2.connect(database='tweets', password=password, user=user_name)
cur = conn.cursor()

startDate = datetime.datetime(2018,9,15,0,0,0)

dframe = pd.read_excel("./twitter-influence/buckets_list.xlsx")
bucketsdf = dframe.loc[dframe['bucket'] == 'media']

query = "INSERT INTO buckets_tweets VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

for sntr in bucketsdf['handle']:
    acct = api.get_user(screen_name = sntr)
    # # item limit is set to 3200 most recent tweets by Twitter
    for twt in Cursor(api.user_timeline, tweet_mode='extended', id=acct.id).items(600):
        print(twt)
        if (twt.created_at > startDate):
            # ignore retweets
            try:
                retweet = twt.retweeted_status.full_text
                print('RETWEET IGNORED: ', retweet)
                print('')
            except AttributeError:
                data = {}
                data['id'] = twt.id_str
                data['date'] = twt.created_at
                data['text'] = twt.full_text
                data['is_quote'] = twt.is_quote_status
                if (data['is_quote']):
                    try:
                        data['quoted_twt_id'] = twt.quoted_status.id_str
                    except AttributeError:
                        data['quoted_twt_id'] = None
                else:
                    data['quoted_twt_id'] = None
                if (twt.in_reply_to_status_id is not None):
                    data['is_reply'] = True
                else:
                    data['is_reply'] = False
                data['in_reply_to_status_id'] = twt.in_reply_to_status_id_str
                data['retweets_count'] = twt.retweet_count
                data['favorites_count'] = twt.favorite_count
                data['handle'] = acct.screen_name
                data['user_id'] = acct.id_str
                data['collected_on'] = datetime.datetime.today().strftime('%Y-%m-%d')
                print(data)
                print(' ')

                # insert data object to Postgres
                try:
                    cur.execute(query, (
                        data['id'],
                        data['date'],
                        data['text'],
                        data['is_quote'],
                        data['is_reply'],
                        data['quoted_twt_id'],
                        data['in_reply_to_status_id'],
                        data['retweets_count'],
                        data['favorites_count'],
                        data['handle'],
                        data['user_id'],
                        data['collected_on']
                    ))
                    conn.commit()
                # error handle for data that already exists in table
                except pg2.IntegrityError:
                    conn.rollback()
                    print('Rollback: Already exists...')

cur.close()
conn.close()