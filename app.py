import os
from dotenv import load_dotenv
from flask import Flask, render_template
from flask_pymongo import PyMongo
import numpy as np
import pandas as pd
import math
import pickle
import json

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv('data/articles_dataset.csv')
df.head()
vectorizer = pickle.load(open("data/vectorizer.pickle", "rb"))
train = pickle.load(open("data/train.pickle", "rb"))

load_dotenv()

app = Flask(__name__)

## sets up the database
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test')
def testdb():
    return  json.dumps({'test': [x for x in mongo.db.test.find({},{'_id':0})]})

@app.route('/search', methods=['GET'])
def search():
    query = 'coronavirus'
    show_results = []
    query_vec = vectorizer.transform([query])
    results = cosine_similarity(train,query_vec).reshape((-1,))

    for i in results.argsort()[-10:][::-1]:
        article = {}
        if( results[i] > 0.2 ):
            article['id'] = df.iloc[i,0]
            article['title'] = df.iloc[i,1]
            show_results.append(article)
    
    return json.dumps({'results': show_results})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)