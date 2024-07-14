from typing import List

from .parking_level import Level
from .vehicle import Vehicle


class ParkingLot:
    _instance = None

    def __init__(self, name) -> None:
        if ParkingLot._instance is not None:
            raise Exception("Attempted to recreate a singleton")
        else:
            ParkingLot._instance = self
            self.levels: List[Level] = []

    @staticmethod
    def get_instance():
        if ParkingLot._instance is None:
            ParkingLot()
        return ParkingLot._instance

    def add_level(self, level):
        self.levels.append(level)

    def park_vehicle(self, vehicle) -> bool:
        for level in self.levels:
            if level.park_vehicle(vehicle):
                return True

        return False

    def unpark_vehicle(self, vehicle: Vehicle) -> bool:
        for level in self.levels:
            if level.unpark_vehicle(vehicle):
                return True
        return False

    def display_availability(self) -> None:
        for level in self.levels:
            level.display_availability()
