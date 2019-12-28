from flask import Flask
import myScraper as scrap

app = Flask(__name__)


@app.route('/')
def getFeatures():
    dataScraped = scrap.getFeatures(
        'https://www.youtube.com/watch?v=Ugs9HASX4rA')
    return dataScraped


if(__name__ == '__main__'):
    app.run(host='0.0.0.0')
