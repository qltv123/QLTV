import pymongo

uri = "mongodb://mrd198:12051998d@ds335957.mlab.com:35957/c4e32thuvien"
client = pymongo.MongoClient(uri)
db = client.c4e32thuvien
collection = db.user

def get_all2():
    return list(collection.find())

def insert_data_user(namek,sex,birth,cmt,job,level,wp,phone,ct,city,add,time):
    collection.insert_one({'namek':namek,'sex':sex,'birth': birth,'cmt':cmt,'job':job,'level':level,'wp':wp,'phone':phone, 'ct':ct,'city':city,'add':add,'time':time})