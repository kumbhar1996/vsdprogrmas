import pymongo 

url='mongodb://localhost:27017'
mongoclient=pymongo.MongoClient(url)
db=mongoclient['mydb']
collection=db['student']

document=collection.find()

for doc in document:
    print(doc)