from flask import Flask
import requests
import ml
import os
from pymongo import MongoClient

app = Flask(__name__)


@app.route('/')
def getFeatures():
    client = MongoClient('192.168.99.101', 27017)
    try:
        features = requests.get(url='http://192.168.99.101:5000/').json()
    except Exception:
        return 'Scraping Failed'

    print('Prediction started')

    try:
        data = client.yt_db['projet_cs'].find({})
    except Exception:
        return 'DB Failed'

    try:
        result = str(ml.view_prediction(features, data))
    except Exception:
        return 'ML Failed'

    print(result)

    output = 'View prediction = ' + result

    return output


if(__name__ == '__main__'):
    app.run(host='0.0.0.0', port=5001)
