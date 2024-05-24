from flask import Flask

app = Flask(__name__)


# Return list of every flight
@app.route('/flights', methods=['GET'])
def get_flights():
    return 'Not yet available'


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
def patch_flight(id):
    return 'Not yet available'
