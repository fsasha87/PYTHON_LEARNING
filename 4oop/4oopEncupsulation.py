class Field:

    def __init__(self):
        self.__value = None

    def get_value(self):
        return self.__value

    def set_value(self, value):
        self.__value = value


# encapsulation: class_M: def__init__(self,a,_b,__c):...=> obj => print(obj.a/_b/_M__c)=>obj.a/_b/_M__c=...

class Encapsulation(object):
    def __init__(self, a, b, c):
        self.public = a
        self._protected = b
        self.__private = c

x = Encapsulation(10, 11, 13)
print(x.public)  # 10
print(x._protected)  # 11
x._protected = 23
print(x._protected)  # 23
# print(x.__private)  # AttributeError
print(x._Encapsulation__private)  # 13
x._Encapsulation__private = 76
print(x._Encapsulation__private)  # 76


class P:
    def __init__(self, x):
        self.__x = x

    def __get_x(self):
        return self.__x

    def __set_x(self, x):
        self.__x = x

    x = property(__get_x, __set_x)


obj = P(5)
print(obj.x)
obj.x = 10
print(obj.x)



# encapsulation: class_R: def_init:self__x=x => @property_def_x(self):return self.__x => @x.setter_def_x(self.x):self.__x=x =>
class R:
    def __init__(self, x):
        self.__x = x

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x


r = R(5)
print(r.x)
r.x = 12
print(r.x)





