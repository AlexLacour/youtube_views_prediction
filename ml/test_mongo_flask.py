from pymongo import MongoClient

client = MongoClient('192.168.99.100', 27017)

data = data = client.yt_db['projet_cs'].find({})

count = 0
for element in data:
    count += 1
print(count)
