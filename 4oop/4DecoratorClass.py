# декораторы методы класса
class Person:
    origin_country = "USA"

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def speak(self, words):
        print(f"{self.name} speaks: {words}")

    @classmethod  # встроенный декоратор
    def change_origin_country(cls, new_country):
        cls.origin_country = new_country
        print(cls.origin_country)

Person.change_origin_country("Ukraine")  # Ukraine


# декоратор статический класс
class Person2:
    origin_country = "USA"

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    @classmethod
    def change_origin_country(cls, new_country):
        cls.origin_country = new_country
        print(cls.origin_country)

    @staticmethod  # метод помечен встроенным декоратором, который сообщает Python, что этот метод является статическим.
    def is_adult(age):
        return age > 18

print(Person2.is_adult(19))  # True


# Property
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def email(self):
        return f"{self.first_name}.{self.last_name}@email.com"

obj = Person("Alex", "Johnson")
print(obj.email)  # 'Alex.Johnson@email.com'
obj.first_name = "Bob"
print(obj.email)  # 'Bob.Johnson@email.com'

# abstract class
from abc import ABC, abstractmethod  # импорт с ABC модуля
class Animal(ABC):
    @abstractmethod
    def eat(self):
        raise NotImplementedError("You have to implement eat() method")

class Dog(Animal):

    def eat(self):
        print("Dog is eating!")

obj = Dog()
obj.eat()  # Dog is eating!
