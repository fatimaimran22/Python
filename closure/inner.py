def outer(y):
    def inner(x):
        return x+y
    return inner


inner_function=outer(10)

print(inner_function(5))


funcs=[]


for i in range(3):
    funcs.append(lambda i=i : print(i))


for f in funcs:
    f()