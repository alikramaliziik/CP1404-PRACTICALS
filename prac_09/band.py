class Band:
    """Band class for storing a collection of musicians."""

    def __init__(self, name=""):
        """Initialise a Band with a name and empty musician collection."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of the Band."""
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"

    def __repr__(self):
        """Return a string representation of the Band, showing variables."""
        return str(vars(self))

    def add(self, musician):
        """Add a musician to the band's collection."""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing each musician playing their first instrument."""
        return "\n".join(musician.play() for musician in self.musicians)
