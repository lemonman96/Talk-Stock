import tweepy, io

consumer_key = 'r0swpFT2HEKOzy1jOavTUn5kQ'
consumer_secret = 'JMxEoIuWDwRhuISrFP1O2xNCWbujVtq8xahcGEXpg7Tl7X8NRQ'
access_token = '1264334445227708416-VHyroKpCnaccXGBQNpR2KMvE4qS6to'
access_token_secret = 'Sh2qM0wsI6apnR8d6am6aWtiMXGhqPmyZUBT9UBw9zB8W'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
with open('data.csv', 'w', encoding="utf-8") as file:
    for status in tweepy.Cursor(api.search, q='tesla stock -filter:retweets filter:verified', count=100).items(300):
        if status is not None:
            file.write(status.created_at.strftime("%m/%d/%Y") + ',' + status.user.name + ',' + status.text + '\n')