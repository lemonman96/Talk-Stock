import os, subprocess, csv, json
from talkstock import app
from talkstock.VaderAnalyzer import Analyzer
from flask import render_template

@app.route('/')
def index():
    overall_sentiment = []
    analyzer = Analyzer()
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'csvWriter.py')
    subprocess.run('py ' + filename)
    with open(dirname + '/data.csv', 'r', encoding='utf8') as file:
        reader = csv.reader(file)
        for row in reader:
            json_dict = json.dumps(analyzer.sentiment_scores(sentence=row[2]))
            overall_sentiment.append(json_dict)
    return render_template('index.html', overall_sentiment=json.dumps(overall_sentiment))