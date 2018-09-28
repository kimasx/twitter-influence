import yaml
import psycopg2 as pg2
from bs4 import BeautifulSoup
from requests import get


conf = yaml.load(open('./twitter-influence/credentials.yaml'))
password = conf['user']['password']
user_name = conf['user']['name']

conn = pg2.connect(database='tweets', password=password, user=user_name)
cur = conn.cursor()


cur.execute("""
    SELECT buckets_tweets.handle,buckets_tweets.id FROM buckets_tweets
    JOIN buckets ON buckets_tweets.handle = buckets.handle
    WHERE buckets.bucket='';
""")
tweets = cur.fetchall()


for tweet in tweets:
    url = 'https://twitter.com/%s/status/%s' % tweet
    print(url)
    resp = get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    reply_tag = soup.find('button', class_='ProfileTweet-actionButton js-actionButton js-actionReply')
    if reply_tag.find('span', class_='ProfileTweet-actionCount ProfileTweet-actionCount--isZero ') is not None:
        print('zero replies')
        cur.execute("UPDATE buckets_tweets SET replies_num = %s WHERE id = %s;", (0, tweet[1]))
    else:
        reply = soup.find('span', class_='ProfileTweet-actionCount')
        print(reply['data-tweet-stat-count'], 'replies')
        cur.execute("UPDATE buckets_tweets SET replies_num = %s WHERE id = %s;", (int(reply['data-tweet-stat-count']), tweet[1]))
    conn.commit()


cur.close()
conn.close()