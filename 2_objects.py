class Student:
    group = 'P16'

    def __new__(cls, first_name, last_name):
        print(f"Creating the {cls.__name__}")
        obj = object.__new__(cls)
        obj.full_name = first_name + last_name
        return obj

    def __init__(self, first_name, last_name):
        print("Init")
        self.first_name = first_name
        self.last_name = last_name

    def get_info(self):
        return self.first_name + ' ' + self.last_name

    @staticmethod
    def to_upper(text):
        return text.upper()

    @staticmethod
    def to_title(text):
        return text.title

    @classmethod
    def update_group(cls, group_name):
        cls.group = group_name


student = Student('Alisher', 'Alisherov')
student_1 = Student('Dilshodbek', 'Yo\'ldoshev')
print(student.group)
Student.update_group('P15')
print(student.group)
