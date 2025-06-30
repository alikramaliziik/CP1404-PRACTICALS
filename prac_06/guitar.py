"""
CP1404/CP5632 Practical - Guitar class
Estimated time: 10 minutes
Actual time: 13 minutes
"""

class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialize a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string representation of Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Return the age of the guitar in years."""
        current_year = 2025
        return current_year - self.year

    def is_vintage(self):
        """Return True if the guitar is 50 or more years old."""
        return self.get_age() >= 50
