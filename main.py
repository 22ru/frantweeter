import os
import sys
import time
import tweepy
import random

f = open("apikeys", "r")
consumer_key=f.readline()
consumer_secret=f.readline()
access_token=f.readline()
access_token_secret=f.readline()
f.close()

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

twitterapi = tweepy.API(auth)

#open the file
tweettext = open("tweets.txt")
tweets = tweettext.readlines()
tweettext.close()

while (True):
    try:
        line = int(random.random()* len(tweets))
        tweet = tweets[line]
        print time.strftime("%d %b %Y %I:%M:%S %p ") + tweets[line]
        twitterapi.update_status(status = tweet)
    except:
        print "Unexpected error:", sys.exc_info()[0], sys.exc_info()[1]
        pass
    time.sleep(60* (int(random.random()*500) + 360) )
