class Guitar:
    """Represent a Car object."""

    def __init__(self, name="", year=0, cost=0.0):
        """Initialise a Car instance. fuel: float, one unit of fuel drives one kilometre"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of the Car."""
        return f"{self.name} ({self.year}) : ${self.cost}"

    def __lt__(self, other):
        return self.year < other.year

    def get_age(self):
        return 2022 - self.year

    def is_vintage(self):
        return self.get_age() >= 50

