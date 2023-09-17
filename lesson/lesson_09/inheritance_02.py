from datetime import datetime

from lesson.lesson_09.inheritance import Student


class Person:
    def __init__(self, name: str, date_of_birth: datetime.date, student_id: int, course: str):
        self.name = name
        self.date_of_birth = date_of_birth
        self.student_id = student_id
        self.course = course

    def __repr__(self):
        return str(vars(self))

    def get_age(self):
        today = datetime.now().date()
        age = today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        return age


if __name__ == '__main__':
    p1 = Person("Jane", datetime(1999, 2, 14), 14305967, "IT")
    print(p1)
    print(p1.get_age())

    s1 = Student("Benz", datetime(1999, 2, 14), 143025967, "IT")
    print(s1)
