class Numbers:
    def __iter__(self):
        self.no=2
        # self.no=1
        return self
    def __next__(self):
        self.no+=2
        return self.no-2
        # if self.no <=5:
        #     self.no+=1
        #     return self.no-1
        # else:
        #     raise StopIteration
        
obj=Numbers()
it=iter(obj)
for i in range(5):
    print(next(it))

#print(next(it))