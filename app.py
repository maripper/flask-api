from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import os

app = Flask(__name__)
CORS(app, origins='http://localhost:4200')


# Flask maps HTTP requests to Python functions.
# The process of mapping URLs to functions is called routing.
@app.route('/agrivalle', methods=['GET'])
def home():
    return {"data1":1,
            "data2":0.5,
            "data3":0.2}


# A method that runs the application server.
if __name__ == "__main__":
    # Threaded option to enable multiple instances for multiple user access support
    app.run(debug=False, threaded=True, port=5000)