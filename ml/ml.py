import json
import numpy as np
from sklearn.linear_model import LinearRegression
import pickle
import random


def create_model(n_features):
    model = LinearRegression()

    return model


def get_data(filepath):
    with open(filepath, 'r') as file:
        data = json.load(file)
    likes = []
    dislikes = []
    ld_ratios = []
    dates = []
    genres = []
    titles_caps = []
    views = []

    for index in data:
        element = data[str(index)]
        likes.append(element['likes'])
        dislikes.append(element['dislikes'])
        ld_ratios.append(element['ld_ratio'])
        dates.append(int(element['date'].split('-')[1]))
        genres.append(element['genre'])
        titles_caps.append(int(element['is_title_all_caps']))
        views.append(element['views'])

    X = list(zip(likes, dislikes, ld_ratios, dates, genres, titles_caps))
    y = views
    return np.asarray(X), np.asarray(y)


def train_model(X, y):
    model = create_model()
    model.fit(X, y)

    filename = 'model.sav'
    with open(filename, 'wb') as file:
        pickle.dump(model, file)
    return model


def process_features(features):
    with open('genres.pkl') as genres_file:
        genres = pickle.load(genres_file)
        genre_to_index = {v: k for k, v in genres.items()}

        features_processed = []
        features_processed.append(features['likes'])
        features_processed.append(features['dislikes'])
        features_processed.append(features['likes'] / features['dislikes'])
        features_processed.append(features['datepublished'].split('-')[1])
        features_processed.append(genre_to_index[features['genre'].lower()])
    return features_processed


def view_prediction(data_filepath, features):
    X, y = get_data(data_filepath)
    model = train_model(X, y)

    features_processed = process_features(features)
    prediction = model.predict(np.asarray(features_processed))

    return prediction


def random_ml():
    return random.random()