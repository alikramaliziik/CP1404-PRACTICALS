"""
CP1404/CP5632 Practical - Programming Language class
Estimated time: 10 minutes
Actual time: 15 minutes
"""

class ProgrammingLanguage:
    """Represent a Programming Language object."""

    def __init__(self, name, typing, reflection, year):
        """Initialize a ProgrammingLanguage instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return True if the programming language is dynamically typed."""
        return self.typing == "Dynamic"

    def __str__(self):
        """Return string representation of ProgrammingLanguage."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
