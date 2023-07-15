class Person:
    def __init__(self, first_name, last_name, age, passport, addresss, birth_date, where_born, pnfl):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.passport = passport
        self.address = addresss
        self.birth_date = birth_date
        self.where_born = where_born
        self.pnfl = pnfl

    @property
    def first_name_(self):
        return self.first_name

    @first_name_.setter
    def first_name_(self, val):
        self.first_name = val

    @property
    def last_name_(self):
        return self.last_name

    @last_name_.setter
    def last_name_(self, val):
        self.last_name = val

    @property
    def full_name_(self):
        return self.first_name + ' ' + self.last_name

    @full_name_.setter
    def full_name_(self, val_1, val_2):
        self.first_name = val_1
        self.last_name = val_2

    @property
    def age_(self):
        return self.age

    @age_.setter
    def age_(self, val):
        self.age = val

    @property
    def pnfl_(self):
        return self.pnfl

    @pnfl_.setter
    def pnfl_(self, val):
        self.pnfl = val


# Child classes
# Student
class Student(Person):
    def __init__(self, first_name, last_name, age, passport, addresss, birth_date, where_born, pnfl, grade, study_where,
                 entered_date, finished_date):
        super().__init__(first_name, last_name, age, passport, addresss, birth_date, where_born, pnfl)
        self.grade = grade
        self.study_where = study_where
        self.entered_date = entered_date
        self.finished_date = finished_date

    @property
    def grade_(self):
        return self.grade

    @grade_.setter
    def grade_(self, val):
        self.grade = val

    @property
    def study_where_(self):
        return self.study_where

    @study_where_.setter
    def study_where_(self, val):
        self.study_where = val

    @property
    def entered_date_(self):
        return self.entered_date

    @entered_date_.setter
    def entered_date_(self, val):
        self.entered_date = val

    @property
    def finished_date_(self):
        return self.finished_date

    @finished_date_.setter
    def finished_date_(self, val):
        self.finished_date = val

    def get_difference(self):
        return self.finished_date - self.entered_date


# class Teacher
class Teacher(Person):
    def __init__(self, first_name, last_name, age, passport, addresss, birth_date, where_born, pnfl, subjects: list,
                 degree, salary, experience, languages: list, certifications: list):
        super().__init__(first_name, last_name, age, passport, addresss, birth_date, where_born, pnfl)
        self.subjects = subjects
        self.degree = degree
        self.salary = salary
        self.experince = experience
        self.languages = languages
        self.certifications = certifications

    @property
    def subjects_(self):
        return self.subjects

    @subjects_.setter
    def subjects_(self, val):
        self.subjects.clear()
        self.subjects.extend(val)

    @property
    def degree_(self):
        return self.degree

    @degree_.setter
    def degree_(self, val):
        self.degree = val

    @property
    def salary_(self):
        return self.salary

    @salary_.setter
    def salary_(self, val):
        self.salary = val

    @property
    def experince_(self):
        return self.experince

    @experince_.setter
    def experince_(self, val):
        self.experince = val

    @property
    def languages_(self):
        return self.languages

    @languages_.setter
    def languages_(self, val):
        self.languages.clear()
        self.languages.extend(val)

    @property
    def certifications_(self):
        return self.certifications

    @certifications_.setter
    def certifications_(self, val):
        self.certifications.clear()
        self.certifications.extend(val)

    # Instace methods
    def add_subject(self, val):
        self.subjects.append(val)

    def remove_subject(self, val):
        self.subjects.remove(val)

    def add_language(self, val):
        self.languages.append(val)

    def remove_language(self, val):
        self.languages.remove(val)

    def add_certification(self, val):
        self.certifications.append(val)

    def remove_certification(self, val):
        self.certifications.remove(val)


# class Abt
class Abt(Person):
    def __init__(self, first_name, last_name, age, passport, addresss, birth_date, where_born, pnfl, subjects: list):
        super().__init__(first_name, last_name, age, passport, addresss, birth_date, where_born, pnfl)
        self.subjects = subjects

    def get_subjects(self):
        return self.subjects

    def add_subjects(self, val):
        self.subjects.append(val)


person_1 = Person('Asilbek', 'Tolibov', 19, 'AD1234567', 'Chilonzor', 2004, 'Navai', 12345678998287)
student_1 = Student('Asilbek', 'Tolibov', 19, 'AD1234567', 'Chilonzor', 2004, 'Navai', 12345678998287, 1, 'TATU', 2022,
                    2026)
teacher_1 = Teacher('Turonbek', 'Kuzibayev', 23, 'AD22342342', 'Tashkent', 2000, 'Uzbekistan', 12324234287973,
                    ['pytohn', 'rust', 'php'], 'middle', 999, 2, ['uzbek', 'english', 'russia'], 'PDP teacher')
abt_1 = Abt('Asilbek', 'Tolibov', 19, 'Ad2342342', 'Chilonzor', 2004, 'Navai', 12438726192837,
            ['english', 'math', 'physics'])

# print(student_1.finished_date_)
teacher_1.add_language('france')
print(teacher_1.languages_)
teacher_1.remove_language('france')
print(teacher_1.languages_)
print(abt_1.get_subjects())
