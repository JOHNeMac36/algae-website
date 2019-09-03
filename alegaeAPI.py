#!/usr/bin/python

from flask import Flask, jsonify
from flask_cors import CORS
import json
import serialTest

app = Flask(__name__)
CORS(app)

@app.route('/algae_api/measurements')
def get_measurements():

    # a Python object (dict):
    x = serialTest.getMeasurement()
    return jsonify(x)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
