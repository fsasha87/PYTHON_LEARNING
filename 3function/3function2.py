print(all({}))  # True
print(any({}))  # False
print(all([1, True, [2, 'name']]))  # True
print(any([1, True, [2, 'name']]))  # True
print(all([1, tuple(), [2, 'name']]))  # False
print(any([1, tuple(), [2, 'name']]))  # True
print(any([0, tuple(), False]))  # False

def square(x):
    return x ** 2
print(square(5))  # 25
my_func = square  # assign a function to a variable
print(my_func(7))  # 49


def apply_func(func, *args):
    results = []
    for arg in args:
        results.append(func(arg))
    return results

print(apply_func(square, 3, 5, 6))  # use square as input argument [9, 25, 36]

def apply_func2(func, a):
    return func(a)
print(apply_func2(square, 5))  # 25


def cube(x):
    return x ** 3

func_mapping = {'square': square, 'cube': cube}  # store functions in a dict
print(func_mapping)  # {'square': <function square at 0x0000022295535580>, 'cube': <function cube at 0x000002229559B100>}
print(func_mapping['square'])  # <function square at 0x00000154841C2290>
print(func_mapping['square'](6))  # 36
print(func_mapping['cube'](6))  # 216

def get_func(func):
    func_mapping2 = {'square': square, 'cube': cube}
    return func_mapping2.get(func, None)  # return function
my_func = get_func('cube')
print(my_func)  # <function cube at 0x00000154841C2680>
print(my_func(7))  # 343


        # types of arguments
def sum_number(a, b):
  print(f"{a}+{b}={a+b}")
sum_number(2, 5)  # 2+5=7

def sub_number(minuend, subtrahend):
  print(f"{minuend}-{subtrahend}={minuend - subtrahend}")

sub_number(1, 3)  # 1-3=-2
sub_number(3, 1)  # 3-1=2

sub_number(minuend=3, subtrahend=1)  # 3 assigned to minuend, 1 – subtrahend  #3-1=2
sub_number(subtrahend=1, minuend=3)  # the same here  #3-1=2

def minus(a, b, c):
    print(a - b - c)
minus(7, 1, 2)  #4
minus(b = 7, c = 1, a = 2)  #-6
minus(7, c = 1, b = 2)  #4


def sum_number(a, b=1): # 1 is a default value for argument b
    print(f"{a}+{b}={a+b}")

def sum(a, b=1): # 1 is a default value for argument b
    print(a+b)
sum(3)  # 4
sum(2, 5)  # 7

        # args, kkwargs
def show_arguments(*args, **kwargs):
  print(f"args: {args}; kwargs: {kwargs}")
show_arguments(1, 'name', arg1=[1, 2, 3], arg2='value')  # args: (1, 'name'); kwargs: {'arg1': [1, 2, 3], 'arg2': 'value'}

def show_arguments2(*args, **kwargs):
  print(args[1:-1])
  print(kwargs['name'])
show_arguments2(1, 'name', 'value', 10, name='arg1', arg2='Tom')  # ('name', 'value')    # arg1

def show_unpacked_arguments(a, b, c, d, e):
  print(a, b, c, d, e)

list_of_args = [1, 2, 'name']
key_value_args = {'e': 'value', 'd': 3}
show_unpacked_arguments (*list_of_args, **key_value_args)  # 1 2 name 3 value

show_unpacked_arguments (1, 2, 'name', e='value', d=3)  # тоже самое: 1 2 name 3 value

def multiple_lines(text, num):
  text = text * num
  print(text)

text = 'external text'
multiple_lines(text, 3) # inside of function we update copied text argument external textexternal textexternal text

students = {'Tom':28, 'John':25}
def test(students):
  new = {'Alan':30,'Dan':27}
  students.update(new)
  print(f'Inside the function: {students}')

test(students)
print(f'Outside the function: {students}')