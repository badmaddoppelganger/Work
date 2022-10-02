"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    """New class with Vehicle's attrs plus new attrs -
    :max_cargo: cargo limit weight (see import details)
    :cargo - weight of Plane's luggage
    """
    def __init__(self, weight, fuel, fuel_consumption, max_cargo=0):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo
        self.cargo = 0

    def load_cargo(self, add_weight):
        """Method added value to the cargo attr and check that cargo is not > max_cargo"""
        if (self.cargo + add_weight) <= self.max_cargo:
            self.cargo += add_weight
        else:
            raise CargoOverload

    def remove_all_cargo(self):
        """Method return and after removes value of attr cargo"""
        old_cargo = self.cargo
        self.cargo = 0
        return old_cargo
