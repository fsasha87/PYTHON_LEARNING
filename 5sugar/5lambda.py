        # anonym function (lambda выражение) - функция в одну строчку
sum_lambda = lambda a, b: a + b
print(sum_lambda(1, 3))  # 4

def sum_number(a, b):
    return a + b
print(sum_number(1, 3))  # 4 аналог без лямбды

# func2 = lambda: print("Hello")
func2 = lambda: "Hello".upper()
print(func2())

people = [("Alice", 25), ("Bob", 30), ("Charlie", 20)]  # список кортежей
people.sort(key=lambda x: x[1])
print(people)  # [('Charlie', 20), ('Alice', 25), ('Bob', 30)]

nums = [48, 6, 9, 21, 1]
square_all = map(lambda num: num * 2, nums)
print(square_all)  # map returns an iterable object <map object at 0x000002951E273CA0>
print(list(square_all))  # [96, 12, 18, 42, 2]

import random
names = ['Sam', 'Don', 'Sid']
code_names = ['Iron', 'Batman', 'Capitan']
secret_names = map(lambda x: random.choice(code_names), names)
print("========>", list(secret_names))

nums = [48, 9, 12, 0, -1]
print(list(filter(lambda num: num % 2 == 0, nums)))  # [48, 12, 0]
print(list(filter(None, nums)))  # [48, 9, 12, -1]  # 0 was removed ложные ел-ты удаляются

from functools import reduce
nums = [1, 2, 3, 4, 5]
print(reduce(lambda x, y: x+y, nums))  # 15  ((((1+2)+3)+4)+5)

print("max:", reduce(lambda a, b: a if (a>b) else b, nums))  # max: 5
