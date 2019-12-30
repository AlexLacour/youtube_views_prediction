import numpy as np
from sklearn.linear_model import LinearRegression
import pickle
import random


def create_model():
    model = LinearRegression()

    return model


def get_data(data):
    likes = []
    dislikes = []
    ld_ratios = []
    dates = []
    genres = []
    titles_caps = []
    views = []

    for element in data:
        likes.append(int(element['likes']))
        dislikes.append(int(element['dislikes']))
        ld_ratios.append(float(element['ld_ratio']))
        dates.append(int(element['date'].split('-')[1]))
        genres.append(int(element['genre']))
        titles_caps.append(int(element['is_title_all_caps']))
        views.append(int(element['views']))

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
    with open('genres.pkl', 'rb') as genres_file:
        genres = pickle.load(genres_file)
        genre_to_index = {v: k for k, v in genres.items()}

        features_processed = []
        features_processed.append(int(features['likes']))
        features_processed.append(int(features['dislikes']))
        features_processed.append(
            float(int(features['likes']) / int(features['dislikes'])))
        features_processed.append(int(features['datepublished'].split('-')[1]))
        features_processed.append(
            int(genre_to_index[features['genre'].lower()]))
        features_processed.append(int(features['title'].isupper()))

        features_processed = np.asarray(features_processed, dtype='float32')
        features_processed = np.expand_dims(features_processed, 0)
    return features_processed


def view_prediction(features, data):
    X, y = get_data(data)
    model = train_model(X, y)

    features_processed = process_features(features)

    prediction = np.squeeze(model.predict(features_processed))

    return prediction


def random_ml():
    return random.random()
