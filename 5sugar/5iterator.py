# Iterator Pattern
numbers = [2, 5, 8]  # iterable
iterator1 = iter(numbers)  # iterator
print(next(iterator1))  # 2
print(next(iterator1))  # 5
print(next(iterator1))  # 8
# print(next(iterator1))   # Error: StopIteration
numbers = [2, 5, 7, 1, 0]
for num in numbers:
    print(num)


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

#
dict1 = {'Sasha': 25, 'Alice': 30, 'Ann': 15}
iter1 = iter(dict1.items())
print(next(iter1))
iter2 = iter(dict1.values())
print(next(iter2))
iter3 = iter(dict1.keys())
print(next(iter3))


# Create an Iterator
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 9:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclass = MyNumbers()
myiter = iter(myclass)
for i in myiter:
    print(i)




class Repeat:
    def __init__(self, msg):
        self.msg = msg

    def __iter__(self):
        return self

    def __next__(self):
        return self.msg


# obj = Repeat("car")
# obj_iterator = obj.__iter__()
# while True:
#   message = obj_iterator.__next__()
#   print(message)  # бесконечный цикл

# obj = Repeat("car")
# for message in obj:
#    print(message)  # тоже самое. Цикл for — это синтаксический сахар для цикла while.


# Finite iterator
class FiniteRepeat:

    def __init__(self, msg, max_count):
        self.msg = msg
        self.max_count = max_count
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.max_count:
            raise StopIteration
        self.count += 1
        return self.msg


obj = FiniteRepeat("car", 2)
for message in obj:
    print(message)

obj2 = FiniteRepeat("car", 3)
obj_iterator = iter(obj2)
while True:
    try:
        message = next(obj_iterator)
    except StopIteration:
        break
    print(message)



