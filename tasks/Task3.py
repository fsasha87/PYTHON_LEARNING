# func: pass=>minus(b=,a=)=>d_suma(arg=)=f1(2)=>func(square/suma,*a):forin_a->list; d_show(a*,k**)=>d_show(a,...)=>show([],{})
def test_func():
    pass  # ничего не произойдет

def minus(a, b, c):
    print(a - b - c)
minus(7, 1, 2)  # 4
minus(b=7, c=1, a=2)  # -6
minus(7, c=1, b=2)  # 4


def sum1(a, b=4):
    return a + b
print(sum1(5, 6))  # 11
func5 = sum1  # assign a function to a variable
print(type(func5))  # <class 'function'>
print(func5(3))  # 7
print(func5(3, 5))  # 8

def square(x):
    return x ** 2
def foo(func1, *a):
    result = []
    for i in a:
        result.append(func1(i))
    return result
print(foo(square, 2, 4))  # [4, 16]
print(foo(sum1, 2, 4, 6, 8))  # [6, 8, 10, 12]


def show_arguments(*a, **k):
    print(f"args:{a}; kwargs:{k}")
show_arguments(5, True, "Hello", 6.2, k=[1, 2, 3], b=8, c=False)  # args:(5, True, 'Hello', 6.2); kwargs:{'k': [1, 2, 3], 'b': 8, 'c': False}


def show_unpacked_arguments(a, b, c, d):
    print(a, b, c, d)
i = [1, "Hello"]
j = {'c': 'Hi', 'd': 0}
show_unpacked_arguments(*i, **j)  # 1 Hello Hi 0

def show_unpacked_arguments(a, b, c, d, e):
  print(a, b, c, d, e)
i = [1, 2, 'name']
j = {'e': 'value', 'd': 3}
show_unpacked_arguments(*i, **j)  # 1 2 name 3 value


# namespaces: LEG_name(create-print) => global => nonlocal; globals(); globals()['a']; def_sum:...locals()
name = 'global'
def a():
    # global name
    name = 'enclosing'
    def b():
        # nonlocal name
        name = 'local'
        print('l:', name)  # l:local  НО ПРИ nonlocal: e:local
    b()
    print("e:", name)  # e:enclosing
a()
print('g:', name)  # g:global  НО ПРИ global g:enclosing


a = 'Hello'
print(globals())  # выведет глобальные объекты, в т.ч. переенные класса
print(globals()['a'])
globals()['a'] = "Hello Amigo"
print(globals()['a'])

def sum_numbers(x, y):
    res = x + y
    print(locals())
    return res
sum_numbers(2,5)  # {'x': 2, 'y': 5, 'res': 7}


# mymodule.py: print();d_say():__name__;if__name__=='__main__':print;say; mmc.py: i_mm;mm.say();print(__name__/mm.__name__)
# mymodule.py:
print('Hello from MM')
def say_hello():
    print("Hello", __name__)
# if __name__ == '__main__':
#     print('Only from MM')
#     say_hello()
#mmc.py:
#import myModule
# myModule.say_hello()
# print(__name__)
# print(myModule.__name__)



# try:5/o=>except_Error=>else=>finally; try:int(input) if<0:raise_ValueError => except_Valueerror_as_ve: pr(ve)
try:
    x = 5 / 0
except ZeroDivisionError:
    print("Деление на ноль")
else:
    print("try is done")
finally:
    print("Finally")

try:
    a = int(input("Enter a positive integer: "))
    if a <= 0:
        raise ValueError("That is not a positive number!")
except ValueError as ve:
    print(ve)


# class_CustomError(Exception):init(data)=>try:n=int(input(""))=>if n<0:raise CustomError("")=> except_CE_as_e:print(e)
class CustomError(Exception):
    def __init__(self, data):
        self.data = data


try:
    number = int(input("Enter number"))
    if number < 0:
        raise CustomError("Negative value")
except CustomError as e:
    print(e.data)
    print(e)


# magic: person(name,age)->def_str_:return_f'{s.name}'->def_eq_{s,o}:if_isistance(o,Person):return_s.name=o.name_return_False->def_hash_:return_hash(s.name,s.age)
# ->p1('A')=p2('A')=p3->pr(p1==p2)->pr(p1._eq_(p2))->pr(id(p1)=id(p3))->pr(hash(p1)=hash(p2))->#pr(o._str_()/_repr_/_dict_/_dir_/_class_/_module_/_doc_/_hash_)->str/repr/dir/hash(o)
class Person:
    """
    Docstring of person obj
    """

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name}, age {self.age}'

    def __repr__(self):
        return f'Person(name={self.name!r}, age={self.age!r})'

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.name == other.name and self.age == other.age
        return False

    def __hash__(self):
        return hash((self.name, self.age))


person1 = Person("Sasha", 37)
person2 = Person("Alice", 30)
person3 = Person("Sasha", 37)
person4 = person1
print(person1 == person2)  # False
print(person1 == person3)  # True
print(person1 == person4)  # True
print('eq', person1.__eq__(person2))  # False
print('eq', person1.__eq__(person3))  # True
print('eq', person1.__eq__(person4))  # True
print(id(person1) == id(person2))  # False
print(id(person1) == id(person3))  # False
print(id(person1) == id(person4))  # True
print(hash(person1) == hash(person4))  # True
print(hash(person1) == hash(person3))  # True
print(hash(person1) == hash(person2))  # False

print('str:', person1.__str__())
print('repr:', person1.__repr__())
print('dict', person1.__dict__)  # dict {'name': 'Sasha'}
print('dir', person1.__dir__())  # dir ['name', '__module__', '__init__',...
print('class:', person1.__class__)  # class: <class '__main__.Person'>
print('module:', person1.__module__)  # module: __main__
print('doc:', person1.__doc__)  # Docstring of person obj
print('hash:', person1.__hash__())  # hash: 82733206205

print('STR:', str(person1))
print('REPR:', repr(person1))
print('HASH:', hash(person1))  # HASH: 82733206205
print('id:', id(person1))  # id: 2245969292240
print('DIR:', dir(person1))   # DIR: ['__class__', '__delattr__', '__dict__'
