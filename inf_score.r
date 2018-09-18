library(RPostgres)
library(dplyr)
library(ggplot2)
library(xlsx)



##
# Retrieve Data from Postgres Database w/ RPostgres Package
#

con <- dbConnect(RPostgres::Postgres(),
                 host='localhost',
                 port='5432',
                 dbname='tweets',
                 user='postgres',
                 password=rstudioapi::askForPassword("Enter database password"))

mentions <- dbGetQuery(con, 'SELECT mentioned_user_handle, COUNT(*) 
                       FROM mentions
                       GROUP BY mentioned_user_handle
                       ORDER BY COUNT(*) DESC;')

total_retweets <- dbGetQuery(con, 'SELECT handle, SUM(retweets_count) AS sum
        FROM tweets 
        GROUP BY handle
        ORDER BY sum DESC;')

tweets_count <- dbGetQuery(con, 'SELECT handle, COUNT(*) AS tweets_count
                           FROM tweets
                           GROUP BY handle
                           ORDER BY tweets_count DESC;')

user_info <- dbGetQuery(con, 'SELECT handle, followers_count FROM users')



## 
# Calculate and ranks users by influence score
#

calculate_inf_score <- function(followers, retweets, tweets, mentions) {
  i_r <- (retweets+mentions) / followers
  r_rt <- 2
  score <- (i_r + r_rt) / 2
  return(score)
}

metrics <- inner_join(user_info, mentions, by=c('handle' = 'mentioned_user_handle')) %>% 
  inner_join(x=tweets_count, y=., by=c('handle' = 'handle')) %>%
  inner_join(x=total_retweets,y=., by=c('handle' = 'handle'))
inf_score <- rep(0, length(metrics$handle))
metrics <- cbind(metrics,inf_score)
metrics <- rename(metrics, mentions = count, retweets = sum) 
metrics[c('tweets_count', 'followers_count', 'retweets')] <- sapply(metrics[c('tweets_count', 'followers_count', 'retweets')], as.numeric)

metrics$inf_score <- mapply(calculate_inf_score, metrics$followers_count, metrics$retweets, metrics$tweets_count, metrics$mentions)
metrics$norm_score <- (metrics$inf_score - min(metrics$inf_score) ) / (max(metrics$inf_score) - min(metrics$inf_score))

g <- ggplot(metrics, aes(reorder(handle,norm_score), norm_score)) + geom_bar(stat='identity')+coord_flip()
g + labs(y='Influence Score (0-1)', x='Top 33 Twitter Users Ranked by Influence Score')



## 
# Get number of users gained and find correlation with user influence
#

usersGainedData <- read.xlsx('../OneDrive - Harvard Business School/twitter_user_changes.xlsx',sheetIndex = 1, header = TRUE)
gained <- ggplot(usersGainedData, aes(reorder(handle,metrics$norm_score), percent_change*100)) + geom_bar(stat='identity')+coord_flip()
gained + labs(x='Top 33 Twitter Users Ranked by Influence Score', y='Percent Change in Num. of Followers (%)')


correlationDf <- data.frame(metrics$handle, metrics$norm_score, usersGainedData$percent_change)
newColNames <- c('user','inf_score', 'percent_change_followers')
colnames(correlationDf) <- newColNames

cor.test(x=correlationDf$inf_score, y=correlationDf$percent_change_followers, method = 'spearman')

linCorr <- ggplot(correlationDf, aes(x=inf_score, y=percent_change_followers)) + geom_point(color='#2980B9', size = 2)
linCorr + scale_x_continuous(name='Influence Score') + scale_y_continuous(name='Percent Change in Number of Followers') 