class Flight:

    _last_id = 0

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
