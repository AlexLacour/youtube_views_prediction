from flask import Flask
import requests
import ml
import os

app = Flask(__name__)

route('/ml')
def getFeatures():
    features = requests.get(url='http://127.0.0.1:5000/scrap').json()
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, '../data.json')

    print('Prediction started')

    result = str(ml.view_prediction(features, json_url))

    print(result)

    output = 'View prediction = ' + result

    return output


app.run(port = 5001)


socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('', 5333))

while True:
        socket.listen(5)
        client, address = socket.accept()
        print "{} connected".format( address )

        response = client.recv(255)
        if response != "":
                print response

print "Scrapper closed"
client.close()
stock.close()

# @app.route('/ml')
# def getFeatures():
#     features = requests.get(url='http://127.0.0.1:5000/scrap').json()
#     SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
#     json_url = os.path.join(SITE_ROOT, '../data.json')

#     print('Prediction started')

#     result = str(ml.view_prediction(features, json_url))

#     print(result)

#     output = 'View prediction = ' + result

#     return output


# app.run(port = 5001)
