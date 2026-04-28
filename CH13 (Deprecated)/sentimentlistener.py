#sentimentlistener.py
"""Script that searches fot weets that match a search string and tallies the number of positive, neutral and negative tweets"""
import keys
import preprocessor as p
import sys
from textblob import TextBlob
import tweepy

class SentimentListener(tweepy.StreamListener):
    """Handles incoming Tweet stream"""
    def __init__(self, api, sentiment_dict, topic, limit=10):
        """Configure the SentimentListener
        api is the API Object that interacts with Twitter
        sentiment_dict is a dictionary in which we'll keep track of the tweet sentiments
        topic is the topic we're searching for
        limit is the maximum number of tweets to process
        """
        self.sentiment_dict = sentiment_dict
        self.tweet_count = 0
        self.topic = topic
        self.TWEET_LIMIT = limit

        #Set tweet-preprocessor to remove URLs/reserved words
        p.set_options(p.OPT.URL, p.OPT.RESERVED)
        super().__init__(api)                       #Call superclas's init

    def on_status(self, status):
        """Called when Twitter pushes a new tweet to you"""
        #Get the tweet's text
        try:
            tweet_text = status.extended_tweet.full_text
        except:
            tweet_text = status.text

        #ignore retweets
        if tweet_text.startswith('RT'):
            return

        tweet_text = p.clean(tweet_text)            #Clean the tween (remove URLs and reserved words)

        #Ignore tweet if the topic is not in the tweet text
        if self.topic.lower() not in tweet_text.lower():
            return

        #update self.sentiment_dict with the polarity
        blob = TextBlob(tweet_text)
        if blob.sentiment.polarity > 0:
            sentiment = '+'
            self.sentiment_dict['positive'] += 1
        elif blob.sentiment.polarity == 0:
            sentiment = ' '
            self.sentiment_dict['neutral'] += 1
        else:
            sentiment = '-'
            self.sentiment_dict['negative'] += 1

        #Display the tweet
        print(f'{sentiment} {status.user.screen_name}: {tweet_text}\n')

        self.tweet_count += 1           #Track number of tweets processed

        #if TWEET_LIMIT is reached, return False to terminate streaming
        return self.tweet_count != self.TWEET_LIMIT

    def main():
        """Configure the OAuthHandler"""
        auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
        auth.set_access_token(keys.access_token, keys.access_token_secret)
        #Get the API Object
        api = tweepy.API(auth, wait_on_rate_limit=True)

        #Create the StreamListener subclass object
        search_key = sys.argv[1]
        limit = int(sys.argv[2])

        sentiment_dict = {'positive': 0, 'neutral': 0, 'negative': 0}
        sentiment_listener = SentimentListener(api, sentiment_dict, search_key, limit)

        #Set up Stream
        stream = tweepy.Stream(auth=api.auth, listener=sentiment_listener)

        #Start filtering English tweets containing search_key
        stream.filter(track=[search_key], languages=['en'], is_async=False)

        print(f'Tweet sentiment for "{search_key}"')
        print('Positive:', sentiment_dict['positive'])
        print('Neutral:', sentiment_dict['neutral'])
        print('Negative:', sentiment_dict['negative'])

    if __name__ == '__main__':
        main()