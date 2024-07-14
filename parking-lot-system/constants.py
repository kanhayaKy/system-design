from enum import Enum


class VehicleType(Enum):
    Motorcycle = 1
    Car = 2
    Truck = 3


class ParkingSpotStatus(Enum):
    Available = "Available"
    Reserved = "Reserved"
