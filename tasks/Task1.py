import math
from math import sqrt
import random

# Print:s1+s2; s1,s2; s*2; s,end=""; s1,s2,sep=""; str,int,bool; \t\n\"\r; "Me"+str(age); "Me{}".format(age); f"Me{age}"
print("str1" + "str2")  # str1str2
print("str1", "str2")  # str1 str2
print("string1", end=" ")
print("string2")  # string1 string2
print("Hi" * 2)  # HiHi
print("Result:", 7, True, sep="")  # Result:7True
print("Not this \rOnly \tthis \"!\"")  # Only 	this "!"
age = 33
print("Me " + str(age))
print("Me {}".format(age))
print(f"Me {age}")


# int: 5/2; 5//2; 5%2; 5**2; +=; min(,,,); pow(,); round(5/3); math.sqrt(4); sqrt(4); 3+int(s); s+str(3); s,str(3)

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
print(math.sqrt(4))  # 2.0
print(random.randint(1, 10))  # 9
print(sqrt(9))  # 3.0
str_num = "5"
print(3 + int(str_num))  # 8
print(str_num + str(3))  # 53
print(str_num, str(3))  # 5 3

# string: s.find['a']; len[s]; s.cont['a']; s.upper(); s.isupper(); s.capitalize()
word1 = "itproger"
print(len(word1))
print(word1.count('r'))
print(word1.upper())
print(word1.isupper())
print(word1.islower())
print(word1.capitalize())  # 1й символ с заглавной, остальные в нижнем
print(word1.find('p'))  # индекс совпадения

# String: s => s.split(',') => print([]/[1]) => fori => ",".join([])
word2 = 'Football, basketball, skate'
hobby = word2.split(', ')
print(hobby)  # ['Football', 'basketball', 'skate']
print(hobby[1])  # basketball
for i in range(len(hobby)):
    hobby[i] = hobby[i].capitalize()
    print(hobby[i])  # Football     Basketball      Skate
result = ", ".join(hobby)
print(result)  # Football, Basketball, Skate

# Slice: str/list[1]/[0:4]/[4:]/[4:-2]/[0:-1:2]/[::]/[::-1]/[::-2]/str[slice(0, 4)]
word3 = 'Football'
print(word3[1])
print(word3[slice(0, 4)])  # Foot
print(word3[0:4])  # Foot - срез
print(word3[4:])  # ball
print(word3[4:-2])  # ba
print(word3[0:-1:2])  #Fobl
print(word3[::])  # Football
print(word3[::-1])  # llabtooF
print(word3[::-2])  # lato


# if: random.randint(1,99) => print(is_adult) => if not:print; if<18 => elif>60 =>else; ternar: status=s2 if>18 else s2
age = random.randint(1, 100)
print("Age:", age)
is_adult = age > 18 and age < 60
print(is_adult)
if not is_adult:
    print("You can't work")
if age <= 18:
    status = "child"
elif age > 60:
    status = "pensioner"
else:
    status = "adult"
print(status)
status = "adult" if age >= 18 else "child"
print(status)


# random.choice([,,]) => match x: case int()/str()/_:print()
x = random.choice([1, "Hello", True, None])
print(x)
match x:
    case int():
        print("Целое число")
    case str():
        print("Строка")
    case _:
        print("Other type")


# for: range(1,10) => 3 continue => 5 break => print(i); forin s: print(i)  else:"end"; forin s: found 'a'; forin s: counter 'a'
for i in range(1, 10):
    if i == 3:
        continue
    if i == 5:
        break
    print(i)  # 1  2  4

word = "asana"
for i in word:
    print(i, end=" ")
print("\n")

counter = 0
for i in word:
    if i == "a":
        counter +=1
print("Counter:" + str(counter))

found = None
for k in word:
    if k == "h":
        found = True
        break
    else:
        found = False
print(f"There is {k} in word: {found}")

# while: i<5:print(i); сумма парных чисел 1-10, else"End"
x = 1
while x < 5:
     print(x)
     x += 1

y = 0
sum = 0
while y <= 10:
    y += 1
    if y % 2 == 1:
        continue
    sum += y
    print(sum)
print("Sum: ", sum)

operation = 'read'
match operation:
    case 'read':
        print("read")
    case _:
        print("Other variant")
