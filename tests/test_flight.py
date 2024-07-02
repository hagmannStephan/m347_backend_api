# tests/test_flight.py

from api.models.Flight import Flight

def test_flight_initialization():
    flight = Flight(1, 'New York', 'London', 1)
    assert flight.idFlight == 1
    assert flight.Employee_idEmployee == 1
    assert flight.origin == 'New York'
    assert flight.destination == 'London'

def test_to_dict():
    flight = Flight(2, 'Paris', 'Tokyo', 2)
    flight_dict = flight.to_dict()
    expected_dict = {
        'idFlight': 2,
        'Employee_idEmployee': 2,
        'origin': 'Paris',
        'destination': 'Tokyo'
    }
    assert flight_dict == expected_dict
