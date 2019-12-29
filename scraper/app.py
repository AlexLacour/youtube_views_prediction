from flask import Flask, request
import myScraper as scrap
import requests

app = Flask(__name__)


@app.route('/scrap')
def getFeatures():
    if(request.method == 'POST'):
        dataScraped = scrap.getFeatures(request.args['url'])
        requests.post(url='http://192.168.99.100:5001/ml', data=dataScraped)
    return 'Scraping'


if(__name__ == '__main__'):
    app.run(host='0.0.0.0', port=5000, threaded=True)
