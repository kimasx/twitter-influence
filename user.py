"""
Get user timeline data
"""

import datetime

# top_100 = [
        # 'katyperry',
        # 'justinbieber',
        # 'BarackObama',
        # 'rihanna',
        # 'taylorswift13',
        # 'ladygaga',
        # 'TheEllenShow',
        # 'Cristiano',
        # 'jtimberlake',
        # 'KimKardashian',
        # 'ArianaGrande',
        # 'ddlovato',
        # 'selenagomez',
        # 'britneyspears',
        # 'realDonaldTrump',
        # 'shakira',
        # 'jimmyfallon',
        # 'BillGates',
        # 'narendramodi'
        # 'JLo',
        # 'BrunoMars',
        # 'Oprah',
        # 'KingJames',
        # 'neymarjr',
        # 'MileyCyrus',
        # 'NialOfficial',
        # 'Drake',
        # 'iamsrk',
        # 'SrBachchan'
        # 'KevinHart4real',
        # 'BeingSalmanKhan',
        # 'LilTunechi',
        # 'wizkhalifa',
        # 'Louis_Tomlinson',
        # 'Harry_Styles',
        # 'LiamPayne',
        # 'Pink',
        # 'onedirection',
        # 'aliciakeys'
        # 'KAKA',
        # 'chrisbrown',
        # 'EmmaWatson',
        # 'ConanOBrien',
        # 'kanyewest'
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
# ]

from apisetup import api
from pgsetup import cur, conn
query = "INSERT INTO users VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

for user in top_100:
    usr = api.get_user(screen_name=user)
    data = {
        'id': usr.id,
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
        'date_queried': datetime.datetime.today().strftime('%Y-%m-%d')
    }

    # Insert data into Postgres
    cur.execute(query, (data['id'],
                        data['name'],
                        data['handle'],
                        data['location'],
                        data['verified'],
                        data['description'],
                        data['followers_count'],
                        data['following_count'],
                        data['tweets_count'],
                        data['likes_count'],
                        data['listed_count'],
                        data['date_queried']
                        )
    )
    conn.commit()
    print(data)

cur.close()
conn.close()