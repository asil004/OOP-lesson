class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    @property
    def name_(self):
        return self.name

    @name_.setter
    def name_(self, value):
        self.name = value

    @name_.deleter
    def name_(self):
        del self.name


sanjar = Student('sanjar', 18)

print(sanjar.name_)
sanjar.name_ = 'asil'
print(sanjar.name_)
del sanjar.name_
print(sanjar.name_)