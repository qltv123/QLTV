import pymongo
from bson.objectid import ObjectId

uri = "mongodb://mrd198:12051998d@ds335957.mlab.com:35957/c4e32thuvien"
client = pymongo.MongoClient(uri)
db = client.c4e32thuvien
collection = db.sach


def get_all():
    return list(collection.find())

def insert_data_book(names,link,sl,nxb,price):
    collection.insert_one({"names":names,"link":link,"sl":sl,"nxb":nxb,"price":price})

def update_book_by_id(book_id,names,link,nxb,sl,price): 
    collection.update_one({"_id":ObjectId(book_id)},
    {"$set":{"names":names,"link":link,"nxb":nxb,"sl":sl,"price":price}})

def get_book_by_id(book_id): 
    return collection.find_one({"_id":  ObjectId(book_id)})

def delete_data_book(book_id):
    collection.delete_one({"_id":  ObjectId(book_id)})
    

