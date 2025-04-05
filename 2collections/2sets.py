
        # set (списки, но еленты уникальны и идут в случайном порядке)
        # frozen set - объединение кортежа и множества (еленты уникальны и перемешаны, нельзя ничего добавить)
my_set = {1, 113.5, True, "Some string"}
print(type(my_set))  # <class 'set'>
print(set("Hello"))  # {'l', 'H', 'e', 'o'}
list1 = [5, 7, 3, 5, 5, 21]
set4 = set(list1)
print(set4)  # {21, 3, 5, 7}
tuple1 = (5, 7, 3, 5, 5, 21)
set5 = set(tuple1)
print(set5)  # {21, 3, 5, 7}

set1 = {5, 7, 4, 3, 5}
print(set1)  # {3, 4, 5, 7}
for i in set1:
    print(i)
# set1[2] = 43  # TypeError
# print(set1[0])  # TypeError
set1.add(32)  # {32, 3, 4, 5, 7}
set1.update(['23', True, 4, 6])  # {32, True, 3, 4, 5, 6, 7, '23'}
set1.remove(True)  # {32, 3, 4, 5, '23', 7, 6}
set1.pop()  # {3, 4, 5, 6, 7, '23'}
# set1.clear()  # set()
print(set1)

new_data = frozenset([5, 4, '30', True, 4])  # frozenset({True, 3, 4, 5, 6, 7, '30'})
print(new_data)  # frozenset({'30', True, 4, 5})
for i in new_data:
    print(i)
# new_data.add(4)  # AttributeError

s1 = {"a", "b", "c"}
s2 = {"a", "d"}
s3 = {"a"}
print(s1 | s2)  # {'d', 'a', 'c', 'b'}
print(s1.union(s2))  # {'d', 'a', 'c', 'b'}
print(s1 & s2)  # {'a'}
print(s1.intersection(s2))  # {'a'}
print(s1 - s2)  # {'c', 'b'}
print(s1.difference(s2))  # {'c', 'b'}
s1.update(s2)  # {'b', 'a', 'd', 'c'} # Обновляем множество элементами из другого множества
print(s1)
print("a" in s1)
print(s1.issuperset("a"))  # True
print(s3.issuperset(s1))  # True
print(s1.issubset(s3))  # True
