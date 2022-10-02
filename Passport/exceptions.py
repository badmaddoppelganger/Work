"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


# "Pass" is don't needed - W0107: Unnecessary pass statement (unnecessary-pass)

class LowFuelError(Exception):
    """Init new type of exception Low Fuel!"""


class NotEnoughFuel(Exception):
    """Init new type of exception Not enough fuel!"""


class CargoOverload(Exception):
    """Init new type of exception Cargo overload!"""
