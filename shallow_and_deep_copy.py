print("------Assignment---------")
numbers=[10,20,30]
a=numbers
a.append(40)
print(numbers)
print(a)
print(id(numbers))
print(id(a))

print("------Shallow---------")
import copy
b=copy.copy(numbers)
b.append(50)
print(numbers)
print(b)
print(id(numbers))
print(id(b))

print("------Deep---------")
num=[[1,2],[3,4]]
b=copy.deepcopy(num)
b[0].append(100)
print(num)
print(b)
print(id(num))
print(id(b))