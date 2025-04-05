class Building:

    def __init__(self, year, city):
        self.year = year
        self.city = city

    def get_info(self):
        print("Year:", self.year, ". City:", self.city)

class School(Building):  # наследоввание

    def __init__(self, pupils, year, city):
        super(School, self).__init__(year, city)  # поля родителя
        self.pupils = pupils

    def get_info(self):  # полиморфизм
        super().get_info()
        print("Pupils:", self.pupils)


class Shop(Building):
    pass


school = School(100, 2000, "Kiev")
school.get_info()
shop = Shop(2002, "Odessa")
shop.get_info()
shop2 = Building(2003, "Lvov")
shop2.get_info()
