from flask import Flask, request, jsonify
from chat import get_response
from flask_cors import CORS
import subprocess
import json

app = Flask(__name__)
CORS(app)

@app.route('/api/generate', methods=['POST'])
def generate():
    data = request.get_json()
    prompt = data.get('prompt')

    response = get_response(prompt) 

    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
