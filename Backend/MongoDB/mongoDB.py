from pymongo import MongoClient

# MongoDB connection URL
url = "mongodb://localhost:27017"
client = MongoClient(url)

# Database and Collection Name
db_name = "AllChat"
collection_name = "PhysicsChat"

def fetch_data():
    try:
        # Connect to the MongoDB server
        print("Connected successfully to server")
        
        # Access the database and collection
        db = client[db_name]
        collection = db[collection_name]

        # Fetch all data from the collection
        data = list(collection.find({}))  # Empty query `{}` means fetch all documents

        print("Type of Data:", type(data))
        # Output the data
        print("Data fetched successfully:", data)
    except Exception as error:
        print("Error fetching data:", error)
    finally:
        # Close the connection
        client.close()

def reset_and_insert_data():
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
            },
            {
                "role": "user",
                "content": "I need help with MongoDB."
            }
        ]

        # Insert the new data into the collection
        insert_result = collection.insert_many(new_data)
        print("New data inserted successfully with IDs:", insert_result.inserted_ids)
    except Exception as error:
        print("Error:", error)
    finally:
        # Close the connection
        client.close()

def add_data():
    try:
        # Connect to the MongoDB server
        print("Connected successfully to server")
        
        # Access the database and collection
        db = client[db_name]
        collection = db[collection_name]

        # Data to insert
        new_data = [
            {
                "role": "assistant",
                "content": "What specific topics in physics do you need help with?"
            },
            {
                "role": "user",
                "content": "Can you explain Newton's Laws of Motion?"
            }
        ]

        # Insert the new data into the collection
        insert_result = collection.insert_many(new_data)
        print(f"{len(insert_result.inserted_ids)} new documents inserted successfully.")
    except Exception as error:
        print("Error:", error)
    finally:
        # Close the connection
        client.close()

def insert_into_new_collection():
    new_collection_name = 'prompt'
    try:
        # Connect to the MongoDB server
        print("Connected successfully to server")
        
        # Access the database
        db = client[db_name]
        
        # New data to insert
        new_data = {
            "role": "assistant",
            "content": "This is a new collection!"
        }
        
        # Insert the new data into the new collection
        collection = db[new_collection_name]  # This will create the collection if it doesn't exist
        insert_result = collection.insert_one(new_data)
        print(f"Data inserted into {new_collection_name} collection successfully.")
    except Exception as error:
        print("Error:", error)
    finally:
        # Close the connection
        client.close()

# Uncomment the desired function to run
# fetch_data()
# reset_and_insert_data()
# add_data()
insert_into_new_collection()
