import tweepy
import csv

consumer_key='r0swpFT2HEKOzy1jOavTUn5kQ'
consumer_secret='JMxEoIuWDwRhuISrFP1O2xNCWbujVtq8xahcGEXpg7Tl7X8NRQ'
access_key='1264334445227708416-gf2xhkNipHaBqjidVrejFX8IuPbr7i'
access_secret='lWOjkirjuqgaNqoI9Sy8HV916q7znDn3r2hTHjG5zxbol'

#authorize twitter, initialize tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

with open('talkstock/data.csv', 'w', encoding="utf-8", newline='') as file:
    for status in tweepy.Cursor(api.search, q='tesla stock -filter:retweets filter:verified', count=100, tweet_mode='extended', lang = 'en').items(300):
        if status is not None:

            csvWriter = csv.writer(file)

            tweets_encoded = status.full_text.encode('utf-8')
            tweets_decoded = tweets_encoded.decode('utf-8')
            csvWriter.writerow([status.created_at.strftime("%m/%d/%Y"), status.user.name, tweets_decoded])