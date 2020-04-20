import os
from dotenv import load_dotenv
from flask import Flask, render_template, request
from flask_pymongo import PyMongo
import numpy as np
import pandas as pd
import math
import pickle
import json

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv('./data/articles_dataset.csv')
df.head()
vectorizer = pickle.load(open("./data/vectorizer.pickle", "rb"))
train = pickle.load(open("./data/train.pickle", "rb"))

load_dotenv()

app = Flask(__name__)

# sets up the database
mongo1 = PyMongo(app, uri = os.getenv("MONGO_URI_1"))
mongo2 = PyMongo(app, uri = os.getenv("MONGO_URI_2"))

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404
    
@app.route('/')
def index():
    query = request.args['query'] if 'query' in request.args else None
    articles = []
    if query is not None:
        query_vec = vectorizer.transform([query])
        results = cosine_similarity(train,query_vec).reshape((-1,))

        for i in results.argsort()[-10:][::-1]:
            article = {}
            if( results[i] > 0.2 ):
                article['id'] = df.iloc[i,0]
                article['title'] = df.iloc[i,1]
                articles.append(article)

    return render_template('search.html', articles = articles)

@app.route('/article/<paper_id>')
def article(paper_id):
    print(paper_id)

    article = mongo1.db.articles.find_one({'paper_id': paper_id},{'_id':0}) 
    if article is None:
        article = mongo2.db.articles.find_one_or_404({'paper_id': paper_id},{'_id':0})

    return render_template('article.html', article = article)

@app.route('/test')
def testdb():
    return  json.dumps({'test': [x for x in mongo2.db.articles.find({'paper_id': 'be5bddac1b08e3f6c757bdbd6564255e6ee96f4a'},{'_id':0})]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
