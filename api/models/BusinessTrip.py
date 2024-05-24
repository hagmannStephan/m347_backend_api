class BusinessTrip:

    _last_id = 0

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
