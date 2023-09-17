from datetime import datetime

from lesson.lesson_09.person import Person


class Student(Person):
    def __init__(self, student_id: int, course: str, **kwargs):
        super().__init__(**kwargs)
        self.id = student_id
        self.course = course
        print("Student.init")

    def __str__(self):
        print("Student str")
        return f"{super().__str__()} [{self.id}], doing course {self.course}"

    def __repr__(self):
        print("Student repr")
        return str(vars(self))


if __name__ == '__main__':
    s1 = Student(name="Jerry", date_of_birth=datetime(2001, 12, 14), student_id=14305967, course="IT")
    print(s1)
    print(s1.get_age())