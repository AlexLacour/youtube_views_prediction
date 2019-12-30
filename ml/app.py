from flask import Flask, request
import ml
from pymongo import MongoClient
import db_functions as dbu

app = Flask(__name__)


@app.route('/ml', methods=['GET', 'POST'])
def getViews():
    features = request.form

    client = MongoClient('mongodb', 27017)

    data = client.yt_db['projet_cs']

    result = str(int(ml.view_prediction(features, data.find({}))))

    dbu.db_insert_new_video(features, data)

    return result


if(__name__ == '__main__'):
    app.run(host='0.0.0.0', port=5001)
