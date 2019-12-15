from flask import Flask
import myScraper as scrap

app = Flask(__name__)


@app.route('/')
def Hello():
    return 'Hello World !'


@app.route('/scrap')
def getFeatures():
    return scrap.getFeatures()


"""
export FLASK_APP=app.py
export FLASK_ENV=development
flask run

set FLASK_APP=app.py
set FLASK_ENV=development
flask run
"""
