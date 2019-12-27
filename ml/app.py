from flask import Flask
import requests
import ml
import os

app = Flask(__name__)


@app.route('/ml')
def getFeatures():
    features = requests.get(url='http://127.0.0.1:5000/scrap').json()
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, '../data.json')

    print('Prediction started')

    result = str(ml.view_prediction(features, json_url))

    print(result)

    output = 'View prediction = ' + result

    return output


app.run()
