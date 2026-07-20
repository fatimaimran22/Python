import random

print(random.random())
print(random.randint(10,50))
print(random.uniform(5.5,9.5))
print(random.randrange(2,20,2)) #start stop step
print(random.randrange(1,20,2))

fruits = ["Apple", "Banana", "Orange", "Mango", "Grapes"]
print(random.choice(fruits))
print(random.choices(fruits,k=4))
print(random.sample(fruits,3))

numbers = [1,2,3,4,5,6,7]
random.shuffle(numbers)
print(numbers)

#random.seed(25)
print(random.randint(1,100))

print(random.randrange(1,7))    #Dice

print(random.choice(["Heads","Tails"]))

students = ["Ali","Ahmed","Fatima","Sara","Zain"]
print(random.choice(students))

print(random.sample(range(1,50),6)) #Generate 6 unique numbers between 1 and 49.

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
password=""
for i in range(8):
    password+=random.choice(characters)

print(password)