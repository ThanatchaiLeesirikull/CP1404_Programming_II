from datetime import datetime


class Person:
    def __init__(self, name: str, date_of_birth: datetime.date):
        self.name = name
        self.date_of_birth = date_of_birth
        self.address = ""
        print("Person.init")

    def __str__(self):
        date_string = datetime.strftime(self.date_of_birth, "%d/%m/%Y")
        return f"{self.name} DOB: {date_string}, lives at {self.address}"

    def __repr__(self):
        return str(vars(self))

    def get_age(self):
        return int((datetime.now() - self.date_of_birth).days / 365.24)


