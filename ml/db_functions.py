import pickle
from datetime import date


def create_features_to_insert(features):
    with open('genres.pkl', 'rb') as genres_file:
        genres = pickle.load(genres_file)
        genre_to_index = {v: k for k, v in genres.items()}

        features_to_insert = {}
        features_to_insert['likes'] = int(features['likes'])
        features_to_insert['dislikes'] = int(features['dislikes'])
        features_to_insert['ld_ratio'] = float(
            int(features['likes']) / (int(features['dislikes']) + 1))
        features_to_insert['date'] = features['datepublished']
        features_to_insert['genre'] = int(
            genre_to_index[features['genre'].lower()])
        features_to_insert['is_title_all_caps'] = int(
            features['title'].isupper())

        features_to_insert['views'] = int(features['views'])

    return features_to_insert


def db_insert_new_video(features, data):
    features_to_insert = create_features_to_insert(features)
    today_date = date.today()
    video_date_published = [int(x)
                            for x in features['datepublished'].split('-')]
    video_date = date(video_date_published[0],
                      video_date_published[1],
                      video_date_published[2])

    age_of_video = int((today_date - video_date).days)

    if(age_of_video > 30):
        data.insert_one(features_to_insert)
