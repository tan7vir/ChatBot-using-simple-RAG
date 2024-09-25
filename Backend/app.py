from flask import Flask, request, jsonify
from get_response import get_response
from flask_cors import CORS
import subprocess
import json

app = Flask(__name__)
CORS(app)

@app.route('/api/generate', methods=['POST'])
def generate():
    data = request.get_json()

    response = get_response(data) 

    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
