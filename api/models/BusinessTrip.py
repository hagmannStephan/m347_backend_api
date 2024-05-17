from datetime import datetime
from typing import List


class BusinessTrip:
    def __init__(self, id: int, title: str, description: str,
                 start_trip: datetime, end_trip: datetime, meetings: list, employees: list):
        self.id = id
        self.title = title
        self.description = description
        self.start_trip = start_trip
        self.end_trip = end_trip
        self.meetings = meetings
        self.employees = employees

    def get_id(self):
        return self.id

    def set_id(self, id: int):
        self.id = id

    def get_title(self):
        return self.title

    def set_title(self, title: str):
        self.title = title

    def get_description(self):
        return self.description

    def set_description(self, description: str):
        self.description = description

    def get_meetings(self):
        return self.meetings

    def set_meetings(self, meetings: List['Meeting']):
        self.meetings = meetings

    def get_employees(self):
        return self.employees

    def set_employees(self, employees: List['Employee']):
        self.employees = employees

    def get_start_trip(self):
        return self.start_trip

    def set_start_trip(self, start_trip: datetime):
        self.start_trip = start_trip

    def get_end_trip(self):
        return self.end_trip

    def set_end_trip(self, end_trip: datetime):
        self.end_trip = end_trip

    def __str__(self):
        return (f"BusinessTrip [id={self.id}, title={self.title}, description={self.description}, "
                f"start_trip={self.start_trip}, end_trip={self.end_trip}, "
                f"meetings={self.meetings}, employees={self.employees}]")
