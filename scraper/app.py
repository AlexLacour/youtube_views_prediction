from flask import Flask, redirect
import myScraper as scrap
import requests

# app = Flask(__name__)


# @app.route('/scrap')
# def getFeatures():
#     
#     # r = requests.post('http://127.0.0.1:5000/ml', dataScraped)
#     return dataScraped


# app.run(port=5000)

app=Flask(__name__)

@app.route('/')
def getFeatures():
    dataScraped = scrap.getFeatures('https://www.youtube.com/watch?v=Ugs9HASX4rA')
    return dataScraped