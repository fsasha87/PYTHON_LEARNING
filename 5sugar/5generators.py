# list generators
list1 = [1, 2, 3, 4, 5]
list2 = [n**2 for n in list1]
print(list2)  # Вывод: [1, 4, 9, 16, 25]
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
evens = [n for n in numbers if n % 2 == 0]
print(evens)  # Вывод: [2, 4, 6, 8]
words = ["apple", "banana", "cherry"]
uppercase_words = [word.upper() for word in words]
print(uppercase_words)  # Вывод: ['APPLE', 'BANANA', 'CHERRY']

# n = int(input("Input integer number: "))
# even_numbers = []
# for i in range(1, n):
#     if not i % 2:
#         even_numbers.append(i)
# print(even_numbers)  # [2, 4, 6, 8]
#
# even_numbers = [i for i in range(1, n) if not i % 2]  # тоже самое List Comprehensions
# print(even_numbers)  # [2, 4, 6, 8]


# n = int(input("Enter length: "))
# user_list = []
# i = 0
# while i < n:
#     string = "Enter element #" + str(i + 1) + ": "
#     user_list.append(input(string))
#     i += 1
# print(user_list)

# # list task: array of even numbers in entered number
# n = int(input("Input integer number: "))
# even_numbers = []
# for i in range(1, n):
#     if not i % 2:
#         even_numbers.append(i)
# print(even_numbers) # [2, 4, 6, 8, 10]

# # list task (2nd variant): array of even numbers in entered number
# n = int(input("Input integer number: "))
# even_numbers = [i for i in range(1, n) if not i % 2]
# print(even_numbers)

    #  <class 'enumerate'>
x = ['apple', 'banana', 'cherry']
y = enumerate(x)
print(list(y))  # [(0, 'apple'), (1, 'banana'), (2, 'cherry')]
print(type(y))  #  <class 'enumerate'>

# zip: li1,li2->z=[u*v for u,v in zip(li1,li2)]; str1,li->print(zip(str1,li))
vec1 = [3, 10, 2]
vec2 = [-20, 5, 1]
dot_mul = [u*v for u, v in zip(vec1, vec2)]
print(dot_mul)  # [-60, 50, 2]
dot_prod = sum(dot_mul)
print(dot_prod)  # -8

s = 'abc'
t = [10, 20, 30]
r = zip(s, t)
print(dict(zip(s, t)))
print(list(r))  # [('a', 10), ('b', 20), ('c', 30)]
print(dict(r))  # {'a': 10, 'b': 20, 'c': 30}
print(type(r))  # <class 'zip'>

s = 'abc'
t = (10, 20, 30, 40, 50)
u = (-2, 9, -90, 999)
r = zip(s, t, u)
print(list(r))  # [('a', 10, -2), ('b', 20, 9), ('c', 30, -90)]

# from intertools import zip_longest
# k = zip_longest(s, t, u)
# print(list(k))  # [('a', 10, -2), ('b', 20, 9), ('c', 30, -90), (None, 40, 99), (None, 50, None)]



# generator_expression: g=(n*2 for n in range(5))->print(type())->print(list(g)); l2=[n*2_for_n_in_range(10)]
list6 = [n*2 for n in range(5)]  # List comprehension
print(type(list6))  # <class 'list'>
gen = (n*2 for n in range(5))  # Generator expression
print(type(gen))  # <class 'generator'>
print(list(gen))  # [0, 2, 4, 6, 8]
for i in gen:
    print(i)

a = sum(x*x for x in range(1,10))
print(a)  # 285

g = (x*x for x in range(1,10))
print(type(g))  # <class 'generator'>
print(list(g))  # [1, 4, 9, 16, 25, 36, 49, 64, 81]

def my_generator():
    print("Inside my generator")
    yield 'a'
    yield 'b'
    yield 'c'

print(my_generator())

for el in my_generator():
    print(el)
