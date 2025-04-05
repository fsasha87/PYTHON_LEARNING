
        # turple кортежы (как списки но нельзя измененить (константа), весят меньше, используются для передачи данных)
my_tuple = (5.5, True, "Some string", (1, 2, 3))
print(my_tuple)  # (5.5, True, 'Some string', (1, 2, 3))
for item in my_tuple:
    print(item)
print(my_tuple.index(5.5))  # 0
print(my_tuple.count(True))  # 1
print(len(my_tuple))  # 4
print(my_tuple[::-1])  # перевернули ((1, 2, 3), 'Some string', True, 5.5)

data_1 = 5, 7, True  # тое создали кортеж
print(data_1)  # (5, 7, True)
data_2 = (5,)
print(data_2)  # (5,)   но (5) выведет int
data_3 = 5,
print(data_3)  # (5,)

data = (6, True, 5.6, 'Hello')
print(data)  # (6, True, 5.6, 'Hello')
print(data[2])  # 5.6
print(data[1:5])  # (True, 5.6, 'Hello')
# data[0] = 5  # TypeError
print(data.count(6))  # 1
print(len(data))  # 4
print(data.index(6)) # 0

list = [5, 7, 8]
print(list)  # [5, 7, 8]
new_data = tuple(list)
print(new_data)  # (5, 7, 8)
word4 = tuple("Hello")
print(word4)  # ('H', 'e', 'l', 'l', 'o')

# packing-unpacking
a, b, c = 40, 56.6, 90
#? print(type((a, b, c)))  # <class 'tuple'>
print(a, b, c)  # 40 56.6 90
(a, b, c) = (40, 56.6, 90)
#? print(type((a, b, c)))  # <class 'tuple'>
print(a, b, c)  # 40 56.6 90
my_tuple = 40, 56.6, 90
print(my_tuple)  # (40, 56.6, 90)
print(*my_tuple)  # 40 56.6 90

# tuple immutable, list mutable
x = (1, 2, 3)
y = (1, 2, 3)
print(x == y)  # true
print(id(x), id(y)) # 2014662830592 2014662830592
print(x is y)  # true
print(hash(x), hash(y))  # 529344067295497451 529344067295497451
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # true
print(id(a), id(b))  # 2014660515904 2014660679040
print(a is b)  # false
# print(hash(a), hash(b))  # TypeError:
some_tuple = (1, 2, 3)
print(hash(some_tuple))  # 529344067295497451
print(id(some_tuple))  # 2306799118848


