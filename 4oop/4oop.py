class Cat:
    # def __init__(self):  # конструктор по умолчанию
    #     pass

    # def __init__(self, name, age, isHappy):  # создали конструктор
    #     self.name = name
    #     self.age = age
    #     self.isHappy = isHappy
    #     self.get_data()  # доп.метод

    def __init__(self, name, age, isHappy = None):  # 2сп  None - поззволяет переопределить конструктор на меньше параметров
        self.set_data(name, age, isHappy)

    def set_data(self, name, age, isHappy):   # self - автоматически подставился, говорит, что метод внутри класса и обращается к полям внутри класса
        self.name = name
        self.age = age
        self.isHappy = isHappy

    def get_data(self):
        print(self.name, "age:", self.age, ". Happy:", self.isHappy)

cat4 = Cat("Olenka", 4, False)
cat4.get_data()

cat5 = Cat("LyaLya", 20)
cat5.get_data()

# cat1 = Cat()
# cat1.name = "Barsik"
# cat1.age = 3
# cat1.isHappy = True
# print(cat1.name)
#
# cat3 = Cat()
# cat3.set_data("ivasyk", 1, False)
# print(cat3.name)
# cat3.get_data()

print(dir(Cat))
print(dir(cat4))
print(cat4.__class__)
print(Cat.__class__)
print(cat4.__dict__)
print(Cat.__dict__)
print(cat4.__str__)
print(Cat.__str__)


