# Parent class
# Class Animal
class Animal:
    def __init__(self, name, age, type, sleep):
        self.name = name
        self.age = age
        self.type = type
        self.sleep = sleep

    def display(self):
        return f'Ismi:{self.name}, yoshi:{self.age}, turi:{self.type}.'

    def get_sleep(self):
        return f'{self.name} {self.sleep} soat uxlidi.'


# Child class
# class Cat
class Cat(Animal):
    def __init__(self, name, age, type, sleep, color, eat):
        super().__init__(name, age, type, sleep)
        self.color = color
        self.eat = eat

    def can_sleep(self):
        return True

    def can_myav(self):
        return f'Myov'


# class Dog
class Dog(Animal):
    def __init__(self, name, age, type, sleep, color, eat):
        super().__init__(name, age, type, sleep)
        self.color = color
        self.eat = eat

    def can_wow(self):
        return f'WOW'

    def can_jump(self):
        return True

    def can_beat(self):
        return True


# class Cow
class Cow(Animal):
    def __init__(self, name, age, type, sleep, color, eat):
        super().__init__(name, age, type, sleep)
        self.color = color
        self.eat = eat

    def can_eat(self):
        return True

    def can_give_milk(self):
        return f'3 litr'

    def can_moa(self):
        return f'Moa'


# class Horse
class Horse(Animal):
    def __init__(self, name, age, type, sleep, color, eat, speed):
        super().__init__(name, age, type, sleep)
        self.color = color
        self.eat = eat
        self.speed = speed

    @property
    def speed_(self):
        return self.speed

    @speed_.setter
    def speed_(self, val):
        self.speed = val

    @speed_.deleter
    def speed_(self):
        del self.speed

    @property
    def color_(self):
        return self.color

    @color_.setter
    def color_(self, val):
        self.color = val

    def get_eat(self):
        return True


# class Tiger
class Tiger(Animal):
    def __init__(self, name, age, type, sleep, color, eat, speed):
        super().__init__(name, age, type, sleep)
        self.color = color
        self.eat = eat
        self.speed = speed

    @property
    def speed_(self):
        return self.speed

    @speed_.setter
    def speed_(self, val):
        self.speed = val

    @speed_.deleter
    def speed_(self):
        del self.speed

    def get_speed_thirsty(self):
        return self.speed - 25


# class Rabit
class Rabit(Animal):
    def __init__(self, name, age, type, sleep, color, eat):
        super().__init__(name, age, type, sleep)
        self.color = color
        self.eat = eat

    def get_color(self):
        return self.color

    def can_eat(self):
        return True

    def can_jump(self):
        return True


# class Jaguar
class Jaguar(Animal):
    def __init__(self, name, age, type, sleep, color, eat, speed):
        super().__init__(name, age, type, sleep)
        self.color = color
        self.eat = eat
        self.speed = speed

    def get_color(self):
        return self.color

    def del_color(self):
        del self.color
        return f'Rangi o\'chirildi'

    def set_color(self, val):
        self.color = val


animal_1 = Animal('Akamaru', 7, 'it', 7)
print(animal_1.display())
print(animal_1.get_sleep())
