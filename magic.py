# Callable Objects
class A:
    def __call__(self, *args, **kwargs):
        print("__call__ method is called")


obj = A()
obj()  # __call__ method is called


# with open("text.txt.txt") as f:
#     data = f.read()

# Context manager
class ContextManager:
    def __init__(self):
        print('__init__ method called')

    def __enter__(self):
        print('__enter__ method called')
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('__exit___ method called')


with ContextManager() as manager:
    print('inside with statement block')


class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()


with FileManager('testFiles/text.txt', 'w') as f:
    f.write("First Line\n")
    f.write("Second Line")


