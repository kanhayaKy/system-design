from abc import ABC

from .constants import VehicleType


class Vehicle(ABC):
    def __init__(self, licence_plate, type) -> None:
        self.__license_plate = licence_plate
        self.__type = type

    def get_type(self) -> VehicleType:
        return self.__type

    def get_license_plate(self) -> str:
        return self.__license_plate


class Motorcycle(Vehicle):
    def __init__(self, licence_plate) -> None:
        type = VehicleType.Car
        super().__init__(licence_plate, type)


class Car(Vehicle):
    def __init__(self, licence_plate) -> None:
        type = VehicleType.Car
        super().__init__(licence_plate, type)


class Car(Vehicle):
    def __init__(self, licence_plate) -> None:
        type = VehicleType.Car
        super().__init__(licence_plate, type)
