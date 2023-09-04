class Point:

    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"{self.x}, {self.y}"

    def __eq__(self, other):
        return self.x == self.y

    def __le__(self, other):
        return self.x <= self.y

    def __lt__(self, other):
        return self.x < self.y

    def __add__(self, other):
        return City(self.x + other.x, self.y + other.y)


number_1 = Point(34, 24)
number_2 = Point(14, 24)

print(number_1.y < number_1.x)


class City:

    def __init__(self, name="", population=0, percent=0.0):
        self.name = name
        self.population = population
        self.percent = percent

    def __repr__(self):
        return f"{self.name}, {self.population:,}, {self.percent}%"

    def __lt__(self, other):
        """less than"""
        return self.population < other.population

    def __le__(self, other):
        """less than or equal"""
        return self.population <= other.population

    def __eq__(self, other):
        """equal"""
        return other.population == self.population

    def __add__(self, other):
        return City(self.name + other.name, self.population + other.population, 100)


def run_tests():
    c1 = City("Tokyo", 13921000, 11.20)
    c2 = City("Rome", 2761632, 4.70)

    print(c1 + c2)


if __name__ == '__main__':
    run_tests()

