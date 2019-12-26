from flask import Flask
import ml

app = Flask(__name__)


@app.route('/')
def Hello():
    return 'Hello World !'


@app.route('/ml')
def getFeatures():
    return ml.random_ml()
