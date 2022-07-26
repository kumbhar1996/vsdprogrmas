import pymongo 

url='mongodb://localhost:27017'

mongoclient=pymongo.MongoClient(url)
db=mongoclient['group']
collection=db['student']

document={'name':'akshay','loc':'solapur','rno':56,'marks':89}

result=collection.insert_one(document)
print(result.inserted_id)
