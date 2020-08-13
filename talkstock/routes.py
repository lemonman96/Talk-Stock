import json
from talkstock import app
from talkstock.VaderAnalyzer import Analyzer
from flask import render_template, request

@app.route('/')
def index():
    
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    stock_name = request.form['stock_name']
    overall_sentiment = []
    analyzer = Analyzer(search=stock_name)
    for tweet in analyzer.tweets:
        overall_sentiment.append(analyzer.sentiment_scores(sentence=tweet['text']))
    return render_template('search.html', overall_sentiment=overall_sentiment, stock_name=stock_name)