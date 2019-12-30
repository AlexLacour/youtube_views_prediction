import pickle
import numpy as np


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


features = {'likes': '30', 'dislikes': '15', 'datepublished': '2018-02-17',
            'genre': 'Gaming', 'title': 'AZER', 'views': '42'}

print(process_features(features))
