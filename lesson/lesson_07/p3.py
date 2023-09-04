x = isinstance(5, int)
print(x)

x = isinstance("str", int)
print(x)

print([3 + 4] * 4)


class Ocean:

    def __init__(self, sea_creature_name, sea_creature_age):
        self.name = sea_creature_name
        self.age = sea_creature_age

    def __str__(self):
        return f'The creature type is {self.name} and the age is {self.age}'

    def __repr__(self):
        return f'Ocean(\'{self.name}\', {self.age})'


c = Ocean('Jellyfish', 5)

print(str(c))
print(repr(c))