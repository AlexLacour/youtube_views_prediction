from flask import Flask, request, redirect
import ml

app = Flask(__name__)


@app.route('/ml', methods=['GET', 'POST'])
def getFeatures():
    return ml.random_ml()


app.run(port=5000, threaded=True)
