import nltk
#import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

class Analyzer:

    def __init__(self):
        self.posCount=0
        self.negCount=0
        self.neuCount=0
    

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


    
            