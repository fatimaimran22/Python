#Single Inheritence
class Animal:
    def __init__(self,name):
        self.name=name
        print(f"Animal '{self.name}' created.") 

    def speak(self):
        print("Animal makes a sound.")

class Dog(Animal):
    def speak(self):
        super().speak()
        print(f"{self.name} says Woof!") 


dog=Dog("Bella")
dog.speak()

#Multiple Inheritence
class Father:
    def get_last_name(self):
        print("Smith")
    
class Mother:
    def get_last_name(self):
        print("Alina") 
    
class Child(Father,Mother):
    def get_last_name(self):
        Father.get_last_name(self)
        Mother.get_last_name(self)
        return "Ahmad"

c=Child()
print(c.get_last_name())

#Multi-level inheritence
class Electronics:
    def __init__(self):
        self.type="Electronic device"

    def has_power(self):
        print("This device needs power")

class Phone(Electronics):
    def __init__(self):
        super().__init__()
        self.type="Phone"
    
    def can_call(self):
        print("This device can make calls.")

class SmartPhone(Phone):
    def __init__(self):
        super().__init__()
        self.type="Smartphone"

    def has_internet(self):
        print("This device has internet")


obj=SmartPhone()
obj.has_internet()
obj.has_power()
obj.can_call()