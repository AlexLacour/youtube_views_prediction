from flask import Flask
import requests
import ml
import os
from pymongo import MongoClient

app = Flask(__name__)


@app.route('/')
def getFeatures():
    client = MongoClient('192.168.99.101', 27017)
    features = requests.get(url='http://scraper:5000/').json()

    print('Prediction started')

    result = str(ml.view_prediction(features, client.yt_db['projet_cs']))

    print(result)

    output = 'View prediction = ' + result

    return output


if(__name__ == '__main__'):
    app.run(host='0.0.0.0', port=5001)
