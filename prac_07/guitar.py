"""
CP1404/CP5632 Practical
Guitar class
"""

class Guitar:
    """Represent a Guitar object."""
    
    def __init__(self, name="", year=0, cost=0.0):
        """Initialise a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost
    
    def __str__(self):
        """Return string representation of a Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"
    
    def __repr__(self):
        """Return detailed string representation of a Guitar."""
        return f"Guitar({self.name}, {self.year}, {self.cost})"
    
    def is_vintage(self):
        """Return True if the guitar is 50 or more years old."""
        return 2025 - self.year >= 50
    
    def __lt__(self, other):
        """Compare guitars by year for sorting."""
        return self.year < other.year
