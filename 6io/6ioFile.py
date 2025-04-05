# file = open('text.txt', 'w')  # w - режим работы для записи в него (стирает файл)
# # file = open('text.txt', 'a')  # a - добавление информации
# file.write('Hello\n')
# file.write('!!!')
# file.close()
#
# data = input("Enter word: ")
# file2 = open('text2.txt', 'w')
# file2.write(data + '\n')
# file2.close()

# # try:with_open(path,'r',enc='utf-8')_as_f: print(f.read(/7)/readline/readlines) => forin_f:print => except(FileNFE):
# file3 = open('testFiles/text2.txt', 'r')  # r - открываем для чтения
# print(file3.name)  # text2.txt
# print(file3.closed)  # False
# print(file3.mode)  # r
# print(file3.read())  # считает весь файд
# print(file3.read(7))  # считает первых 7символов
# print(file3.readline())  # считать одну строку
# print(file3.readlines())  # считать все строки
# for line in file3:
#     print(line, end='')  # построчно
# file3.close()
# print(file3.closed)  # True


# try:
#     file5 = open('text3.txt', 'r', encoding='utf-8')  # FileNotFoundError
#     print(file5.read())
# except FileNotFoundError:
#     print("Файл не найден")
# finally: file5.close()  # NameError - посколько переменная file5 не видна в finally

        #  менеджер with as - сам закроет файл всегда
try:
    with open('text2.txt', 'r', encoding='utf-8') as file4:  # FileNotFoundError
        print(file4.read())
except FileNotFoundError:
    print("Файл не найден")



lines = ["Hello Word\n", "Hello Work\n", "Hello World\n"]
with open("../testFiles/text.txt", "w") as file:
    file.writelines(lines)

print("Список строк записан в файл")


with open("../testFiles/text.txt", "a") as myfile:
    print("\nhello world", file=myfile)


with open("../testFiles/text.txt", "r") as file:
    for line in file:
        print(line, end="")

with open("../testFiles/text.txt", "w+") as file:
    file.write("Hello world\nHello work\n")  # сначала записываем данные
    file.seek(0)        # перемещаемся к первому байту в файле
    content = file.read()   # считываем данные
    print(content)

    # task read - write picture
# i0-picture: list=[] => open(path,'rb'):f.read => open(path,'wb'):f.write
FILENAME = "../testFiles/arbuz.jpg"  # файл для чтения
NEWFILENAME = "testFiles/arbuz_new.jpg"  # файл для записи

image_data = []  # список для хранения считанных данных

# считываем файл в список image_data
with open(FILENAME, "rb") as file:
    image_data = file.read()

# запись выше считанных байт в новый файл
with open(NEWFILENAME, "wb") as file:
    file.write(image_data)

print(f"Файл {FILENAME} скопирован в {NEWFILENAME}")




