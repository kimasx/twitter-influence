library(RPostgres)
library(dplyr)
library(ggplot2)
library(xlsx)


##
# Define variables or functions to bs used
#
buckets <- c('artist','athlete','university','senator')

calculate_ir <- function(followers, retweets, mentions) {
  ir <- (retweets+mentions) / followers
  return(ir)
}

calculate_rmr <- function(retweets, replies, total_tweets) {
  rmr <- (retweets+replies) / total_tweets
  return(rmr)
}

calculate_inf_score <- function(ir, rmr) {
  score <- (ir+rmr)/2
  return(score)
}


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


user_info <- dbGetQuery(con, 'SELECT handle,followers_count FROM buckets;')

tweets_info <- dbGetQuery(con, 'SELECT 
      	                        buckets.handle, 
                                COALESCE(COUNT(buckets_tweets.id),0) AS tweets,
                                SUM(CASE WHEN retweets_count>0 THEN 1 ELSE 0 END) AS retweets,
                                SUM(CASE WHEN has_replies THEN 1 ELSE 0 END) AS replies,
                                buckets.bucket
                                FROM buckets_tweets
                                RIGHT JOIN buckets ON buckets_tweets.handle=buckets.handle
                                GROUP BY buckets.handle,buckets.bucket;')


buckets_metrics <- inner_join(user_info, mentions, by=c('handle' = 'handle')) %>% 
  inner_join(x=total_retweets,y=., by=c('handle' = 'handle'))

buckets_metrics$ir <- mapply(calculate_ir, buckets_metrics$followers_count, buckets_metrics$retweets, buckets_metrics$mentions)
tweets_info$rmr <- mapply(calculate_rmr, tweets_info$retweets, tweets_info$replies, tweets_info$tweets)
tweets_info$rmr <- round(tweets_info$rmr, digits = 4)
tweets_info <- tweets_info[complete.cases(tweets_info),]

ir_scores <- buckets_metrics %>% select(handle,bucket,followers_count,ir)
rmr_scores <- tweets_info %>% select(handle, rmr)
scores <- merge(x=ir_scores, y=rmr_scores, by='handle')

scores$inf_score <- mapply(calculate_inf_score, scores$ir, scores$rmr)
scores$bucket <- as.factor(scores$bucket)

unis <- scores %>% filter(bucket=='university')
artists <- scores %>% filter(bucket=='artist')
athletes <- scores %>% filter(bucket=='athlete')
senators <- scores %>% filter(bucket=='senator')


scores$norm_score <- (scores$inf_score - min(scores$inf_score) ) / (max(scores$inf_score) - min(scores$inf_score))
unis$norm_score <- (unis$inf_score - min(unis$inf_score) ) / (max(unis$inf_score) - min(unis$inf_score))
artists$norm_score <- (artists$inf_score - min(artists$inf_score) ) / (max(artists$inf_score) - min(artists$inf_score))
athletes$norm_score <- (athletes$inf_score - min(athletes$inf_score) ) / (max(athletes$inf_score) - min(athletes$inf_score))
senators$norm_score <- (senators$inf_score - min(senators$inf_score) ) / (max(senators$inf_score) - min(senators$inf_score))


write.xlsx(scores,'C:/Users/sunkim/Development/twitter-influence/bucket_scores.xlsx',sheetName='all_buckets', row.name=F)
write.xlsx(unis,'C:/Users/sunkim/Development/twitter-influence/bucket_scores.xlsx',sheetName='university', append=T, row.name=F)
write.xlsx(artists,'C:/Users/sunkim/Development/twitter-influence/bucket_scores.xlsx',sheetName='artist', append=T, row.name=F)
write.xlsx(athletes,'C:/Users/sunkim/Development/twitter-influence/bucket_scores.xlsx',sheetName='athlete', append=T, row.name=F)
write.xlsx(senators,'C:/Users/sunkim/Development/twitter-influence/bucket_scores.xlsx',sheetName='senator', append=T, row.name=F)
