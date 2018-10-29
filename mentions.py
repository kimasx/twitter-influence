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

dframe = pd.read_excel("./twitter-influence/buckets_list.xlsx")
bucketsdf = dframe.loc[dframe['bucket'] == 'athlete']

query = "INSERT INTO buckets_mentions VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

startTime = datetime.datetime(2018,9,15,0,0,0)
#endTime = datetime.datetime(2018,9,3,0,0,0)

for uni in bucketsdf['handle']:
    mentioned_user = api.get_user(screen_name=uni)
    q = '@' + mentioned_user.screen_name
    print(mentioned_user.screen_name)
    for tweet in Cursor(api.search, q=(q+'-filter:retweets'), since=startTime, tweet_mode='extended').items(500):
        data = {
            'id': tweet.id_str,
            'date': tweet.created_at,
            'text': tweet.full_text,
            'in_reply_to_status_id': tweet.in_reply_to_status_id_str,
            'user_id': tweet.user.id_str,
            'handle': tweet.user.screen_name,
            'mentioned_user_id': mentioned_user.id_str,
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
        except pg2.IntegrityError:
            conn.rollback()
            print('Rollback: Already exists...')
cur.close()
conn.close()