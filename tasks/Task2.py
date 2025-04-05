# list: [,,]=>len(l)=>append=>insert=>extend([,,])=>sort()=>reverse()=>pop()/(i)=>remove(v)=>count(v)=>forin=>clear()
numbers = [5, 2, 7]
# numbers[3] = 100  # IndexError:
numbers.append(100)
print(numbers)  # [5, 2, 7, 100]
numbers.insert(1, True)
print(numbers)  # [5, True, 2, 7, 100]
numbers.extend([5, 6, 8])
print(numbers)  # [5, True, 2, 7, 100, 5, 6, 8]
numbers.sort()
print(numbers)  # [True, 2, 5, 5, 6, 7, 8, 100]
numbers.reverse()
print(numbers)  # [100, 8, 7, 6, 5, 5, 2, True]
numbers.pop()  # удалили последний элемент
print(numbers)  # [100, 8, 7, 6, 5, 5, 2]
numbers.remove(100)
print(numbers)  # [8, 7, 6, 5, 5, 2]
numbers.pop(-2)  # удалили по индексу
print(numbers)  # [8, 7, 6, 5, 2]
# numbers.clear()  # удалит все
# print(numbers)  # []
print(numbers.count(6))  # количество совпадений
print(len(numbers))  # кол-во елементов
nums2 = [5, 2, 7, "50", False]
for el in nums2:
    el *= 2
    print(el)


# tuple: (),_ => forin => tuple[0]=TypeError =>tuple[1:3]/[::-1]=> index(v) =>len => count => tuple(list) => tuple(str)
data = (6, True, 5.6, 'Hello')
# data[0] = 5  # TypeError
print(data)  # (6, True, 5.6, 'Hello')
print(data[2])  # 5.6
print(data[1:5])  # (True, 5.6, 'Hello')
print(data[::-1])  # ('Hello', 5.6, True, 6)
print(data.index(6))  # 0
print(len(data))  # 4
print(data.count(6))  # 1
list = [5, 7, 8]
print(list)  # [5, 7, 8]
new_data = tuple(list)
print(new_data)  # (5, 7, 8)
word4 = tuple("Hello")
print(word4)  # ('H', 'e', 'l', 'l', 'o')


# set:{}=>print(set[2])=>add=>update([,])=>remove(v)=>pop()=>clear; set(str); set(list); set(tuple); frozenset([,])=>add=>forin
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
print(set("Hello"))  # {'l', 'H', 'e', 'o'}
nums = [5, 7, 3, 5, 5, 21]
nums = set(nums)
print(nums)  # {21, 3, 5, 7}

new_data = frozenset([5, 4, '30', True, 4])  # frozenset({True, '30', 4, 5})
print(new_data)  # frozenset({'30', True, 4, 5})
for i in new_data:
    print(i)
# new_data.add(4)  # AttributeError

# set: {}{} =>print(s1|s2)/s1.union(s2)=>&/intersection=>-/difference=>update=>'a' in s1=>s1.issuperset("a")=>issubset
s1 = {"a", "b", "c"}
s2 = {"a", "d"}
s3 = {"a"}
print(s1 | s2)  # {'d', 'a', 'c', 'b'}
print(s1.union(s2))  # {'d', 'a', 'c', 'b'}
print(s1 & s2)  # {'a'}
print(s1.intersection(s2))  # {'a'}
print(s1 - s2)  # {'c', 'b'}
print(s1.difference(s2))  # {'c', 'b'}
s1.update(s2)  # {'b', 'a', 'd', 'c'}
print(s1)
print("a" in s1)
print(s1.issuperset("a"))  # True
print(s3.issuperset(s1))  # True
print(s1.issubset(s3))  # True


# dict: {:,:} => ifin:d[k] => d.get(k) => d[k]=v => del_d[k]/pop(k)/popitem()/clear => copy() => d1.update(d2)
dic = {
    "name": "Filip",
    "age": 32
}
print(dic)  # {'name': 'Filip', 'age': 32}
if "name" in dic:
    print(dic["name"])  # Filip или KeyError
print(dic.get("name"))  # Filip
dic["country"] = "Ukraine"
# del dic["country"]  # удалит пару по ключу
# dic.pop('name')  # удалит пару по ключу
# dic.popitem()  # удалит последний елемент
# dic.clear()  # очистит словарь
# ?dic.update(???)
print(dic)  # {'name': 'Filip', 'age': 32}
dic2 = dic.copy()
print(dic)  # {'name': 'Filip', 'age': 32}
dic3 = {1: "A", 2: "B"}
dic4 = {2: "BB", 3: "C"}
dic3.update(dic4)
print("!!!!!!!!", dic3)  # {1: 'A', 2: 'BB', 3: 'C'}
print(dic4)  # {2: 'BB', 3: 'C'}

# dict: {:,:} =>for i/k,v in d.items/keys/values;  dict([(:),(:)])/dict(=,=);  {:{:,:},:{:,:}} => print
print(dic)  # {'name': 'Filip', 'age': 32, 'country': 'Ukraine'}
for i in dic:
    print(i)  # name  age  country
for i in dic:
    print(i, dic[i])  # name Filip    age 32    country Ukraine
for key in dic.keys():
    print(key)  # name  age  country
for value in dic.values():
    print(value)   # Filip  32  Ukraine
for i in dic.items():
    print(i)  # ('name', 'Filip')  ('age', 32)  ('country', 'Ukraine')
for key, value in dic.items():
    print(key, "-", value)  # name - Filip    age - 32    country - Ukraine


print(dic.keys())  # dict_keys(['name', 'age', 'country'])
print(dic.values())  # dict_values(['Filip', 32, 'Ukraine'])
print(dic.items())  # dict_items([('name', 'Filip'), ('age', 32), ('country', 'Ukraine')])

d3 = dict([("name", "Peter"), ("age", 19)])
print(d3)  # {'name': 'Peter', 'age': 19}
d4 = dict(code='UA', name="Ukraine")  # ключ строка
print(type(d4))  # <class 'dict'>

users2 = {
    "Tom":
        {"age": 23, "country": "UA"},
    "Sasha":
        {"age": 24, "country": "USA"}
}
print(users2)
print(users2["Sasha"]["country"])














users = {
    "Tom": {
        "phone": "+971478745",
        "email": "tom12@gmail.com"
    },
    "Bob": {
        "phone": "+876390444",
        "email": "bob@gmail.com",
        "skype": "bob123"
    }
}


