from flask import Flask, request
import requests

app = Flask(__name__)


@app.route('/front')
def getFeatures():
    result = None

    url = {'url': 'https://www.youtube.com/watch?v=Ugs9HASX4rA'}
    requests.post(url='http://192.168.99.100:5000/scrap', data=url)

    # result = await request.get_json()

    return result


if(__name__ == '__main__'):
    app.run(host='0.0.0.0', port=5002, threaded=True)
