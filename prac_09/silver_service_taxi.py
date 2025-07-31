from taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi with fanciness scaling and flagfall."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi instance, based on parent class Taxi."""
        super().__init__(name, fuel)
        self.price_per_km = Taxi.price_per_km * fanciness

    def get_fare(self):
        """Return the price for the taxi trip, including flagfall."""
        return super().get_fare() + self.flagfall

    def __str__(self):
        """Return a string representation, including flagfall."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"
