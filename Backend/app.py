from flask import Flask, request, jsonify, make_response
from get_response import get_response
from MongoDB.fetch_all_collection import fetch_all_collection, fetch_chat_list
from MongoDB.delete_chat import delete_chat
from MongoDB.update_collection import update_collection
import atexit
import subprocess
import os

from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Function to start Ollama
def start_ollama():
    try:
        # Redirect stdout and stderr to os.devnull
        with open(os.devnull, 'w') as devnull:
            ollama_process = subprocess.Popen(
                ["ollama", "serve"], 
                stdout=devnull,  # Discard stdout
                stderr=devnull,  # Discard stderr
                shell=True       # Required for Windows
            ) 
            print("Ollama is starting...", flush=True)
            return ollama_process
    except Exception as e:
        print(f"Error starting Ollama: {e}", flush=True)
        return None



# When Backend starts
ollama_process = start_ollama()

# Stop the Ollama server
def stop_ollama():
    if ollama_process:
        ollama_process.terminate()  
        print("Ollama server stopped.", flush=True)

# Register the stop_ollama function to be called on exit
atexit.register(stop_ollama)

@app.route('/api/generate', methods=['POST'])
def generate():
    data = request.get_json()
    response = get_response(data) 
    return jsonify(response)


@app.route('/api/fetch_collection', methods=['POST'])
def fetch_collection():
    # Call the function to fetch all collections and return the result
    response = fetch_all_collection()  # No parameters expected
    return jsonify(response)  # Return as JSON


@app.route('/api/fetch_chat', methods=['POST'])
def fetch_chat():
    
    data = request.get_json()
    collection_name = data.get("collection_name")
    response = fetch_chat_list(collection_name=collection_name)  # No parameters expected
    
    for doc in response:
        doc['_id'] = str(doc['_id'])  # Convert ObjectId to string

    return jsonify(response)  # Return as JSON



@app.route('/api/delete_chat_', methods=['POST'])
def delete_chat_():
    
    data = request.get_json()
    collection_name = data.get("collection_name")
    response = delete_chat(collection_name=collection_name)  
    return jsonify(response)


@app.route('/api/add_response', methods=['POST'])
def add_response():
    
    data = request.get_json()
    AssisContent = data.get("AssisContent")
    content = data.get("content")
    response = update_collection(AssisContent=AssisContent, content=content)
    return jsonify(response)
    
if __name__ == "__main__":
    app.run(debug=True)
