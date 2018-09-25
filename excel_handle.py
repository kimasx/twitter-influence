import pandas as pd
import datetime, yaml
from apisetup import api
import psycopg2 as pg2


conf = yaml.load(open('./twitter-influence/credentials.yaml'))
password = conf['user']['password']
user_name = conf['user']['name']

conn = pg2.connect(database='tweets', password=password, user=user_name)
cur = conn.cursor()

dframe = pd.read_excel("./twitter-influence/buckets_list.xlsx")
query = "INSERT INTO buckets VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

senators = dframe.loc[dframe['bucket'] == 'senator']
for sntr in senators['handle']:
    usr = api.get_user(screen_name=sntr)
    data = {
            'id': usr.id_str,
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
            'bucket': senators.loc[ senators['handle'] == sntr, 'bucket' ].iloc[0],
            'date_queried': datetime.datetime.today().strftime('%Y-%m-%d')
        }
    print(data)
    # cur.execute(query, (data['id'],
    #                     data['name'],
    #                     data['handle'],
    #                     data['location'],
    #                     data['verified'],
    #                     data['description'],
    #                     data['followers_count'],
    #                     data['following_count'],
    #                     data['tweets_count'],
    #                     data['likes_count'],
    #                     data['listed_count'],
    #                     data['bucket'],
    #                     data['date_queried']
    #                     )
    # )
    # conn.commit()

cur.close()
conn.close()