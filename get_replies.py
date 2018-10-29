import yaml
import psycopg2 as pg2
from bs4 import BeautifulSoup
from requests import get


"""
Scrape the number of replies of a tweet
"""

# handle twitter API auth
conf = yaml.load(open('./twitter-influence/credentials.yaml'))
password = conf['user']['password']
user_name = conf['user']['name']
conn = pg2.connect(database='tweets', password=password, user=user_name)
cur = conn.cursor()

# get tweets data we collected in Postgres
cur.execute("""
    SELECT handle,id FROM tweets;
""")
tweets = cur.fetchall()

# find only reply count in HTML using BeautifulSoup
for tweet in tweets:
    url = 'https://twitter.com/%s/status/%s' % tweet
    print(url)
    resp = get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    reply_tag = soup.find('button', class_='ProfileTweet-actionButton js-actionButton js-actionReply')

    # set reply count as zero if HTML class has 'isZero'
    if reply_tag.find('span', class_='ProfileTweet-actionCount ProfileTweet-actionCount--isZero ') is not None:
        print('zero replies')
        cur.execute("UPDATE buckets_tweets SET replies_num = %s WHERE id = %s;", (0, tweet[1]))
    # get replies count and push into database
    else:
        reply = soup.find('span', class_='ProfileTweet-actionCount')
        print(reply['data-tweet-stat-count'], 'replies')
        cur.execute("UPDATE tweets SET replies_num = %s WHERE id = %s;", (int(reply['data-tweet-stat-count']), tweet[1]))

    conn.commit()


cur.close()
conn.close()