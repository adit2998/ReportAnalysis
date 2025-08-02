# edgar-fetcher/main.py
import os
from pymongo import MongoClient

mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
client = MongoClient(mongo_uri)
db = client["edgar_db"]
collection = db["sample_collection"]

doc = {"message": "Hello from EDGAR again"}
result = collection.insert_one(doc)

print("Inserted doc with _id:", result.inserted_id)