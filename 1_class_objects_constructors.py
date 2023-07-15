# class Person:
#     def __init__(self, first_name, last_name, age, birth_date, where_from):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.birth_day = birth_date
#         self.where_from = where_from
#
#     def __repr__(self):
#         return f"Odamning ism faimiliyasi {self.first_name} {self.last_name}"
#
#
# asil = Person('Asilbek', 'Tolibov', 19, 2004, 'Navai')
# print(asil)
#
# from uuid import uuid1
#
#
# class Teacher:
#     def __init__(self, name, teach_object, practise):
#         self.name = name
#         self.teach_object = teach_object
#         self.practise = practise
#         self.id = uuid1()
#
#     def __repr__(self):
#         return f'name: {self.name} Object: {self.teach_object} Practise: {self.practise} id: {self.id}'
#
#
# class Student:
#     def __init__(self, name, last_name):
#         self.name = name
#         self.last_name = last_name
#         self.subjects = []
#         self.id = uuid1()
#
#     def add_subjects(self, sub):
#         self.subjects.append(sub)
#
#     def get_subjects(self):
#         return self.subjects
#
#     def __repr__(self):
#         return f'{self.name} {self.last_name}'
#
#
# class Fan:
#     def __init__(self, fan_name, fan_soati, fan_yunalishi):
#         self.name = fan_name
#         self.soati = fan_soati
#         self.yunalishi = fan_yunalishi
#         self.id = uuid1()
#
#     def __repr__(self):
#         return f'{self.name} {self.soati} {self.yunalishi}{self.id}'
#
#
# class Group:
#     def __init__(self, title):
#         self.title = title
#         self.students = []
#
#
# student = Student('Asilbek', 'Tolibov')
# student1 = Student('Sanjar', 'Tolibov')
#
# group = Group('P16')
# group.students = [student, student1]
#
# print(group.students)
# teacher_1 = Teacher('Turonbek', 'Python', 2)
# print(teacher_1)
#
# student_1 = Student('Asilbek', 'Tolibov', 'Navai', 19)
# print(student_1)
#
# fan_1 = Fan('Matematika', 23, 'tabiiy')
# print(fan_1)

# class Subject:
#     def __init__(self, title):
#         self.title = title
#         self.semestr = 1
#
#     def __repr__(self):
#         return f'{self.title}'
#
#
# class Teacher:
#     def __init__(self, first_name, last_name, degree, subject):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.degree = degree
#         self.subject = subject
#
#     def __repr__(self):
#         return f'{self.subject}'
#
#
# teacher_1 = Teacher('Asilbek', 'Tolibov', 'oliy', 'Math')
# print(teacher_1)

# ----------------------------
# 1
# import math
#
#
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def calculate_circle_area(self):
#         return math.pi * self.radius ** 2
#
#     def calculate_circle_peremetr(self):
#         return 2 * math.pi * self.radius
#
#     def __repr__(self):
#         return f"Aylananing uzunligi {self.calculate_circle_area()}, parametri {self.calculate_circle_peremetr()}"
#
#
# radius = float(input("Radiusni kiriting: "))
# circle = Circle(radius)
# print(circle)

# 2
# class Person:
#     def __init__(self, name, country, date_birth):
#         self.name = name
#         self.country = country
#         self.date_birth = date_birth
#
#     def calculate_age(self):
#         return 2023 - self.date_birth
#
#
# person = Person('Asilbek', 'Uzbekistan', 2004)
# print(person.calculate_age())
