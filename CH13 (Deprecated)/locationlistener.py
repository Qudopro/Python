#locationlistener.py
"""Receives tweets matching a search string and stores a list of dictionaries containing each tweet's screen_name/text/location"""
import tweepy
from tweetutilities import get_tweet_content

class LocationListener(tweepy.StreamListener):
    """Handles incoming Tweet stream to get location data"""
    def __init__(self, api, counts_dict, tweets_list, topic, limit=10):
        """Configure the LocationListener"""
        self.tweets_list = tweets_list              #Store the dictionaries returned by the get_tweet_content
        self.counts_dict = counts_dict              #Keep track of the total number of tweets processed
        self.topic = topic
        self.TWEET_LIMIT = limit
        super().__init__(api)


    def on_status(self, status):
        """Called when Twitter pushes a new tweet to you"""
        #Get each tweet's screen_name, text and location
        tweet_data = get_tweet_content(status, location=True)               #Get info of each tweet

        #Ignore retweets and tweets that don't contain the topic
        if(tweet_data['text'].startswith('RT') or self.topic.lower() not in tweet_data['text'].lower()):
            return

        #Track the number of original tweets we process
        self.counts_dict['total_tweets'] += 1           #Original tweet

        #Ignore tweets with no location
        if not status.user.location:
            return

        #Indicate that we found a tweet with a location
        self.counts_dict['locations'] += 1          #Tweet with location

        self.tweets_list.append(tweet_data)         #Store the tweet
        print(f'{status.user.screen_name}: {tweet_data["text"]}\n')

        #If TWEET_LIMIT is reached, return False to terminate streaming
        return self.counts_dict['location'] != self.TWEET_LIMIT


