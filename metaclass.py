class MyMeta(type):
    def __new__(cls, name, base, attr):
        print(f"Creating class: {name}")
        return super().__new__(cls, name, base, attr)
    
class Person(metaclass=MyMeta):
    pass

