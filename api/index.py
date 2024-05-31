from flask import Flask, jsonify, make_response, request
# from models.Flight import Flight
# from vercel import get

app = Flask(__name__)

# Currently all saved in one file because vercel doesn't allow other files that index.py per default
# (and I don't yet know how to change it)
flights_data = [
    {
      "Employee_idEmployee": 1,
      "destination": "Unknown",
      "idFlight": 1,
      "origin": "Zurich"
    },
    {
      "Employee_idEmployee": 3,
      "destination": "Unknown",
      "idFlight": 2,
      "origin": "Bern"
    }
]


class Flight:

    _last_id = 0    # Currently id's may occur more than once, because there are already elements in the list

    def __init__(self, Employee_idEmployee: int, origin: str, destination: str, ):
        Flight._last_id += 1
        self.idFlight = Flight._last_id
        self.Employee_idEmployee = Employee_idEmployee
        self.origin = origin
        self.destination = destination

    def to_dict(self):
        return {
            'idFlight': self.idFlight,
            'Employee_idEmployee': self.Employee_idEmployee,
            'origin': self.origin,
            'destination': self.destination
        }


# Check if API is up and running
@app.route('/')
def home():
    return 'API is up and running!'


# Return list of every flight
@app.route('/flights', methods=['GET'])
def get_flights():
    return jsonify(flights_data)


# Get specific flight by id
@app.route('/flights/<flight_id>', methods=['GET'])
def get_flight(flight_id):
    for flight in flights_data:
        if flight["idFlight"] == int(flight_id):
            return flight
    return make_response("ID not found", 404)


# Create a new flight
@app.route('/flights', methods=['POST'])
def post_flight():
    data = request.get_json()
    flight = Flight(data.get('Employee_idEmployee'), data.get('origin'), data.get('destination'))
    flight = flight.to_dict()
    flights_data.append(flight)
    return make_response(jsonify(flight), 201)


# Replace an already existing flight
@app.route('/flights/<flight_id>', methods=['PUT'])
def put_flight(flight_id):
    index = None

    for flight in flights_data:
        if flight["idFlight"] == int(flight_id):
            index = flights_data.index(flight)
            break

    if not index:
        return make_response("ID not found", 404)

    flights_data.pop(index)

    data = request.get_json()
    flight = Flight(data.get('Employee_idEmployee'), data.get('origin'), data.get('destination'))
    flight = flight.to_dict()
    flights_data.append(flight)
    return make_response(jsonify(flight), 200)


# Modify an already existing flight
@app.route('/flights/<flight_id>', methods=['PATCH'])
def patch_flight(flight_id):
    data = request.get_json()
    for flight in flights_data:
        if flight["idFlight"] == int(flight_id):
            if data.get('Employee_idEmployee'):
                flight['Employee_idEmployee'] = data.get('Employee_idEmployee')
            if data.get('origin'):
                flight['origin'] = data.get('origin')
            if data.get('destination'):
                flight['destination'] = data.get('destination')
            return make_response(flight, 200)

    return make_response("ID not found", 404)


# Delete a flight
@app.route('/flights/<flight_id>', methods=['DELETE'])
def delete_flight(flight_id):
    for flight in flights_data:
        if flight["idFlight"] == int(flight_id):
            index = flights_data.index(flight)
            flights_data.pop(index)
            return flight

    return make_response("ID not found", 404)


if __name__ == '__main__':
    app.run(debug=True)
