from searchtweets import load_credentials,collect_results,gen_rule_payload


premium_search_args = load_credentials('./twitter-influence/twitter_keys.yaml',
                 yaml_key='search_tweets_api',
                 account_type='premium',
                 env_overwrite=False)

rule = gen_rule_payload('@jtimberlake',
                        from_date='2018-06-13',
                        to_date='2018-09-14',
                        results_per_call=100)

tweets = collect_results(rule,max_results=150,
                         result_stream_args=premium_search_args)

for twt in tweets:
    print(twt['created_at'])
    print(twt['text'])
    print(twt['user']['screen_name'])