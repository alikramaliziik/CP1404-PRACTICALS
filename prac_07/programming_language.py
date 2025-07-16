"""
CP1404/CP5632 Practical
Programming Language class with tests.
Estimated time: 30 minutes
Actual time: 45 minutes
"""

class ProgrammingLanguage:
    """Represent information about a programming language."""

    def __init__(self, name, typing, reflection, year, pointer_arithmetic):
        """Construct a ProgrammingLanguage with the given attributes."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year
        self.pointer_arithmetic = pointer_arithmetic

    def __str__(self):
        """Return a readable string representation of a ProgrammingLanguage."""
        return (f"{self.name} ({self.typing}), Reflection: {self.reflection}, "
                f"Pointer Arithmetic: {self.pointer_arithmetic}, First appeared: {self.year}")

    def __repr__(self):
        """Return a detailed string representation for debugging."""
        return (f"ProgrammingLanguage(name='{self.name}', typing='{self.typing}', "
                f"reflection={self.reflection}, year={self.year}, "
                f"pointer_arithmetic={self.pointer_arithmetic})")

    def is_dynamic(self):
        """Return True if the language is dynamically typed."""
        return self.typing == "Dynamic"

def run_tests():
    """Run simple tests/demos on ProgrammingLanguage class."""
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995, False)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991, False)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991, False)

    languages = [ruby, python, visual_basic]
    print(python)
    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)

if __name__ == "__main__":
    run_tests()
