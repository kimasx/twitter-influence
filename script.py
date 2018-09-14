# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 12:22:46 2018

@author: sunkim
"""

import datetime
from tweepy.cursor import Cursor
from apisetup import api
from pgsetup import conn, cur

#tweets = db.tweets

top_100 = [
        'katyperry',
        'justinbieber',
        'BarackObama',
        'rihanna',
        'taylorswift13',
        'ladygaga',
        'TheEllenShow',
        'Cristiano',
        'jtimberlake',
        'KimKardashian',
        'ArianaGrande',
        'ddlovato',
        'selenagomez',
        'britneyspears',
        'realDonaldTrump',
        'shakira',
        'jimmyfallon',
        'BillGates',
        'narendramodi'
        'JLo',
        'BrunoMars',
        'Oprah',
        'KingJames',
        'neymarjr',
        'MileyCyrus',
        'NialOfficial',
        'Drake',
        'iamsrk',
        'SrBachchan'
        'KevinHart4real',
        'BeingSalmanKhan',
        'LilTunechi',
        'wizkhalifa',
        'Louis_Tomlinson',
        'Harry_Styles',
        'LiamPayne',
        'Pink',
        'onedirection',
        'aliciakeys'
        'KAKA',
        'chrisbrown',
        'EmmaWatson',
        'ConanOBrien',
        'kanyewest'
        # 'Adele',
        # 'akshaykumar',
        # 'zaynmalik',
        # 'ActuallyNPH',
        # 'sachin_rt',
        # 'PMOIndia',
        # 'KendallJenner',
        # 'imVkholi',
        # 'pitbull',
        # 'danieltosh',
        # 'khloekardashian',
        # 'KylieJenner',
        # 'deepikapadukone',
        # 'iHrithik',
        # 'POTUS',
        # 'coldplay',
        # 'aamir_khan',
        # 'kourtneykardash',
        # 'andresiniesta8',
        # 'HillaryClinton',
        # 'MesutOzil1088',
        # 'priyankachopra',
        # 'elonmusk',
        # 'Eminem',
        # 'AvrilLavigne',
        # 'davidguetta',
        # 'MohamadAlarefe',
        # 'blakeshelton',
        # 'ricky_martin',
        # 'MariahCarey',
        # 'arrahman',
        # 'NICKIMINAJ',
        # 'ShawnMendes',
        # 'edsheeran',
        # 'AlejandroSanz',
        # 'Dr_alqarnee',
        # 'LeoDiCaprio',
        # '3gerardpique',
        # 'DalaiLama',
        # 'StephenAtHome',
        # 'shugairi',
        # 'aplusk',
        # 'JimCarrey',
        # '10Ronaldinho',
        # 'aliaa08',
        # 'virendersehwag',
        # 'Pontifex',
        # 'AnushkaSharma',
        # 'jamesdrodriguez',
        # 'agnezmo',
        # 'SnoopDogg',
        # 'KDTrey5',
        # 'GarethBale11',
        # 'ParisHilton',
        # 'FALCAO',
        # 'WayneRooney'
]


startDate = datetime.datetime(2018,9,3,0,0,0)
query = "INSERT INTO tweets VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

for usr_handle in top_100:
    acct = api.get_user(screen_name = usr_handle)
    # # item limit is set to 3200 most recent tweets by Twitter
    for twt in Cursor(api.user_timeline, tweet_mode='extended', id=acct.id).items(500):
        print(twt)
        if (twt.created_at > startDate):
            try:
                retweet = twt.retweeted_status.full_text
                print('RETWEET IGNORED: ', retweet)
                print('')
            except AttributeError:
                data = {}
                data['id'] = twt.id
                data['date'] = twt.created_at
                data['text'] = twt.full_text
                data['is_quote'] = twt.is_quote_status
                if (data['is_quote']):
                    try:
                        data['quoted_twt_id'] = twt.quoted_status.id
                    except AttributeError:
                        data['quoted_twt_id'] = None
                else:
                    data['quoted_twt_id'] = None
                if (twt.in_reply_to_status_id is not None):
                    data['is_reply'] = True
                else:
                    data['is_reply'] = False
                data['in_reply_to_status_id'] = twt.in_reply_to_status_id
                data['retweets_count'] = twt.retweet_count
                data['favorites_count'] = twt.favorite_count
                data['handle'] = acct.screen_name
                data['user_id'] = acct.id
                data['collected_on'] = datetime.datetime.today().strftime('%m-%d-%Y')
                print(data)
                print(' ')
                # INSERT INTO MONGO
                #tweets.insert(data)

                # INSERT INTO POSTGRESQL
                # try:
                #     cur.execute(query, (
                #         data['id'],
                #         data['date'],
                #         data['text'],
                #         data['is_quote'],
                #         data['is_reply'],
                #         data['quoted_twt_id'],
                #         data['in_reply_to_status_id'],
                #         data['retweets_count'],
                #         data['favorites_count'],
                #         data['handle'],
                #         data['user_id'],
                #         data['collected_on']
                #     ))
                #     conn.commit()
                # except:
                #     conn.rollback()
                #     print('Rollback: Already exists...')