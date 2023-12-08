from pymongo import mongo_client

def get_mongodb():
    client = MongoClient("mongodb://localhost")

    db = client.hw
    return db