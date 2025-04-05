class Person:
    """
    Docstring of person obj
    """

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name}, age {self.age}'

    def __repr__(self):
        return f'Person(name={self.name!r}, age={self.age!r})'

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.name == other.name and self.age == other.age
        return False

    def __hash__(self):
        return hash((self.name, self.age))
# magic: person(name,age)->def_str_:return_f'{s.name}'->def_eq_{s,o}:if_isistance(o,Person):return_s.name=o.name_return_False->def_hash_:return_hash(s.name,s.age)
# ->p1('A')=p2('A')=p3->pr(p1==p2)->pr(p1._eq_(p2))->pr(id(p1)=id(p3))->pr(hash(p1)=hash(p2))->#pr(o._str_()/_repr_/_dict_/_dir_/_class_/_module_/_doc_/_hash_)->str/repr/dir/hash(o)


person1 = Person("Sasha", 37)
person2 = Person("Alice", 30)
person3 = Person("Sasha", 37)
person4 = person1
print(person1 == person2)  # False
print(person1 == person3)  # True
print(person1 == person4)  # True
print('eq', person1.__eq__(person2))  # False
print('eq', person1.__eq__(person3))  # True
print('eq', person1.__eq__(person4))  # True
print(id(person1) == id(person2))  # False
print(id(person1) == id(person3))  # False
print(id(person1) == id(person4))  # True
print(hash(person1) == hash(person4))  # True
print(hash(person1) == hash(person3))  # True
print(hash(person1) == hash(person2))  # False

print('str:', person1.__str__())
print('repr:', person1.__repr__())
print('dict', person1.__dict__)  # dict {'name': 'Sasha'}
print('dir', person1.__dir__())  # dir ['name', '__module__', '__init__',...
print('class:', person1.__class__)  # class: <class '__main__.Person'>
print('module:', person1.__module__)  # module: __main__
print('doc:', person1.__doc__)  # Docstring of person obj
print('hash:', person1.__hash__())  # hash: 82733206205

print('STR:', str(person1))
print('REPR:', repr(person1))
print('HASH:', hash(person1))  # HASH: 82733206205
print('id:', id(person1))  # id: 2245969292240
print('DIR:', dir(person1))   # DIR: ['__class__', '__delattr__', '__dict__'
