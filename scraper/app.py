from flask import Flask, request, redirect
import myScraper as scrap

app = Flask(__name__)


@app.route('/scrap', methods=['GET', 'POST'])
def getFeatures():
    dataScraped = scrap.getFeatures()
    print(dataScraped)
    return dataScraped


app.run(port=5000, threaded=True)
