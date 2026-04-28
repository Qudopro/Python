#tweetlistener
"""Tweepy.StreamListener subclass that processes tweets as they arrive"""
import tweepy
from textblob import TextBlob

class TweetListener(tweepy.StreamListener):
    """Handles incoming Tweet stream"""

    def __init__(self, api, limit=10):          #The api parameter is the Tweepy API object to interact with Twitter, and limit = 10 is the total number of tweets to process
        """Create instance variables for tracking number of tweets"""
        self.tweet_count = 0
        self.TWEET_LIMIT = limit
        super().__init__(api)               #call superclass's init

    def on_connect(self):
        """Called when a connection is established"""
        print("Connection established\n")


    def on_status(self, status):                #status is the Tweepy Status object representing the tweet
        """Called by Tweepy when each tweet arrives"""
        #get the tweet text
        try:
            tweet_text = status.extended_tweet.full_text                #280 characters
        except:
            tweet_text = status.text                                    #140 characters

        print(f'Screen name: {status.user.screen_name}')                #Usert who sent the tweet
        print(f'   Language: {status.lang}')                            #Language of the tweet
        print(f'     Status: {tweet_text}')                             #Tweet

        if status.lang != 'en':
            print(f' Translated: {TextBlob(tweet_text).translate()}')       #Tramsñate the tweet and display it in English

        print()
        self.tweet_count += 1       #Track number of tweets processed

        #if TWEET_LIMIT is reached, return False to terminate streaming
        return self.tweet_count != self.TWEET_LIMIT
