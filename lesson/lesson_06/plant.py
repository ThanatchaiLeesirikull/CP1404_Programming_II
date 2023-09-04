class Plant:
    def __init__(self, name="Benz", height=170.0, growth_rate=1.0):
        self.name = name
        self.height = height
        self.growth_rate = growth_rate

    def __str__(self):
        return f"Name: {self.name}\nHeight: {self.height}\nGrowth_rate: {self.growth_rate}"

    def feed(self, water):
        self.height += water * self.growth_rate


class Student:

    def __init__(self, first_name="", last_name="", student_id=0):
        self.first_name = first_name
        self.last_name = last_name
        self.id = student_id

    def __str__(self):
        return f"First name: {self.first_name}\nLast name: {self.last_name}\nStudent id: {self.id}"


class Programming_2:

    def __init__(self, marks):
        self.marks = marks

    def __lt__(self, other):
        return self.marks < other.marks


student1_marks = Programming_2(100)
student2_marks = Programming_2(90)

print(student1_marks < student2_marks)
print(student2_marks < student1_marks)

first_name = input("First name: ")
last_name = input("Last name: ")
student_id = int(input("ID: "))

s1 = Student(first_name, last_name, student_id)
print(f"{s1.first_name} has id {s1.id}")
print(s1)

p = Plant()

print("Before feeding:")
print(p)

p.feed(10)  # Feeding the plant with water

print("\nAfter feeding:")
print(p)
