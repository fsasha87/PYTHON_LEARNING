# io: try:with_open(path,'r',enc='utf-8')_as_f: print(f.read(/7)/readline/readlines) => forin_f:print => except(FileNFE):
try:
    with open('../testFiles/text2.txt', 'r', encoding='utf-8') as file3:
        print(file3.read())  # считает весь файд
        # print(file3.read(7))  # считает первых 7символов
        # print(file3.readline())  # считать одну строку
        # print(file3.readlines())  # считать все строки
        # for line in file3:
        #     print(line, end='')  # построчно
except FileNotFoundError:
        print("Файл не найден")


# io: with_open(path,'w+')_as_f: f.write(s)/f.writelines([,]) => f.seek(0) => print(f.read())
with open("../testFiles/text.txt", "w+") as file:
    file.write("Hello world\nHello work\n")  # сначала записываем данные
    file.seek(0)        # перемещаемся к первому байту в файле
    content = file.read()   # считываем данные
    print(content)

# io-picture: list=[] => open(path,'rb'):f.read => open(path,'wb'):f.write
FILENAME = "testFiles/arbuz.jpg"  # файл для чтения
NEWFILENAME = "testFiles/arbuz_new.jpg"  # файл для записи
image_data = []  # список для хранения считанных данных
with open(FILENAME, "rb") as file:
    image_data = file.read()
with open(NEWFILENAME, "wb") as file:
    file.write(image_data)
print(f"Файл {FILENAME} скопирован в {NEWFILENAME}")


# csv: rows=[] => with_open(path,'r')_as_f: => r=csv.reader(f) => header=next(r) => forin r: rows.append(i) => print(rows)
import csv
rows = []
with open("../testFiles/data.csv", 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)
print(header)  # ['name', ' age']
print(rows)  # [['sasha', ' 23'], ['dasha', ' 34'], ['masha', ' 12']]


# csv: [[],[]] => open(path,'w',newline='') => csv.writer(f) => writerows(list/item) => reader(f) => print
FILENAME = "../testFiles/users.csv"

users = [
    ["Tom", 28],
    ["Alice", 23],
    ["Bob", 34]
]
with open(FILENAME, "w", newline="") as file:   # ewline="" - пустая строка позволяет корректно считывать строки из файла вне зависимости от ОС
    writer = csv.writer(file)
    writer.writerows(users)
with open(FILENAME, "a", newline="") as file:
    user = ["Sam", 31]
    writer = csv.writer(file)
    writer.writerow(user)
with open(FILENAME, "r", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row[0], " - ", row[1])


# csv: {:,:} => open(...w...)=> csv.DictWriter(f,fieldnames=[,]])=> w.writeheader() => w.writerows({:,:})/ w.writerow => reader:print
FILENAME = "../testFiles/users2.csv"
users = [
    {"name": "Tom2", "age": 28},
    {"name": "Alice2", "age": 23},
    {"name": "Bob2", "age": 34}
]
with open(FILENAME, "w", newline="") as file:
    columns = ["name", "age"]
    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()
    writer.writerows(users)  # запись нескольких строк
    user = {"name": "Sam2", "age": 41}
    writer.writerow(user)  # запись одной строки
with open(FILENAME, "r", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["name"], "-", row["age"])




# json: import_json->s->dict1=json.loads(s); dict->s=json.dumps(dict)
import json
str1 = '{"name": "Alice", "age": 30, "city": "New York"}'
data_dict = json.loads(str1)
print(data_dict)
print(type(data_dict))
print(data_dict['name'])

data_dict3 = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
str2 = json.dumps(data_dict3)
print(str2)


#data.json: dic->with_open('path','w')_as_f:json.dump(dic,f); with_open('path','r')_as_f:s=json.load(f)
data1 = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
with open('testFiles/data2.json', 'w') as file1:
    json.dump(data1, file1)

with open('testFiles/data.json', 'r') as file:
    data = json.load(file)  # {'name': 'Alice', 'age': 30, 'city': 'New York'}
print(data)
print(type(data))  # <class 'dict'>


# xlsx: p_i_openpyxl: wb=openpyxl.load_workbook(path)->s=wb.active->print(s.cell(1,2).value)->print(s['A2'].value)
# ->for_row_in_s.iter_rows(...):for_c_in_row:print(c.value); s['A1']='Hi'->wb.save(path)


# yaml: dic=> str=yaml.dump(dic,dfs=False) => open(path,w):yaml.dump(dic,f,dfs); dic=yaml.safe_load(f); open(path,r):dic=yaml.safe_load(f)





