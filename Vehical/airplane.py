from flying_vehicle import FlyingVehicle
from ground_vehicle import GroundVehicle

class Airplane(FlyingVehicle,GroundVehicle):
    def __init__(self,airline: str,number_of_crew: int,captain: str, fuel: str, number_of_fins: int, **kwargs):
        self.airline = airline
        self.number_of_crew = number_of_crew
        self.captain = captain
        super().__init__(fuel, number_of_fins, **kwargs)
        
class B707(Airplane):
    def __init__(self, airline: str, number_of_crew: int, captain: str, fuel: str, number_of_fins: int, **kwargs):
        super().__init__(airline, number_of_crew, captain, fuel, number_of_fins, **kwargs)