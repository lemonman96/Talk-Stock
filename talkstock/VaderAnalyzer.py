import nltk, tweepy
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

class Analyzer:

    def __init__(self, search):
        #init member vars
        self.posCount=0
        self.negCount=0
        self.neuCount=0
        self.tweets=[]
    
        #declare api keys
        consumer_key='#'
        consumer_secret='#'
        access_key='#'
        access_secret='#'

        #authorize twitter, initialize tweepy
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_key, access_secret)
        api = tweepy.API(auth)

        #search twitter for relevant tweets
        for status in tweepy.Cursor(api.search, q=search + ' stock -filter:retweets filter:verified', count=100, tweet_mode='extended', lang='en').items(300):
            if status is not None:
                tweets_encoded = status.full_text.encode('utf-8')
                tweets_decoded = tweets_encoded.decode('utf-8')
                tweet_dict = {
                    'created_at': status.created_at.strftime("%m/%d/%Y"),
                    'user': status.user.name,
                    'text': tweets_decoded
                }
                self.tweets.append(tweet_dict)

        

    # function to return sentiment dict
    # of the sentence. 
    def sentiment_scores(self, sentence): 
    
        # Create a SentimentIntensityAnalyzer object. 
        sid_obj = SentimentIntensityAnalyzer() 
    
        # polarity_scores method of SentimentIntensityAnalyzer 
        # oject gives a sentiment dictionary. 
        # which contains pos, neg, neu, and compound scores. 
        sentiment_dict = sid_obj.polarity_scores(sentence) 

        #add to counts
        if sentiment_dict['compound'] >= 0.05:
            self.posCount=self.posCount+1
        elif sentiment_dict['compound'] <= - 0.05: 
            self.negCount=self.negCount+1
        else: 
            self.neuCount=self.neuCount+1
        return sentiment_dict


    
            