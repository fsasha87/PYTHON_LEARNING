import math
from math import sqrt
import random

        # Print:
a, b, c = 7.5, 'Text1', True
print(a)  # 7.5
print(b)  # Text1
print(c)  # True

PI = 3.14
print(PI)


print("Hello")
print("str1" + "str2")  # str1str2
print("str1", "str2")  # str1 str2
print("string1", end=" ")
print("string2")  # string1 string2
print("Hi" * 2)  # HiHi
print("Result:", 7, True, sep="")  # Result:7True
print("Not this \rOnly \tthis line \"!\" \nnew line")  # Only 	this line "!"    new line
# str1 = "Hello"
# del str1
# print(str1)  # NameError
age = 33
print("Me " + str(age))
print("Me {}".format(age))
print(f"Me {age}")
name = "Filip"
location = "UK"
message = "Hello, my name is " + name + ", I am " + str(age) + ", I am from " + location
print(message)  # Hello, my name is Filip, I am 33, I am from UK
message2 = "Hello, my name is {}, I am {}, I am from {}".format(name, age, location)
print(message2)  # Hello, my name is Filip, I am 33, I am from UK
message3 = f"Hello, my name is {name}, I am {age}, I am from {location}"
print(message3)  # Hello, my name is Filip, I am 33, I am from UK

name = 'John'
print("Hello, %s!" % name)
name = "John "
age = 23
print("%s is %d years old." % (name, age))

name = "John"
age = 23
salary = 999.99
print("%s is %d years old. Your sallary is %.3f $" % (name, age, salary))
print("{}, {} and {}".format('John', 'Bill', 'Sean'))  # John, Bill and Sean
print("{1}, {0} and {2}".format('John', 'Bill', 'Sean'))  # Bill, John and Sean
print("{s}, {b} and {j}".format(j='John',b='Bill',s='Sean'))  # Sean, Bill and John

#  scanner
# a = input("Enter your age: ")
# print("Your age:", a)
# num5 = int(input("enter 1st number:"))
# num6 = int(input("enter 2nd number:"))
# print("Result:", num5 * num6)


          # string
word1 = "itproger"
print(word1[1])
print(len(word1))
print(word1.count('r'))
print(word1.upper())
print(word1.isupper())
print(word1.islower())
print(word1.capitalize())  # 1й символ с заглавной, остальные в нижнем
print(word1.find('p'))  # индекс совпадения

word2 = 'Football, basketball, skate'
hobby = word2.split(', ')
print(hobby)  # ['Football', 'basketball', 'skate']
print(hobby[1])  # basketball
for i in range(len(hobby)):
    hobby[i] = hobby[i].capitalize()
    print(hobby[i])  # Football     Basketball      Skate
result = ", ".join(hobby)
print(result)  # Football, Basketball, Skate

letters = "a b c".split(' ')
print(letters)  # ['a', 'b', 'c']
str = ", ".join(letters).upper()  # A, B, C
print(str)
print(str.isalpha())

# Slice: str/list
word3 = 'Football'
print(word3[0])  # F
print(word3[slice(0, 4)])  # el
print(word3[0:4])  # Foot - срез
print(word3[4:])  # ball
print(word3[4:-2])  # ba
print(word3[0:-1:2])  #Fobl
print(word3[::])  # Football
print(word3[::-1])  # llabtooF
print(word3[::-2])  # lato
list = [6, 4, "Stroka", True, 6.5]
print(list[2:])  # ['Stroka', True, 6.5]
print(list[2:5:2])  # ['Stroka', 6.5]
print(list[::])  # [6, 4, 'Stroka', True, 6.5] вывел все
print(list[::-1])  # [6.5, True, 'Stroka', 4, 6]  перевернули список
print(list[::-2])  # [6.5, 'Stroka', 6] перевернули с пропуском через 1

        # operators
print(5/2)  # 2.5
print(5//2)  # 2
print(5%2)  # 1
print(5**2)  # 25
a = 5
a += 3
print(a)  # 8
print(min(0, -1, 5))  # -1
print(pow(5, 3))  # 125
print(round(5 / 3))  # 2
print(math.sqrt(4))  # 2.0  import math
print(random.randint(1, 10))  # 9   import random
print(sqrt(9))  # 3.0
str_num = "5"
print(3 + int(str_num))  # 8
# print(str_num + str(3))  # 53
# print(str_num, str(3))  # 5 3
# boolean and comparison operators
result = 3 >= 1 and 10 < 20
print(result)  # True
result = 3 >= 1 or 10 > 20
print(result)  # True
a = True
print(not a)  # False
k = "a"
j = "a"
print(k==j)  # True

        # data types
a = 10
b = 10.5
c = 8+3j
print(type(a))  # <class 'int'>
print(type(b))  # <class 'float'>
print(type(c))  # <class 'complex'>
x = 5
x = float(x)  # 5.0
print(x)
x = 5.5
x = int(x)  # 5
print(x)
x = 5
x = complex(x)  # (5+0j)
print(x)
my_str = "This is string!"
print(type(my_str))  # <class 'str'>
some_list = [1, 2.5, True, "Str in a list"]
print(type(some_list))  # <class 'list'>
my_tuple = (22, 89, True, False)
print(type(my_tuple))  # <class 'tuple'>
our_set = {4, 3, 6.6, "Hello"}
print(type(our_set))  # <class 'set'>
another_dict = {"message": "Hi!", 33: True}
print(type(another_dict))  # <class 'dict'>
def foo():
    pass
class Bar:
    pass
class Lemon:
    pass
print(type(foo))  # <class 'function'>
print(type(Bar))  # <class 'type'>
print(type(Lemon))  # <class 'type'>

# изменился id
a = 1
print(id(a))  # 140737452886456
a += 2
print(id(a))  # 140737452886520

# не изменился id
my_list = [1, 2]
print(id(my_list))  # 3228291551488 list-mutable
my_list.append(3)
print(id(my_list))  # 3228291551488

a1 = 2
a2 = 2
print(a1 is a2)  # True
print(a1 == a2)  # True

b1 = "Hello"
b2 = "Hello"
print(b1 is b2)  # True
print(b1 == b2)  # True

c1 = [1, 2, 3]
c2 = [1, 2, 3]
print(c1 is c2)  # False
print(id(c1) == id(c2))  # False
print(c1 == c2)  # True

d1 = [1, 2, 3]
d2 = d1
print(d1 is d2)  # True
print(d1 == d2)  # True



# (x>y) AND/OR/NOT (y>z) => x IN(NOT IN) li => s/li IS/IS_NOT/== s2/li2 => id(li1)==id(li2)

















