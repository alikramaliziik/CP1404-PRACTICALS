from car import Car
import random

class UnreliableCar(Car):
    """Specialised version of a Car with a reliability factor."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car a given distance based on reliability.

        Generate a random number between 0 and 100; drive only if it's less than reliability.
        Return the distance actually driven (0 if the car doesn't drive).
        """
        if random.uniform(0, 100) < self.reliability:
            return super().drive(distance)
        return 0
