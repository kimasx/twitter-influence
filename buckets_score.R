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


mentions <- dbGetQuery(con, "SELECT buckets.handle, COUNT(buckets_mentions.id), buckets.bucket FROM buckets_mentions
                             RIGHT JOIN buckets ON buckets_mentions.mentioned_user_handle=buckets.handle
                             GROUP BY buckets.handle, buckets.bucket
                             ORDER BY buckets.bucket;")


total_retweets <- dbGetQuery(con, 'SELECT buckets.handle,COALESCE(SUM(retweets_count),0),buckets.bucket FROM buckets_tweets
                                   RIGHT JOIN buckets ON buckets_tweets.handle=buckets.handle
                                   GROUP BY buckets.handle, buckets.bucket
                                   ORDER BY buckets.bucket;')

tweets_count <- dbGetQuery(con, 'SELECT buckets.handle, COALESCE(COUNT(buckets_tweets),0), buckets.bucket FROM buckets_tweets
                                 RIGHT JOIN buckets ON buckets_tweets.handle=buckets.handle
                                 GROUP BY buckets.bucket, buckets.handle;')

user_info <- dbGetQuery(con, 'SELECT handle,followers_count,bucket FROM buckets;')
