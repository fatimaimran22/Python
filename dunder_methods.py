#building block of Pythons memory model

class List:
    def __init__(self,numbers):
        self.data=list(numbers)
    
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, key):
        return self.data[key]
    
    def __iter__(self):
        return iter(self.data)
    

mylist=List([1,2,3])
print(f"Length of the list is: {len(mylist)}")
print(f"Second Index in my list is: {mylist[2]}")

print("-----Printing list in loop------")
for item in mylist:
    print(item)