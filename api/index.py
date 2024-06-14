from flask import Flask, jsonify, make_response, request
# from models.Flight import Flight
# from vercel import get
# from test import my_var

app = Flask(__name__)

# Currently all saved in one file because vercel doesn't allow other files that index.py per default
# (and I don't yet know how to change it)
flights_data = [
    {
      "Employee_idEmployee": 1,
      "destination": "Unknown",
      "idFlight": 0,
      "origin": "Zurich"
    },
    {
      "Employee_idEmployee": 3,
      "destination": "Unknown",
      "idFlight": 1,
      "origin": "Bern"
    }
]

meetings_data = [
    {
        'idMeeting': 0,
        'description': 'someDescription',
        'Businesstrip_idBusinesstrip': 1,
        'title': 'someTitle'
    },
    {
        'idMeeting': 1,
        'description': 'someOtherDescription',
        'Businesstrip_idBusinesstrip': 0,
        'title': 'someOtherTitle'
    }
]

employees_data = [
    {
        'idEmployee': 0,
        'name': "someName",
        'title': "someTitle",
        'businessTrips': [0, 3, 4]
    },
    {
        'idEmployee': 1,
        'name': "someOtherName",
        'title': "someOtherTitle",
        'businessTrips': [0, 2]
    }
]

businessTrips_data = [
        {
            'idBusinessTrip': 0,
            'description': "someDescription",
            'title': "someTitle",
            'employees': [0, 1]
        },
        {
            'idBusinessTrip': 1,
            'description': "someOtherDescription",
            'title': "someOtherTitle",
            'employees': [6]
        }
]


class Flight:

    _last_id = 1    # Set to 0 if flights_data gets cleared

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


class Meeting:

    _last_id = 1    # Set to 0 if meetings_data gets cleared

    def __init__(self, description: str, Businesstrip_idBusinesstrip: int, title: str):
        Meeting._last_id += 1
        self.idMeeting = Meeting._last_id
        self.description = description
        self.Businesstrip_idBusinesstrip = Businesstrip_idBusinesstrip
        self.title = title

    def to_dict(self):
        return {
            'idMeeting': self.idMeeting,
            'description': self.description,
            'Businesstrip_idBusinesstrip': self.Businesstrip_idBusinesstrip,
            'title': self.title
        }


class Employee:

    _last_id = 1    # Set to 0 if meetings_data gets cleared

    def __init__(self, name: str, title: str, businessTrips: list):
        Employee._last_id += 1
        self.idEmployee = Employee._last_id
        self.name = name
        self.title = title
        self.businessTrips = businessTrips

    def to_dict(self):
        return {
            'idEmployee': self.idEmployee,
            'name': self.name,
            'title': self.title,
            'businessTrips': [trip.to_dict() for trip in self.businessTrips]
        }


class BusinessTrip:

    _last_id = 1    # Set to 0 if businessTrips_data gets cleared

    def __init__(self, description: str, title: str, employees: list):
        BusinessTrip._last_id += 1
        self.idBusinessTrip = BusinessTrip._last_id
        self.description = description
        self.title = title
        self.employees = employees

    def to_dict(self):
        return {
            'idBusinessTrip': self.idBusinessTrip,
            'description': self.description,
            'title': self.title,
            'employees': [employee.to_dict() for employee in self.employees]
        }


# Check if API is up and running
@app.route('/')
def home():
    try:
        return {
            "statusCode": 200,
            "body": "API is up and running"
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": f"Internal Server Error: {str(e)}"
        }


# ---- flights endpoints ----

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


# ---- meetings endpoints ----

@app.route('/meetings', methods=['GET'])
def get_meetings():
    return jsonify(meetings_data)


@app.route('/meetings/<meeting_id>', methods=['GET'])
def get_meeting(meeting_id):
    for meeting in meetings_data:
        if meeting["idMeeting"] == int(meeting_id):
            return meeting
    return make_response("ID not found", 404)


@app.route('/meetings', methods=['POST'])
def post_meeting():
    data = request.get_json()
    meeting = Meeting(data.get('description'), data.get('Businesstrip_idBusinesstrip'), data.get('title'))
    meeting = meeting.to_dict()
    meetings_data.append(meeting)
    return make_response(jsonify(meeting), 201)


@app.route('/meetings/<meeting_id>', methods=['PUT'])
def put_meeting(meeting_id):
    index = None

    for meeting in meetings_data:
        if meeting["idMeeting"] == int(meeting_id):
            index = meetings_data.index(meeting)
            break

    if not index:
        return make_response("ID not found", 404)

    meetings_data.pop(index)

    data = request.get_json()
    meeting = Meeting(data.get('description'), data.get('Businesstrip_idBusinesstrip'), data.get('title'))
    meeting = meeting.to_dict()
    meetings_data.append(meeting)
    return make_response(jsonify(meeting), 200)


@app.route('/meetings/<meeting_id>', methods=['PATCH'])
def patch_meeting(meeting_id):
    data = request.get_json()
    for meeting in meetings_data:
        if meeting["idMeeting"] == int(meeting_id):
            if data.get('description'):
                meeting['description'] = data.get('description')
            if data.get('Businesstrip_idBusinesstrip'):
                meeting['Businesstrip_idBusinesstrip'] = data.get('Businesstrip_idBusinesstrip')
            if data.get('title'):
                meeting['title'] = data.get('title')
            return make_response(meeting, 200)

    return make_response("ID not found", 404)


@app.route('/meetings/<meeting_id>', methods=['DELETE'])
def delete_meeting(meeting_id):
    for meeting in meetings_data:
        if meeting["idFlight"] == int(meeting_id):
            index = meetings_data.index(meeting)
            meetings_data.pop(index)
            return meeting

    return make_response("ID not found", 404)


# ---- employees endpoints ----

@app.route('/employees', methods=['GET'])
def get_employees():
    return jsonify(employees_data)


@app.route('/employees/<employee_id>', methods=['GET'])
def get_employee(employee_id):
    for employee in employees_data:
        if employee["idEmployee"] == int(employee_id):
            return employee
    return make_response("ID not found", 404)


@app.route('/employees', methods=['POST'])
def post_employee():
    data = request.get_json()
    employee = Employee(data.get('name'), data.get('title'), data.get('businessTrips'))
    employee = employee.to_dict()
    employees_data.append(employee)
    return make_response(jsonify(employee), 201)


@app.route('/employees/<employee_id>', methods=['PUT'])
def put_employee(employee_id):
    index = None

    for employee in employees_data:
        if employee["idEmployee"] == int(employee_id):
            index = employees_data.index(employee)
            break

    if not index:
        return make_response("ID not found", 404)

    employees_data.pop(index)

    data = request.get_json()
    employee = Employee(data.get('name'), data.get('title'), data.get('businessTrips'))
    employee = employee.to_dict()
    employees_data.append(employee)
    return make_response(jsonify(employee), 200)


@app.route('/employees/<employee_id>', methods=['PATCH'])
def patch_employee(employee_id):
    data = request.get_json()
    for employee in employees_data:
        if employee["idEmployee"] == int(employee_id):
            if data.get('name'):
                employee['name'] = data.get('name')
            if data.get('title'):
                employee['title'] = data.get('title')
            if data.get('businessTrips'):
                employee['businessTrips'] = data.get('businessTrips')
            return make_response(employee, 200)

    return make_response("ID not found", 404)


@app.route('/employees/<employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    for employee in employees_data:
        if employee["idEmployee"] == int(employee_id):
            index = employees_data.index(employee)
            employees_data.pop(index)
            return employee

    return make_response("ID not found", 404)


# ---- businessTrip endpoints ----

@app.route('/businessTrips', methods=['GET'])
def get_businessTrips():
    return jsonify(businessTrips_data)


@app.route('/businessTrips/<businessTrip_id>', methods=['GET'])
def get_businessTrip(businessTrip_id):
    for businessTrip in businessTrips_data:
        if businessTrip["idBusinessTrip"] == int(businessTrip_id):
            return businessTrip
    return make_response("ID not found", 404)


@app.route('/businessTrips', methods=['POST'])
def post_businessTrip():
    data = request.get_json()
    businessTrip = BusinessTrip(data.get('description'), data.get('title'), data.get('employees'))
    businessTrip = businessTrip.to_dict()
    businessTrips_data.append(businessTrip)
    return make_response(jsonify(businessTrip), 201)


@app.route('/businessTrips/<businessTrip_id>', methods=['PUT'])
def put_businessTrip(businessTrip_id):
    index = None

    for businessTrip in businessTrips_data:
        if businessTrip["idBusinessTrip"] == int(businessTrip_id):
            index = businessTrips_data.index(businessTrip)
            break

    if not index:
        return make_response("ID not found", 404)

    businessTrips_data.pop(index)

    data = request.get_json()
    businessTrip = BusinessTrip(data.get('description'), data.get('title'), data.get('employees'))
    businessTrip = businessTrip.to_dict()
    businessTrips_data.append(businessTrip)
    return make_response(jsonify(businessTrip), 200)


@app.route('/businessTrips/<businessTrip_id>', methods=['PATCH'])
def patch_businessTrip(businessTrip_id):
    data = request.get_json()
    for businessTrip in businessTrips_data:
        if businessTrip["idBusinessTrip"] == int(businessTrip_id):
            if data.get('description'):
                businessTrip['description'] = data.get('description')
            if data.get('title'):
                businessTrip['title'] = data.get('title')
            if data.get('employees'):
                businessTrip['employees'] = data.get('employees')
            return make_response(businessTrip, 200)

    return make_response("ID not found", 404)


@app.route('/businessTrips/<businessTrip_id>', methods=['DELETE'])
def delete_businessTrip(businessTrip_id):
    for businessTrip in businessTrips_data:
        if businessTrip["idBusinessTrip"] == int(businessTrip_id):
            index = businessTrips_data.index(businessTrip)
            businessTrips_data.pop(index)
            return businessTrip

    return make_response("ID not found", 404)


if __name__ == '__main__':
    app.run(debug=True)
