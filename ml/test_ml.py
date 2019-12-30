import requests


features = {'likes': 30, 'dislikes': 15, 'datepublished': '2018-02-17',
            'genre': 'Gaming', 'title': 'AZER', 'views': 42}


response = requests.post(url='http://192.168.99.100:5001/ml',
                         data=features)

print(response.text)
