square=lambda x: x*x
cube=lambda x:x*x*x
evenNo=lambda x: True if x%2==0 else False
largerNo=lambda x,y: x if x>y else y
sortByMarks=lambda students: dict(sorted(students.items(), key=lambda student: student[1]))
sortByNameLength=lambda name: sorted(name, key=len)
#key is basically a function in sorted 
sortDescend=lambda no: sorted(no, reverse=True)
doubleNo=lambda n: list(map(lambda x:x*2, n)) #map(function, iterable)-> map object
cToF=lambda temps: list(map(lambda x: x*(9/5)+32,temps))
findNameLengths=lambda name:[len(n) for n in name]  #list comprehension
keepOnlyEvenNos=lambda n: list(filter(lambda x: x%2==0, n)) #filter(function, iterable)
wordsWthLenGreaterthan5=lambda words: list(filter(lambda x: len(x)>5,words))
postiveNo=lambda numbers: list(filter(lambda n:n>0,numbers))
#reduce(function, iterable, initial_value)
from functools import reduce
FindSum=lambda no: reduce(lambda a,b:a+b,no,0)
FindLargest=lambda no: reduce(lambda a,b: a if a>b else b, no)
MultiplyAll=lambda no: reduce(lambda a,b: a*b, no, 1)

print(square(2))
print(cube(2))
print(evenNo(2))
print(largerNo(9,10))

students={
    "Ali":39,
    "Fatima":50,
    "Ahmad":45
}
print(sortByMarks(students)) #sort dict by marks of students

names=["Ali","Fatima","Hania","Shreya","Akansha"]   #sort names by length
print(sortByNameLength(names))

numbers = [15, 4, 20, 7, 11, 3] #sort no in descending order
print(sortDescend(numbers))

print(doubleNo(numbers))

temps = [0,20,30,40]    #covert celcius to fahrenheit
print(cToF(temps))

print(findNameLengths(names))

numbers = [1,2,3,4,5,6,7,8,9]   #keep only even numbers
print(keepOnlyEvenNos(numbers))

words = [
    "cat",
    "elephant",
    "dog",
    "computer",
    "sun"
]   #Return only the words whose length is greater than 5.
print(wordsWthLenGreaterthan5(words))

numbers = [-3,5,-7,9,-2,4]  #positive numbers only
print(postiveNo(numbers))

print(FindSum(numbers))
print(MultiplyAll(numbers))
