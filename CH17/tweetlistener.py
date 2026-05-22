#tweetlistener
"""Tweepy.StreamListener subclass that processes tweets as they arrive"""
import tweepy
import json
from textblob import TextBlob

class TweetListener(tweepy.StreamListener):
    """Handles incoming Tweet stream"""

    def __init__(self, api, database, limit=10000):
        """Create instance variables for tracking number of tweets"""
        self.db = database
        self.tweet_count = 0
        self.TWEET_LIMIT = limit
        super().__init__(api)               #call superclass's init

    def on_connect(self):
        """Called when a connection is established"""
        print("Connection established\n")

    def on_data(self, data):
        """Called when Twitter pushes a new tweet to you"""
        self.tweet_count += 1               #Track number of tweets processed
        json_data = json.loads(data)        #Convert string to JSON
        self.db.tweets.insert_one(json_data)        #Store in tweets collection     Accesses the DB object db's tweets Collection, creating it if it doesn't exist
        print(f'Screen name: {json_data["user"]["name"]}')                #Usert who sent the tweet
        print(f' Created at: {json_data["created_at"]}')
        print(f'   Received: {self.tweet_count}')                             #Tweet

        #if TWEET_LIMIT is reached, return False to terminate streaming
        return self.tweet_count != self.TWEET_LIMIT

    def on_error(self, status):
        print(status)
        return True
