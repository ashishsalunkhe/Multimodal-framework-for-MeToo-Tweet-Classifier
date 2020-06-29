import tweepy
import pandas as pd
import time
# Developer API keys
consumer_key = 'FhnADHOEmH6rSIo6EtkX1Qrof'
consumer_key_secret = 'kGDdelgKFASHrdVEzMrLR3oEznNDzExWz8nmFHr6zUosLASI3Q'
access_token = '1206572403309965313-HHdJ0nT4LseoTJP0sWymx4xAELtQ5d'
access_token_secret = 'eiQM3T1ryg7GQof1pJYn5naknB4ETlXWMHwDazaNKRNSZ'

auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

metoo_train = pd.read_csv("data/MeTooMMD_train.csv")
tweet_id = list(metoo_train['TweetId'])
tweets = []
for _id in tweet_id:
    try:
        tweetFetched = api.get_status(_id)
        print("Tweet fetched" + tweetFetched.text)
        tweets.append(tweetFetched.text)
        time.sleep(2)

    except:
        print("Inside the exception - no:2")
        continue
metoo_train['tweet'] = tweets
metoo_train.to_csv("data/train.csv")
