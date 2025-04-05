import yaml
# yaml: pip install pyyaml=>dic=> str=yaml.dump(dic,dfs=False); open(path,w):yaml.dump(dic,f,dfs); dic=yaml.safe_load(str); open(path,r):dic=yaml.safe_load(f)
#  словарь в YAML-строку и в yaml-файл:
data1 = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "skills": ["Python", "Machine Learning", "Data Science"]
}
yaml_string1 = yaml.dump(data1, default_flow_style=False) # default_flow_style - не в несколько/одну строку
print(yaml_string1)
print(type(yaml_string1))

with open('../testFiles/data.yaml', 'w') as file:
    yaml.dump(data1, file, default_flow_style=False)


# YAML-строкa в Python-объект (словарь)
yaml_string = """
name: Alice
age: 30
city: New York
skills:
  - Python
  - Machine Learning
  - Data Science
"""
print(type(yaml_string1))  # str
data2 = yaml.safe_load(yaml_string)
print(data2)
print(type(data2))  # dict
print(data2['name'])  # Alice


# Чтение из YAML-файла в словарь
with open('../testFiles/data.yaml', 'r') as file2:
    # data3 = yaml.safe_load(file2)
    data3 = yaml.load(file2, Loader=yaml.Loader)  # 2сп

print(data3)  # {'age': 30, 'city': 'New York', 'name': 'Alice', 'skills': ['Python', 'Machine Learning', 'Data Science']}

