# functions - минипрограммы

def func():
    pass  # ничего не произойдет

def func2():
    print("Hello", end="")
    print("!")

func2()  # Hello!

def func3(word):
    print(word)

func3("Amigo")
func3(5)
func3(True)

def summa(a, b):
    res = a + b
    print("Result:", res)

summa(5, 7)  # Result: 12
summa("H", "i")  # Result: Hi
res = summa(5.5, 7.5)
print(res)  # None

def summa2(a, b):
    return a + b

res = summa2(4, 6)
print(res)  # 10

print(summa2('j', 'a'))  # ja


def minimal(l):
    min_number = l[0]
    for el in l:
        if el < min_number:
            min_number = el
    return min_number

nums1 = [5, 7, 9, 4]
min1 = minimal(nums1)
nums2 = [5.4, 7.2, 2.3, 2.1, 9.4, 4.2]
min2 = minimal(nums2)

if min1 < min2:
    print(min1)
else:
    print(min2)


        # namespaces
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


x = 10
def y():
    global x
    x = "text"
    # globals()['x'] = "some"  # 2 сп
y()
print(x)  # text

x2 = 10
def y2():
    x2 = 'Enclosing'
    print (x2)  # Enclosing
    def z():
        nonlocal x2
        x2 = 3.14
        print(f'local {x2 = }')
    z()  # local x2 = 3.14
    print(f'enclosing {x2 = }')
y2()  # enclosing x2 = 3.14


print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")


def outer():  # внешняя функция
    n = 5
    def inner():  # вложенная функция
        nonlocal n  # указываем, что n - это переменная из окружающей функции
        n = 25
        print(n)
    inner()  # 25
    print(n)
outer()  # 25


        # closure
def outer_function(msg):
    message = msg
    def inner_function():
        print(message)
    return inner_function
my_function = outer_function('Hi!')
my_function()  # Hi!

def outer():  # внешняя функция
    n = 5  # лексическое окружение - локальная переменная
    def inner():  # локальная функция
        nonlocal n
        n += 1  # операции с лексическим окружением
        print(n)
    return inner
fn = outer()  # fn = inner, так как функция outer возвращает функцию inner
# вызываем внутреннюю функцию inner
fn()  # 6
fn()  # 7
fn()  # 8


        # локальная (внутренняя) функция
def print_messages():
    # определение локальных функций
    def say_hello(): print("Hello")
    # вызов локальных функций
    say_hello()

# Вызов функции print_messages
print_messages()


def print_person(name, age):
    if age > 120 or age < 1:
        print("Invalid age")
        return
    print(f"Name: {name}  Age: {age}")


print_person("Tom", 22)
print_person("Bob", -102)

# Функция как тип
def sum(a, b): return a + b
operation = sum
print(operation(5, 6))  # 11

# Функция как параметр функции
def do_operation(a, b, operation):
    result = operation(a, b)
    print(f"result = {result}")
def sum(a, b): return a + b
do_operation(5, 4, sum)  # result = 9


def sum(a, b): return a + b


def subtract(a, b): return a - b


def multiply(a, b): return a * b


def select_operation(choice):
    if choice == 1:
        return sum
    elif choice == 2:
        return subtract
    else:
        return multiply

# Функция как результат функции
operation = select_operation(1)  # operation = sum
print(operation(10, 6))  # 16
operation = select_operation(2)  # operation = subtract
print(operation(10, 6))  # 4
operation = select_operation(3)  # operation = multiply
print(operation(10, 6))  # 60

# с лямбдой
def do_operation(a, b, operation):
    result = operation(a, b)
    print(f"result = {result}")
do_operation(5, 4, lambda a, b: a + b)  # result = 9