class Sun:
    _instance = None

    @classmethod  # makes the method `inst()` a class method
    def inst(cls):
        if cls._instance is None:
            cls._instance = cls()  # creates a new instance of the `Sun` class
        return cls._instance


p = Sun.inst()
f = Sun.inst()
print(p is f)



class Singleton(object):
    obj = None # attribute for storing a single copy
    def __new__(self, * args, ** kwargs): # class Singleton.
        if self.obj is None:
            # If it does not yet exist, then call __new__ of the parent class
            self.obj = object. __new__ (self, *args, **kwargs)
        return self.obj # will return Singleton


object_1 = Singleton()
object_1.Attr = 12
new_object = Singleton()
print(new_object.Attr)  # 12
print(new_object is object_1)  # True  new_object and object_1 is one and the same object
