
# dictionary
dic = {
    "name": "Filip",
    "age": 32
}
print(dic)  # {'name': 'Filip', 'age': 32}
if "name" in dic:
    print(dic["name"])  # Filip или KeyError
print(dic.get("name"))  # Filip (без KeyError)
dic["country"] = "Ukraine"
print(dic)  # {'name': 'Filip', 'age': 32, 'country': 'Ukraine'}
del dic["country"]  # удалит пару по ключу
# dic.pop('name')  # удалит пару по ключу
# dic.popitem()  # удалит последний елемент
# dic.clear()  # очистит словарь
print(dic)  # {'name': 'Filip', 'age': 32}
dic2 = dic.copy()
print(dic)  # {'name': 'Filip', 'age': 32}
dic3 = {1: "A", 2: "B"}
dic4 = {2: "BB", 3: "C"}
dic3.update(dic4)
print(dic3)  # {1: 'A', 2: 'BB', 3: 'C'}
print(dic4)  # {2: 'BB', 3: 'C'}


for i in dic:
    print(i)  # name  age
for key in dic.keys():
    print(key)  # name  age
for value in dic.values():
    print(value)   # Filip  32
for i in dic.items():
    print(i)  # ('name', 'Filip')  ('age', 32)
for key, value in dic.items():
    print(key, "-", value)  # name - Filip    age - 32
print(dic.keys())  # dict_keys(['name', 'age'])
print(dic.values())  # dict_values(['Filip', 32])
print(dic.items())  # dict_items([('name', 'Filip'), ('age', 32)])

d2 = dict()
d6 = {}
print(type(d6))  # <class 'dict'>
print(d2)  # {}
d3 = dict([("name", "Peter"), ("age", 19)])
print(d3)  # {'name': 'Peter', 'age': 19}
d4 = dict(code='UA', name="Ukraine")  # ключ строка
print(type(d4))  # <class 'dict'>
d5 = {(5, 6): 4}
print(d5[(5, 6)])  # 4

users2 = {
    "Tom":
        {"age": 23, "country": "UA"},
    "Sasha":
        {"age": 24, "country": "USA"}
}
print(users2)
print(users2["Sasha"]["country"])

d = {
    "name": "Filip",
    "age": 32,
    "is_registered": False,
    "rate": 12.5,
    "total_score": 200,
    "linked_ids": [1, 45, 98]
}
print(type(d))   # <class 'dict'>

person = {
    'user_1': {
        "first_name": 'John',
        'last_name': 'Marley',
        'age': 45,
        'adress': ('Kiev', 'Sadova str', '45'),
        'grades':{'math': 5, 'physics': 3}
    },
    "user_2":{
    }
}
print(person['user_1'])  # {'first_name': 'John', 'last_name': 'Marley', 'age': 45, 'adress': ('Kiev', 'Sadova str', '45'), 'grades': {'math': 5, 'physics': 3}}
print(person['user_1']['adress'])  # ('Kiev', 'Sadova str', '45')
print(person['user_1']['adress'][1])  # Sadova str


#  Dictionary comprehension:
squares = {x: x*x for x in range(4)}  # {0: 0, 1: 1, 2: 4, 3: 9}
print(squares)
odd_squares = {x: x*x for x in range(7) if x%2 == 1}  # {1: 1, 3: 9, 5: 25}
print(odd_squares)



















