from dataclasses import dataclass
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")
database = client["profile"]
collection = database["aaaaa"]

data = {"i_love_you": True}

collection.insert_one(data)