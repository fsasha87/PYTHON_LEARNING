# encap: class_M: def__init__(self,a,_b,__c):...=> obj => print(obj.a/_b/_M__c)=>obj.a/_b/_M__c=...

class Encapsulation(object):
    def __init__(self, a, b, c):
        self.public = a
        self._protected = b
        self.__private = c


x = Encapsulation(10, 11, 13)
print(x.public)  # 10
print(x._protected)  # 11
x._protected = 23
print(x._protected)  # 23
# print(x.__private)  # AttributeError
print(x._Encapsulation__private)  # 13
x._Encapsulation__private = 76
print(x._Encapsulation__private)  # 76



# encap: class_R: def_init:self__x=x => @property_def_x(self):return self.__x => @x.setter_def_x(self.x):self.__x=x =>
class R:
    def __init__(self, x):
        self.__x = x

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x


r = R(5)
print(r.x)
r.x = 12
print(r.x)



# oop: class=>land;def__init__(self,name,age) => def_show(self) => tom.show; tom.land=FR =>print(Person/tom/tom.__class__.land)
class Person:
    country = "Ukraine"

    def __init__(self, name, age):
        self.name = name
        self.age = 15

    def show_person(self):
        print(f'Person: {self.name}. age: {str(self.age)}')


tom = Person("Tom", 34)
tom.age = 35
tom.show_person()
print(tom.age)
print(tom.name)
tom.country = "Germany"
print(Person.country)  # Ukraine
print(tom.country)  # Germany
print(tom.__class__.country)  # Ukraine

# oop: Person:init(name)+геттер+def__str__=> Employee(P):def_init:(super().__init__(name),company))+str:f"{super().__str__()}/self.name...=> isinstance(o,E)/issubclass(E,P)
class Persona:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def __str__(self):
        return f"Name: {self.__name}"


class Employee(Persona):
    def __init__(self, name, company):
        super().__init__(name)
        self.__company = company

    def __str__(self):
        # return f"{super().__str__()}, company: {self.__company}"
        return f"Name: {self.name}, company: {self.__company}"


tom = Employee("Tom", "Microsoft")
sam = Persona("Sam")
print(sam)
print(tom)
print(isinstance(sam, Employee))
print(issubclass(Employee, Persona))


# oop: class_A: def_f1(self):print(self)=>@classmethod_def_f2(cls):...=>@staticmethod_def_f3():...=>obj.f()=>A.f(obj)
class MyClass:
    def method(self):
        print('instance method', self)

    @classmethod
    def classmethod(cls):
        print('class method', cls)

    @staticmethod
    def staticmethod():
        print('static method')


obj = MyClass()
obj.method()  # instance method <__main__.MyClass object at 0x0000023224A6AF30>
MyClass.method(obj)  # instance method <__main__.MyClass object at 0x0000023224A6AF30>
obj.classmethod()  # class method <class '__main__.MyClass'>
MyClass.classmethod()  # class method <class '__main__.MyClass'>
obj.staticmethod()  # static method
MyClass.staticmethod()  # static method


# poly: class_Dog: def_speak:... => class_Cat: def_speak => def_foo(an):print(an.speak())=> foo(dog/cat)
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"
def animal_sound(animal):
    print(animal.speak())

dog = Dog()
cat = Cat()
animal_sound(dog)  # Выведет: Woof!
animal_sound(cat)  # Выведет: Meow!


#  from_abc_import_ABC,abstractmethod->class_A(ABC):@abstractmethod_def_foo():pass->class_B(A):def_foo():print(...)->b.foo()
from abc import ABC, abstractmethod  # импорт с ABC модуля

class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass

class Dog(Animal):
    def eat(self):
        print('Dog eats')

dog = Dog()
dog.eat()
