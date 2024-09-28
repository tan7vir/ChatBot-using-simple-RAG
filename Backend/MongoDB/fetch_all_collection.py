from pymongo import MongoClient
from flask import jsonify

# MongoDB connection URL
url = "mongodb://localhost:27017"
client = MongoClient(url)

# Database Name
db_name = "AllChat"

def fetch_chat_list(collection_name):
    db = client[db_name]
    collection = db[collection_name]
    # Fetch all documents in the collection
    return list(collection.find({}))  # Return as a list of dictionaries

def fetch_all_collection():
    try:
        
        db = client[db_name]

        # Get the collection names
        collection_names = db.list_collection_names()
        

        # Convert to a list of strings
        # collections_array = list(collection_names)

        # # Create an object to store chat lists
        # chat_lists = {}

        # for collection in collections_array:
        #     chat_lists[collection] = fetch_chat_list(collection)
        return collection_names
        

    except Exception as error:
        print("Error fetching collections:", error)
        return {"error": "An error occurred fetching collections"}
    

# fetch_all_collection()