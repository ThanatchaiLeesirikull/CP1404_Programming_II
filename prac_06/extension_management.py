class Person:

    def __init__(self, first_name="", last_name="", age=0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __lt__(self, other):
        return self.age < other.age

    def __str__(self):
        return f"{self.first_name} {self.last_name}: {self.age} years old"


def main():
    persons = []

    number_of_people = int(input("How many people?: "))

    for i in range(number_of_people):
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        age = int(input("Age: "))

        person = Person(first_name, last_name, age)
        persons.append(person)

    persons.sort()

    for person in persons:
        print(person)


main()
