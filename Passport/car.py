"""
создайте класс `Car`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.engine import Engine


class Car(Vehicle):
    """New class with Vehicle's attrs plus new attr - engine
    :type engine: dataclass Engine (see import details)
    """
    engine = Engine()

    def set_engine(self, engine):
        """
        Set Engine example on Car.
        """
        self.engine = engine
