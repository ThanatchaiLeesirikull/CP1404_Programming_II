from datetime import datetime

from lesson.lesson_09.employee import Employee
from lesson.lesson_09.person import Person
from lesson.lesson_09.student import Student


def main():
    p1 = Person("Jane", datetime(1999, 2, 14))
    print(p1)
    print(p1.get_age())
    s1 = Student(name="Jerry", date_of_birth=datetime(2021, 12, 12), student_id=14305967, course="BIT")
    print(s1)
    print(s1.get_age())
    e1 = Employee("Jack", datetime(1999, 2, 14), 2354)
    print(e1)
    e1.address = "123 Home St"
    people = [p1, s1, e1]
    for person in people:
        print(person)


if __name__ == '__main__':
    main()
