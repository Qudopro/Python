#tweetutilities.py
import time

from textblob import TextBlob
from geopy import OpenMapQuest
import keys
def print_tweets(tweets):
    """For each Tweepy Status object in tweets, display the user's screen_name and tweet text.
    If the language is not English, translate the text with TextBlob"""
    for tweet in tweets:
        print(f'{tweet.screen_name}:', end=' ')

        if 'en' in tweet.lang:
            print(f'{tweet.text}\n')
        elif 'und' not in tweet.lang:           #Translate to English first
            print(f'\n ORIGINAL: {tweet.text}')
            print(f'TRANSLATED: {TextBlob(tweet.text).translate()}\n')


def get_tweet_content(tweet, location=False):           #tweet is a Status object
    """Return dictionary with data from tweet (a Status object): screen_name, text and location"""
    fields ={}
    fields['screen_name'] = tweet.user.screen_name

    #get the tweet's text
    try:
        fields['text'] = tweet.extended_tweet.full_text
    except:
        fields['text'] = tweet.text

    if location:
        fields['location'] = tweet.user.location

    return fields

def get_geocodes(tweet_list):
    """Get the latitude and longitude of each tweet's location. Returns the number of tweets with invalid loaction data"""
    print('Getting geocodes...')
    geo = OpenMapQuest(api_key=keys.mapquest_key)           #geocoder
    bad_locations = 0

    for tweet in tweet_list:
        processed = False
        delay = .1              #Used if OpenMapQuest tiems out to delay next call
        while not processed:
            try:                    #Get coordinates for tweet['location']
                geo_location = geo.geocode(tweet['location'])
                processed = True
            except:                 #Timed out, so wait before trying again
                print('OpenMapQuest service timed out. Waiting')
                time.sleep(delay)
                delay+=.1
        if geo_location:
            tweet['latitude'] = geo_location.latitude
            tweet['longitude'] = geo_location.longitude
        else:
            bad_locations += 1          #was invalid

    print('Done geocoding')
    return bad_locations