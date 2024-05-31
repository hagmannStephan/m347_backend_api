from flask import Flask, jsonify
from models.Flight import Flight
# from vercel import get
import os
import requests

app = Flask(__name__)


# Check if API is up and running
@app.route('/')
def home():
    return 'Not yet available'


# Return list of every flight
@app.route('/flights', methods=['GET'])
def get_flights():
    flight = Flight(1, "Zurich", "Unknown")
    flight = flight.to_dict()
    return jsonify(flight)


# Get specific flight by id
@app.route('/flights/<id>', methods=['GET'])
def get_flight(id):
    return 'Not yet available'


# Create a new flight
@app.route('/flights', methods=['POST'])
def post_flight():
    return 'Not yet available'


# Replace an already existing flight
@app.route('/flights', methods=['PUT'])
def put_flight():
    return 'Not yet available'


# Modify an already existing flight
@app.route('/flights/<id>', methods=['PATCH'])
def patch_flight(id):
    return 'Not yet available'


# Delete a flight
@app.route('/flights/<id>', methods=['DELETE'])
def delete_flight(id):
    return 'Not yet available'


if __name__ == '__main__':
    app.run(debug=True)
