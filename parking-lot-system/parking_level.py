from .parking_spot import ParkingSpot
from .vehicle import Vehicle


class Level:
    def __init__(self, level_number, spots) -> None:
        self.floor = level_number
        self.parking_spots = [ParkingSpot(spot, type) for spot, type in spots]

    def park_vehicle(self, vehicle: Vehicle) -> bool:
        for spot in self.parking_spots:
            if not spot.is_reserved() and spot.get_vehicle_type == vehicle.get_type():
                return spot.reserve_spot(vehicle)

        print(f"No parking spots found at level {self.floor}")
        return False

    def unpark_vehicle(self, vehicle: Vehicle) -> bool:
        for spot in self.parking_spots:
            if not spot.is_reserved() and spot.get_parked_vehicle() == vehicle:
                return spot.release_spot()

        print(f"Vehicle not found at level {self.floor}")
        return False

    def display_availability(self) -> None:
        print(f"Availability for Level : {self.floor}")

        for spot in self.parking_spots:
            print(f"Spot {spot.get_spot_number()} : {spot.get_spot_status()} ")
