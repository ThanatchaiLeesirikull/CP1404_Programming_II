from datetime import datetime

from lesson.lesson_09.person import Person


class Employee(Person):
    def __init__(self, name: str, date_of_birth: datetime.date, employee_id: int):
        super().__init__(name, date_of_birth)
        self.employee_id = employee_id
        print("Employee.init")

    def __repr__(self):
        print("Employee repr")
        date_string = datetime.strftime(self.date_of_birth, "%d/%m/%Y")
        return f"{self.name} ({date_string}), Employee ID: {self.employee_id}"



