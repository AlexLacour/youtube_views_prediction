from flask import Flask
import requests
import ml
import os

app = Flask(__name__)


@app.route('/')
def getFeatures():
    features = requests.get(url='http://scraper:5000/').json()
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__)) #hea
    json_url = os.path.join(SITE_ROOT, 'data.json') #HEA too

    print('Prediction started')

    result = str(ml.view_prediction(features, json_url))

    print(result)

    output = 'View prediction = ' + result

    return output


if(__name__ == '__main__'):
    app.run(host='0.0.0.0', port=5001)
