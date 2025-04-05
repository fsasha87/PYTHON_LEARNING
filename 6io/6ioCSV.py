import csv

# rows=[] => with_open(path,'r')_as_f: => r=csv.reader(f) => header=next(r) => forin r: rows.append(i) => print(rows)

# file = open('testFiles/data.csv')
# csvreader = csv.reader(file)
# header = next(csvreader)
# rows = []
# for row in csvreader:
#     rows.append(row)
# print(rows)  # [['sasha', ' 23'], ['dasha', ' 34'], ['masha', ' 12']]
# file.close()
#
# # 2сп
# rows = []
# with open("testFiles/data.csv", 'r') as file:
#     csvreader = csv.reader(file)
#     header = next(csvreader)
#     for row in csvreader:
#         rows.append(row)
# print(header)  # ['name', ' age']
# print(rows)  # [['sasha', ' 23'], ['dasha', ' 34'], ['masha', ' 12']]

#  [[],[]] => open(path,'w',newline='') => csv.writer(f) => writerows(list/item) => reader(f) => print
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


# {:,:} => open(...w...)=> csv.DictWriter(f,fieldnames=[,]])=> w.writeheader() => w.writerows({:,:})/ w.writerow => reader:print
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

    # запись нескольких строк
    writer.writerows(users)

    user = {"name": "Sam2", "age": 41}
    # запись одной строки
    writer.writerow(user)

with open(FILENAME, "r", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["name"], "-", row["age"])





