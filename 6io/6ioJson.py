import json

# json: import_json->s->dict1=json.loads(s); dict->s=json.dumps(dict)

# Чтение JSON из строки в Python-объект (словарь)
str1 = '{"name": "Alice", "age": 30, "city": "New York"}'
data_dict = json.loads(str1)
print(data_dict)
print(type(data_dict))
print(data_dict['name'])

# из словаря в JSON-строку:
data_dict3 = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
str2 = json.dumps(data_dict3)
print(str2)


#data.json: dic->with_open('path','w')_as_f:json.dump(dic,f); with_open('path','r')_as_f:s=json.load(f)
# со словаря в JSON-файл:
data1 = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
with open('../testFiles/data2.json', 'w') as file1:
    json.dump(data1, file1)


# Чтение JSON из файла
with open('../testFiles/data.json', 'r') as file:
    data = json.load(file)  # {'name': 'Alice', 'age': 30, 'city': 'New York'}
print(data)
print(type(data))  # <class 'dict'>


