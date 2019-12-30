from flask import Flask, request
import myScraper as scrap
import requests

app = Flask(__name__)


@app.route('/scrap', methods=['GET', 'POST'])
def getFeatures():
    dataScraped = scrap.getFeatures(request.form['url'])
    return requests.post(url='http://192.168.99.100:5001/ml', data=dataScraped)


if(__name__ == '__main__'):
    app.run(host='0.0.0.0', port=5000, threaded=True)
