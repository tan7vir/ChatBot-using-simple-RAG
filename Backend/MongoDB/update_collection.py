from pymongo import MongoClient

# MongoDB connection URL
url = "mongodb://localhost:27017"
client = MongoClient(url)

# Database and Collection Name
db_name = "AllChat"
collection_name = "PhysicsChat"


def update_collection(AssisContent, content):
    try:
        # Connect to the MongoDB server
        print("Connected successfully to server")
        
        # Access the database and collection
        db = client[db_name]
        collection = db[collection_name]

        # Data to insert
        new_data = [
            {
                "role": "user",
                "content": content
            },
            {
                "role": "assistant",
                "content": AssisContent
            }
        ]

        # Insert the new data into the collection
        insert_result = collection.insert_many(new_data)
        return "Success"
    except Exception as error:
        print("Error:", error)
        return "error in updating collection"