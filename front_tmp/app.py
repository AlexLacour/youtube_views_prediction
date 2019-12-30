from flask import Flask
import requests


app = Flask(__name__)


@app.route('/front', methods=['GET', 'POST'])
def getFeatures():
    url_to_scrap = {'url': 'https://www.youtube.com/watch?v=Ugs9HASX4rA'}
    result = requests.post(
        url='http://192.168.99.100:5000/scrap', data=url_to_scrap).text

    return result


if(__name__ == '__main__'):
    app.run(host='0.0.0.0', port=5002)
