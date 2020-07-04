import tweepy
import pandas as pd
import time
from pprint import pprint

# Developer API keys
consumer_key = 'XXXX'
consumer_key_secret = 'XXXX'
access_token = 'XX-XX'
access_token_secret = 'XXXX'

auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

metoo = pd.read_csv('data/MeTooMMD_train.csv')
tweet_id = list(metoo['TweetId'])
tweet = []
images = []
retweet_count = []
favorite_count = []
date = []
lang =[]
i = 0
for _id in tweet_id:
    i+=1
    try:
        tweetFetched = api.get_status(_id)
        tweet.append(tweetFetched.text)
        images.append(tweetFetched.extended_entities['media'][0]['media_url_https'])
        retweet_count.append(tweetFetched.retweet_count)
        favorite_count.append(tweetFetched.favorite_count)
        date.append(tweetFetched.created_at.strftime("%Y-%m-%d"))
        lang.append(tweetFetched.lang)
        
    except:
        print("Exception: Tweet might be deleted")
        retweet_count.append('')
        favorite_count.append('')
        date.append('')
        lang.append('')
        images.append('')
        tweet.append('')
        continue
metoo['retweet_count'] = retweet_count
metoo['date'] = date
metoo['lang'] = lang
metoo['tweet'] = tweet
metoo['favorite_count'] = favorite_count
metoo['images'] = images

metoo.to_csv('train.csv')
