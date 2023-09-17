from datetime import datetime

from lesson.lesson_09.inheritance_02 import Person


class Student(Person):
    def __init__(self, name: str, date_of_birth: datetime.date, student_id: int, course: str, **kwargs):
        super().__init__(**kwargs)
        print("Student.init")
