
# oop: class=>def__init__(self,...) => def_sey(self) => Person(name,age) => a.name, age=, a.say

class Person:
    def __init__(self, name,  age):
        self.name = name
        self.age = age

    def say_hello(self):
        print("Hello", self.name)

tom = Person("Tom", 22)
print(tom.name)  # Tom
print(tom.age)  # 22
tom.age = 30
print(tom.age)  # 30
tom.say_hello()  # Hello Tom


        # множественное наследование
class Employee:
    def work(self):
        print("Employee works")


class Student:
    def study(self):
        print("Student studies")


class WorkingStudent(Employee, Student):  # Наследование от классов Employee и Student. Класс работающего студента
    pass


tom = WorkingStudent()
tom.work()  # Employee works
tom.study()  # Student studies


print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
# oop: Person+init(__name)+@property_def_name+def_display => Employee(Person):+def_init(super().init,company)+display+work
#   ? if isinstance()
class Persona:

    def __init__(self, name):
        self.__name = name  # имя человека

    @property
    def name(self):
        return self.__name

    def display_info(self):
        print(f"Name: {self.__name}")


class Employee1(Persona):

    def __init__(self, name, company):
        super().__init__(name)
        self.company = company

    def display_info(self):
        super().display_info()
        print(f"Company: {self.company}")

    def work(self):
        print(f"{self.name} works")


tom = Employee1("Tom", "Microsoft")
tom.display_info()  # Name: Tom
                    # Company: Microsoft

