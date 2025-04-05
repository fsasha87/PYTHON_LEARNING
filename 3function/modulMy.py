surname = "Obama"
print("Hello from modulMy.py")  # загрузится при from moduls import foo
if __name__ == "__main__":  # вып. с этого файла, но не вып.при импорте в другом файле
    print("printing inside modulMy.py")
print(globals()["__name__"])  # __main__  или если запустить с modulMy то:  '__name__': 'modulMy'


def hello():
    print("Hello", surname)


print(dir())







