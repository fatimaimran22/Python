class Animal:
    def sound(self):
        print("Some Animal Sound")

class Cat(Animal):
    def sound(self):
        print("Meow")


c=Cat()
c.sound()


class Person:
    def introduce(self):
        print("I am a person.")

class Student(Person):
    def introduce(self):
        super().introduce()
        print("I am a student.")

s=Student()
s.introduce()