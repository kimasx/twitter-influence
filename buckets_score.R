library(RPostgres)
library(dplyr)
library(ggplot2)
library(xlsx)

buckets <- c('artist','athlete','university','senator')


##
# Retrieve data from Postgres
#

con <- dbConnect(RPostgres::Postgres(),
                host='localhost',
                port='5432',
                dbname='tweets',
                user='postgres',
                password=rstudioapi::askForPassword("Enter database password"))


mentions <- dbGetQuery(con, "SELECT buckets.handle, COUNT(buckets_mentions.id) AS mentions,bucket FROM buckets_mentions
                             RIGHT JOIN buckets ON buckets_mentions.mentioned_user_handle=buckets.handle
                             GROUP BY buckets.handle, buckets.bucket
                             ORDER BY buckets.bucket;")


total_retweets <- dbGetQuery(con, 'SELECT buckets.handle,COALESCE(SUM(retweets_count),0) AS retweets FROM buckets_tweets
                                   RIGHT JOIN buckets ON buckets_tweets.handle=buckets.handle
                                   GROUP BY buckets.handle, buckets.bucket
                                   ORDER BY buckets.bucket;')

tweets_count <- dbGetQuery(con, 'SELECT buckets.handle, COALESCE(COUNT(buckets_tweets),0) AS tweets FROM buckets_tweets
                                 RIGHT JOIN buckets ON buckets_tweets.handle=buckets.handle
                                 GROUP BY buckets.bucket, buckets.handle;')

user_info <- dbGetQuery(con, 'SELECT handle,followers_count FROM buckets;')

buckets_metrics <- inner_join(user_info, mentions, by=c('handle' = 'handle')) %>% 
  inner_join(x=tweets_count, y=., by=c('handle' = 'handle')) %>%
  inner_join(x=total_retweets,y=., by=c('handle' = 'handle'))
