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

#Hierarchial Inheritence
class Account:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    
    def deposit(self, amount):
        self.balance+=amount
        print(f"Deposited {amount}. New balance: {self.balance}") 

    def withdraw(self, amount):
        if amount>self.balance:
            print("Insufficient Balance")
        else:
            self.balance-=amount
            print(f"Withdrew {amount}. New balance: {self.balance}") 


class SavingsAccount(Account):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate=interest_rate

    def add_interest(self):
        interest=self.interest_rate*self.balance
        self.deposit(interest)
        print("Interest Added")

class CheckingAccount(Account):
    def __init__(self, owner, balance, overdraft_limit): 
        super().__init__(owner, balance) 
        self.overdraft_limit = overdraft_limit 

    def withdraw(self, amount): 
        if amount > (self.balance + self.overdraft_limit): 
            print("Overdraft limit exceeded.") 
        else: 
            self.balance -= amount 
            print(f"Withdrew {amount} (using overdraft). New balance: {self.balance}") 
 

s_acc=SavingsAccount("Alice",1000,0.05)
c_acc=CheckingAccount("Bob",2000,200)

s_acc.add_interest()
c_acc.withdraw(600)