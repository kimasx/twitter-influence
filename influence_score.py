# -*- coding: utf-8 -*-
"""
Calculate user influence score

"""
""" 

SNP = (Ri + Rrt) / 2

Ri = Number of individual users who retweet content of A or mention user A / total number of followers of A

"""



metrics = {
    'katyperry': {
        'mentions': 0,
        'retweets_count': 0,
        'tweets_count': 0,
        'followers': 0,
        'inf_score': 0
    },
    'justinbieber':  {
        'mentions': 0,
        'retweets_count': 0,
        'tweets_count': 0,
        'followers': 0,
        'inf_score': 0
    },
    'BarackObama':  {
        'mentions': 0,
        'retweets_count': 0,
        'tweets_count': 0,
        'followers': 0,
        'inf_score': 0
    },
    'rihanna':  {
        'mentions': 0,
        'retweets_count': 0,
        'tweets_count': 0,
        'followers': 0,
        'inf_score': 0
    },
    'taylorswift13':  {
        'mentions': 0,
        'retweets_count': 0,
        'tweets_count': 0,
        'followers': 0,
        'inf_score': 0
    },
    'ladygaga':  {
        'mentions': 0,
        'retweets_count': 0,
        'tweets_count': 0,
        'followers': 0,
        'inf_score': 0
    },
    'TheEllenShow': {
        'mentions': 0,
        'retweets_count': 0,
        'tweets_count': 0,
        'followers': 0,
        'inf_score': 0
    },
    'Cristiano':  {
        'mentions': 0,
        'retweets_count': 0,
        'tweets_count': 0,
        'followers': 0,
        'inf_score': 0
    },
    'jtimberlake':  {
        'mentions': 0,
        'retweets_count': 0,
        'tweets_count': 0,
        'followers': 0,
        'inf_score': 0
    },
    'KimKardashian':  {
        'mentions': 0,
        'retweets_count': 0,
        'tweets_count': 0,
        'followers': 0,
        'inf_score': 0
    },
    'ArianaGrande':  {
        'mentions': 0,
        'retweets_count': 0,
        'tweets_count': 0,
        'followers': 0,
        'inf_score': 0
    },
    'ddlovato':  {
        'mentions': 0,
        'retweets_count': 0,
        'tweets_count': 0,
        'followers': 0,
        'inf_score': 0
    },
    'selenagomez':  {
        'mentions': 0,
        'retweets_count': 0,
        'tweets_count': 0,
        'followers': 0,
        'inf_score': 0
    },
    'britneyspears':  {
        'mentions': 0,
        'retweets_count': 0,
        'tweets_count': 0,
        'followers': 0,
        'inf_score': 0
    },
    'realDonaldTrump':  {
        'mentions': 0,
        'retweets_count': 0,
        'tweets_count': 0,
        'followers': 0,
        'inf_score': 0
    },
    'shakira':  {
        'mentions': 0,
        'retweets_count': 0,
        'tweets_count': 0,
        'followers': 0,
        'inf_score': 0
    },
    'jimmyfallon':  {
        'mentions': 0,
        'retweets_count': 0,
        'tweets_count': 0,
        'followers': 0,
        'inf_score': 0
    },
    'BillGates':  {
        'mentions': 0,
        'retweets_count': 0,
        'tweets_count': 0,
        'followers': 0,
        'inf_score': 0
    },
    'narendramodi':  {
        'mentions': 0,
        'retweets_count': 0,
        'tweets_count': 0,
        'followers': 0,
        'inf_score': 0
    },
    'JLo':  {
        'mentions': 0,
        'retweets_count': 0,
        'tweets_count': 0,
        'followers': 0,
        'inf_score': 0
    },
    'BrunoMars':  {
        'mentions': 0,
        'retweets_count': 0,
        'tweets_count': 0,
        'followers': 0,
        'inf_score': 0
    },
    'Oprah':  {
        'mentions': 0,
        'retweets_count': 0,
        'tweets_count': 0,
        'followers': 0,
        'inf_score': 0
    },
    'KingJames':  {
        'mentions': 0,
        'retweets_count': 0,
        'tweets_count': 0,
        'followers': 0,
        'inf_score': 0
    },
    'neymarjr':  {
        'mentions': 0,
        'retweets_count': 0,
        'tweets_count': 0,
        'followers': 0,
        'inf_score': 0
    },
    'MileyCyrus':  {
        'mentions': 0,
        'retweets_count': 0,
        'tweets_count': 0,
        'followers': 0,
        'inf_score': 0
    },
    'NiallOfficial':  {
        'mentions': 0,
        'retweets_count': 0,
        'tweets_count': 0,
        'followers': 0,
        'inf_score': 0
    },
    'Drake':  {
        'mentions': 0,
        'retweets_count': 0,
        'tweets_count': 0,
        'followers': 0,
        'inf_score': 0
    },
    'iamsrk':  {
        'mentions': 0,
        'retweets_count': 0,
        'tweets_count': 0,
        'followers': 0,
        'inf_score': 0
    },
    'SrBachchan':  {
        'mentions': 0,
        'retweets_count': 0,
        'tweets_count': 0,
        'followers': 0,
        'inf_score': 0
    },
    'KevinHart4real':  {
        'mentions': 0,
        'retweets_count': 0,
        'tweets_count': 0,
        'followers': 0,
        'inf_score': 0
    },
    'BeingSalmanKhan':  {
        'mentions': 0,
        'retweets_count': 0,
        'tweets_count': 0,
        'followers': 0,
        'inf_score': 0
    },
    'LilTunechi':  {
        'mentions': 0,
        'retweets_count': 0,
        'tweets_count': 0,
        'followers': 0,
        'inf_score': 0
    },
    'wizkhalifa':  {
        'mentions': 0,
        'retweets_count': 0,
        'tweets_count': 0,
        'followers': 0,
        'inf_score': 0
    },
    'Louis_Tomlinson':  {
        'mentions': 0,
        'retweets_count': 0,
        'tweets_count': 0,
        'followers': 0,
        'inf_score': 0
    },
    'Harry_Styles':  {
        'mentions': 0,
        'retweets_count': 0,
        'tweets_count': 0,
        'followers': 0,
        'inf_score': 0
    },
    'LiamPayne':  {
        'mentions': 0,
        'retweets_count': 0,
        'tweets_count': 0,
        'followers': 0,
        'inf_score': 0
    },
    'Pink':  {
        'mentions': 0,
        'retweets_count': 0,
        'tweets_count': 0,
        'followers': 0,
        'inf_score': 0
    },
    'onedirection':  {
        'mentions': 0,
        'retweets_count': 0,
        'tweets_count': 0,
        'followers': 0,
        'inf_score': 0
    },
    'aliciakeys':  {
        'mentions': 0,
        'retweets_count': 0,
        'tweets_count': 0,
        'followers': 0,
        'inf_score': 0
    },
    'KAKA':  {
        'mentions': 0,
        'retweets_count': 0,
        'tweets_count': 0,
        'followers': 0,
        'inf_score': 0
    },
    'chrisbrown':  {
        'mentions': 0,
        'retweets_count': 0,
        'tweets_count': 0,
        'followers': 0,
        'inf_score': 0
    },
    'EmmaWatson':  {
        'mentions': 0,
        'retweets_count': 0,
        'tweets_count': 0,
        'followers': 0,
        'inf_score': 0
    },
    'ConanOBrien':  {
        'mentions': 0,
        'retweets_count': 0,
        'tweets_count': 0,
        'followers': 0,
        'inf_score': 0
    },
    'kanyewest':  {
        'mentions': 0,
        'retweets_count': 0,
        'tweets_count': 0,
        'followers': 0,
        'inf_score': 0
    }
}


from pgsetup import conn, cur
import pandas as pd
import matplotlib.pyplot as plt

def influence_score(followers, retweets, mentions):
    i_r = (retweets + mentions) / followers
    # for top 40 users, all of their tweets are retweeted and replied to
    r_rt = 2
    score = (i_r + r_rt) / 2
    return score


try:
    cur.execute(""" 
        SELECT mentioned_user_handle, COUNT(*) 
        FROM mentions
        GROUP BY mentioned_user_handle
        ORDER BY COUNT(*) DESC;
    """)
    mentions = cur.fetchall()

    cur.execute("""
        SELECT handle, SUM(retweets_count) AS sum
        FROM tweets 
        GROUP BY handle
        ORDER BY sum DESC;
    """)
    retweets_count = cur.fetchall()

    cur.execute("""
        SELECT handle, COUNT(*) AS tweets_count
        FROM tweets
        GROUP BY handle
        ORDER BY tweets_count DESC;
    """)
    tweets_count = cur.fetchall()

    cur.execute("SELECT handle, followers_count  FROM users")
    user_info = cur.fetchall()
except:
    conn.rollback()
    print('Rollback...')

# update mentions
for topUsr in mentions:
    if (topUsr[0] in metrics):
        metrics[topUsr[0]].update({ 'mentions': topUsr[1] })
for topUsr in retweets_count:
    if (topUsr[0] in metrics):
        metrics[topUsr[0]].update({ 'retweets_count': int(str(topUsr[1])) })
for topUsr in user_info:
    if (topUsr[0] in metrics):
        metrics[topUsr[0]].update({ 'followers': topUsr[1] })
for topUsr in tweets_count:
    if (topUsr[0] in metrics):
        metrics[topUsr[0]].update({ 'tweets_count': topUsr[1] })

for celeb in metrics:
    print(celeb)
    score = influence_score(metrics[celeb]['followers'], metrics[celeb]['retweets_count'], metrics[celeb]['mentions'])
    metrics[celeb].update({ 'inf_score': score })

df = pd.DataFrame.from_dict(metrics, orient='index')
df['normalized_scores'] = (df.inf_score - df.inf_score.min()) / (df.inf_score.max() - df.inf_score.min())
df = df.sort_values('normalized_scores', ascending=False)


fig, ax = plt.subplots()
ax.barh(df.index, df.normalized_scores)
ax.set_yticklabels(df.index)
ax.invert_yaxis()
plt.xlabel('Top Users on Twitter')
plt.ylabel('Influence Score (0-1)')
plt.title('Influence Score for Top Most Followed Twitter Accounts')
plt.show()