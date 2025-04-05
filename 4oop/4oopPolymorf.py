# poly: class_Dog: def_speak:... => class_Cat: def_speak => def_foo(an):print(an.speak())=> foo(dog/cat)

class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Cow:
    def speak(self):
        return "Moo!"

# Функция, принимающая любой объект с методом speak()
def animal_sound(animal):
    print(animal.speak())


# Создаем объекты разных классов
dog = Dog()
cat = Cat()
cow = Cow()

# Полиморфное поведение
animal_sound(dog)  # Выведет: Woof!
animal_sound(cat)  # Выведет: Meow!
animal_sound(cow)  # Выведет: Moo!
