class Flight:

    _last_id = 1    # Set to 0 if flights_data gets cleared

# api/models/Flight.py

class Flight:
    def __init__(self, idFlight, origin, destination, Employee_idEmployee):
        self.idFlight = idFlight
        self.origin = origin
        self.destination = destination
        self.Employee_idEmployee = Employee_idEmployee

    def to_dict(self):
        return {
            'idFlight': self.idFlight,
            'Employee_idEmployee': self.Employee_idEmployee,
            'origin': self.origin,
            'destination': self.destination
        }