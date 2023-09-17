"""
CP1404/CP5632 Practical - Suggested Solution
SilverServiceTaxi class, derived from Taxi
"""

from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Represent a SilverServiceTaxi."""
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a string representation of a SilverServiceTaxi."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Get the current fare."""
        return self.flagfall + super().get_fare()


if __name__ == '__main__':
    silver_service_taxi = SilverServiceTaxi(name='Hummer', fuel=200, fanciness=4)
    silver_service_taxi.drive(0)
    silver_service_taxi.get_fare()
    print(f"{silver_service_taxi}")
