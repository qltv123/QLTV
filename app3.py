import pymongo

uri = "mongodb://mrd198:12051998d@ds335957.mlab.com:35957/c4e32thuvien"
client = pymongo.MongoClient(uri)
db = client.c4e32thuvien
collection = db.user

def get_all2():
    return list(collection.find())

def insert_data_user(ma,name,phone,sex,add):
    collection.insert_one({'ma':ma,'name':name,'phone':phone, 'sex':sex, 'add':add})