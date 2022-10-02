"""Base module with the parent's class Vehicle"""
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle:
    """Base class of vehicle
    All attrs are type-restricted and have def-values
    """

    def __init__(self, weight: float = 0, fuel: float = 0,
                 fuel_consumption: float = 0, started: bool = False):
        """Initialize all the attrs with def values
        weight: float
        fuel: float
        fuel_consumption: float
        started: bool
        """
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = started

    def start(self):
        """
        Method checks th vehicle's condition and if fuel is > 0 - turn started on (True)
        :return: LowFuelError if there's no fuel
        """
        if not self.started:
            if self.fuel:  # fuel > 0 for engine started
                self.started = True
            else:
                raise LowFuelError

    def move(self, distance):
        """
        Method checks the vehicle's condition and if fuel is enough -
         reduce fuel lvl and pass all the distance
        :return: NotEnoughFuel if there's no enough  fuel
        """
        if self.fuel >= self.fuel_consumption * distance:
            self.fuel -= self.fuel_consumption * distance
        else:
            raise NotEnoughFuel
