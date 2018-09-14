# -*- coding: utf-8 -*-
"""
Top 100 Most Followed Individuals and Artists on Twitter (excludes brands, companies, etc.)

Source:
    
"""

top_followers = [
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
    'narendramodi',
    'JLo',
    'BrunoMars',
    'Oprah',
    'KingJames',
    'neymarjr',
    'MileyCyrus',
    'NiallOfficial',
    'Drake',
    'iamsrk',
    'SrBachchan',
    'KevinHart4real',
    'BeingSalmanKhan',
    'LilTunechi',
    'wizkhalifa',
    'Louis_Tomlinson',
    'Harry_Styles',
    'LiamPayne',
    'Pink',
    'onedirection',
    'aliciakeys',
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
