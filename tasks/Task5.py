#decor: def_milk(func):def_wr():print+func()+return wr; @milk_def_coffee():print; coffee()

def milk(func):
    def wrapper():
        print("Milk")
        func()
    return wrapper

@milk
def coffee():
    print("arabica")

coffee()   # milk    arabica


#decor: def_milk(func):def_wr():print+func()+return wr; def_coffee():print; coffee=milk(coffee); coffee()

def milk(func):
    def wrapper():
        print("Milk")
        func()
    return wrapper


def coffee():
    print("arabica")


coffee = milk(coffee)
coffee()  # milk    arabica


# decor: dev_f1(func):def_wr(a,b):if_b==0:...return return_func(a,b) return_wr; @f1_def_foo(a,b):return_a/b

def smart_divide(func):
    def wrapper(a, b):
        print(f"let's devide {a} on {b}")
        if b == 0:
            print("dividing on zero impossible")
            return
        return func(a, b)
    return wrapper


@smart_divide
def divide(a, b):
    return a/b


divide(5,2)
divide(5, 0)


# iterator: li->iter1=iter(li)->print(next(iter1)); i=iter('Hello')->while_True:try:next(i)->except_StopIter:break; dict1->i=iter(dict1/dict1.values()/items())
list1 = [25, 739, 48]
custom_iterator = iter(list1)
print(next(custom_iterator))  # 25
print(next(custom_iterator))  # 739
for i in list1:
    print(i)

str1 = "Hello"
iter1 = iter(str1)
while True:
    try:
        print(next(iter1))
    except StopIteration:
        break

dict1 = {'Sasha': 25, 'Alice': 30, 'Ann': 15}
iter1 = iter(dict1.items())
print(next(iter1))
iter2 = iter(dict1.values())
print(next(iter2))
iter3 = iter(dict1.keys())
print(next(iter3))


# lambda:cube=la_a:a**3;s.upper;[(),()].sort(key=la_x:x[1]);map(la_i:i*2,li);list(filter(ls_i:i%2,li));reduce(la:x+y,li)
cube = lambda a: a ** 3
print(cube(3))

sum_lambda = lambda a, b: a + b
print(sum_lambda(1, 3))  # 4

# func2 = lambda: print("Hello")
func2 = lambda: "Hello".upper()
print(func2())

people = [("Alice", 25), ("Charlie", 30), ("Bob", 20)]  # список кортежей
people.sort(key=lambda x: x[1])
print(people)  # [('Bob', 20), ('Alice', 25), ('Charlie', 30)]

nums = [48, 6, 9, 21, 1]
square_all = map(lambda num: num * 2, nums)
print(square_all)  # map returns an iterable object <map object at 0x000002951E273CA0>
print(list(square_all))  # [96, 12, 18, 42, 2]

nums = [48, 9, 12, 0, -1]
print(list(filter(lambda num: num % 2 == 0, nums)))  # [48, 12, 0]

print(list(filter(None, nums)))  # [48, 9, 12, -1]  # 0 was removed ложные ел-ты удаляются

from functools import reduce
nums = [1, 2, 3, 4, 5]
print(reduce(lambda x, y: x + y, nums))  # 15  ((((1+2)+3)+4)+5)  import functools


# list_comprehension: l2=[i.upper()_for_i_in_list]; filter=[n_for_n_in_li_if...]/forin:if...:l2.append(i)
words = ["apple", "banana", "cherry"]
uppercase_words = [word.upper() for word in words]
print(uppercase_words)  # Вывод: ['APPLE', 'BANANA', 'CHERRY']
list4 = [4, 5, 6, 9]
list7 = [n for n in list4 if n%2==0]
print(list7)
list5 = []
for i in list4:
    if i%2==0:
        list5.append(i)
print(list5)


# generator_expression: g=(n*2 for n in range(5))->print(type())->print(list(g)); LC: l2=[n*2_for_n_in_range(10)]
list6 = [n*2 for n in range(5)]  # List comprehension
print(type(list6))  # <class 'list'>
gen = (n*2 for n in range(5))  # Generator expression
print(type(gen))  # <class 'generator'>
print(list(gen))  # [0, 2, 4, 6, 8]



# zip: li1,li2->z=[u*v for u,v in zip(li1,li2)]; str1,li->print(zip(str1,li)); x=enumerate(str/li)->print(dict(x))
vec1 = [3, 10, 2]
vec2 = [-20, 5, 1]
dot_mul = [u*v for u, v in zip(vec1, vec2)]
print(dot_mul)  # [-60, 50, 2]
s = 'abc'
t = [10, 20, 30]
r = zip(s, t)
print(dict(zip(s, t)))
print(list(r))  # [('a', 10), ('b', 20), ('c', 30)]
print(dict(r))  # {'a': 10, 'b': 20, 'c': 30}
print(type(r))  # <class 'zip'>
y = enumerate(s)
print(type(y))  # <class 'enumerate'>
print(dict(y))  # {0: 'a', 1: 'b', 2: 'c'}

