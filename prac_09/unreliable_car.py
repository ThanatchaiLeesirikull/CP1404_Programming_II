import random

from prac_09.car import Car


class UnreliableCar(Car):
    """Represent an UnreliableCar object that inherits from Car."""

    def __init__(self, name="", fuel=0, reliability=0):
        """Initialize an UnreliableCar instance.

        name: string, reference name for car
        fuel: float, one unit of fuel drives one kilometer
        reliability: float between 0 and 100, representing the chance of driving
        """
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car a given distance if reliability allows.

        Drive given distance only if a random number is less than reliability,
        otherwise, return 0 km driven.
        """
        if random.randint(0, 100) < self.reliability:
            return super().drive(distance)
        else:
            return 0


if __name__ == '__main__':
    UnreliableCar()


