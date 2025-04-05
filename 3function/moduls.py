import platform
import time

# ВСТРОЕННІЕ МОДУЛИ
time.sleep(3)  # заморозили программу на 3с
print("Hello")

import datetime as d  # присвоили псевдоним
print(d.datetime.now())  # 2024-08-07 19:13:15.343294
print(d.datetime.now().time())  # 19:14:14.428382
print(d.datetime.now().date())  # 2024-08-07
print(d.datetime.now().date().weekday())  # 2

import sys, os
print(sys.path)  # путь к текущему проекту
print(os.name)  # nt (виндовс)
print(platform.system())  # Windows

from math import sqrt, ceil  # импорт одной функции из модуля
print(ceil(sqrt(100)))  # 10 - корень+округлили


        # пакетный менеджер pip  pypi.org
        # установить библиотеку cowsay: в теминале прописаь pip install cowsay
        # результат: Successfully installed cowsay-6.1 и появилась в папке venv\lib\cowsay
import cowsay
cowsay.cow('Hello')  # Hello cow


# module: globals()/dir() => a=10/list1/d_foo()/import_math/from_math_i_sqrt/from_math_i_* => print(dir()/globals())

print(globals())
print(dir())
a = 5

import math

print(math.floor(2.5))  #2

list1 = [1, 3, 5]
print(dir())

def foo():
    pass

# from math import *
print(dir())
print("locals")
print(locals())
print("globals")
print(globals())


        # импортируем свой модуль целиком
import modulMy  # при загрузке модуля выведется Hello from modulMy.py
print(modulMy.surname)  # Obama
modulMy.hello()  # Hello Obama
print(modulMy.__name__)  # modulMy

from modulMy import hello as he
print(he())  # Hello Obama    None








