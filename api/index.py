from flask import Flask
import json

app = Flask(__name__)


# Return list of every flight
@app.route('/flights', methods=['GET'])
def get_flights():
    with open('data/flights.json', 'r') as file:
        data = json.load(file)
    return data


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
