class Flight:

    _last_id = 0

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
