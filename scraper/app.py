from flask import Flask, redirect
import myScraper as scrap
import requests

app = Flask(__name__)


@app.route('/scrap')
def getFeatures():
    dataScraped = scrap.getFeatures()
    # r = requests.post('http://127.0.0.1:5000/ml', dataScraped)
    return dataScraped


app.run(port=5000)
