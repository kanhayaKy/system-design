from .constants import VehicleType, ParkingSpotStatus

from .vehicle import Vehicle


class ParkingSpot:
    def __init__(self, spot_number, vehicle_type=VehicleType.Car) -> None:
        self.__spot_number = spot_number
        self.__vehicle_type = vehicle_type
        self.__parked_vehicle = None

    def is_reserved(self) -> bool:
        return self.__parked_vehicle is None

    def get_spot_status(self) -> str:
        if self.is_reserved():
            return ParkingSpotStatus.Reserved
        else:
            return ParkingSpotStatus.Available

    def get_spot_number(self) -> str:
        return self.__spot_number

    def get_parked_vehicle(self) -> Vehicle:
        return self.__parked_vehicle

    def get_vehicle_type(self) -> VehicleType:
        return self.__vehicle_type

    def reserve_spot(self, vehicle: Vehicle) -> bool:
        if self.is_reserved():
            print("This spot is already reserved")
            return False

        if self.get_vehicle_type() != vehicle.get_type():
            print("Invalid vehicle for the given spot")
            return False

        self.__parked_vehicle = vehicle
        return True

    def release_spot(self) -> bool:
        if not self.is_reserved():
            print("Parking spot is not reserved")
            return True

        self.__parked_vehicle = None
        return True
