from pymongo import MongoClient

# MongoDB connection URL
url = "mongodb://localhost:27017"
client = MongoClient(url)

# Database and Collection Name
db_name = "AllChat"
# collection_name = "PhysicsChat"

def delete_chat(collection_name):
    try:
        # Connect to the MongoDB server
        print("Connected successfully to server")
        
        # Access the database and collection
        db = client[db_name]
        collection = db[collection_name]

        # Delete all data from the collection
        delete_result = collection.delete_many({})
        print(f"{delete_result.deleted_count} documents deleted from {collection_name}")

        # Data to insert
        new_data = [
            {
                "role": "assistant",
                "content": "How may I assist you today?"
            }
        ]

        # Insert the new data into the collection
        insert_result = collection.insert_many(new_data)
        return "Success"
    except Exception as error:
        print ("Error deleting chat:", error)
