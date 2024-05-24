class Employee:

    _last_id = 0

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
