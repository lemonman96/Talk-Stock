import tweepy
import csv

consumer_key='#'
consumer_secret='#'
access_key='#'
access_secret='#'

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