import webbrowser

def validator(func):
    def wrapper(url):
        print("Это текст до функции")
        if "." in url:
            func(url)
        else:
            print("неверный url")
        print("Это текст после функции")
    return wrapper

@validator
def open_url1(url):
    webbrowser.open(url)

# open_url1("http:/itproger.com")

#  декоратор помогает выполнять код до и после функции


#         # nested decorator without decorator syntax
def milk(func):
    def wrapper():
        print("hot milk")
        func()
    return wrapper


def sugar(func):
    def wrapper():
        print("sugar")
        func()
    return wrapper


def coffee(variety="arabica"):
    print(variety)


coffee = sugar(milk(coffee))
coffee()


        # with decorator syntax
def milk(func):
    def wrapper():
        print("hot milk")
        func()
    return wrapper
def sugar(func):
    def wrapper():
        print("sugar")
        func()
    return wrapper
@sugar
# @milk
def coffee(variety="arabica"):
    print(variety)
coffee()   # sugar  hot milk    arabica


def call_counter(origin_function):
    count = 0
    def wrapper(func_arg):
        nonlocal count
        count += 1
        print(f'call number is {count}')
        return origin_function(func_arg)
    return wrapper

@call_counter  # аналог: say_hello = call_counter(say_hello)
def say_hello(guest_name):
    print(f'Hello, {guest_name}')

say_hello('John Doe')  # call number is 1    Hello, John Doe
say_hello('Marilyn Monroe')  # call number is 2    Hello, Marilyn Monroe


def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner
def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner

@star
@percent
def printer(msg):
    print(msg)


printer("Hello")


@percent
@star
def printer(msg):
    print(msg)
printer("Hello")


def smart_divide(func):
    def inner(a,b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! Can not divide")
            return
        return func(a, b)
    return inner


@smart_divide
def divide(a, b):
    return a/b

divide(2,5)
divide(2,0)