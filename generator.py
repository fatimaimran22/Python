#Generator is much more memory efficient

def generate_numbers():
    for i in range(1,11):
        yield i

gen=generate_numbers()
for i in gen:
    print(i)

print("------------")
def generate_first_8_even_numbers():
    for i in range(1,9):
        if i%2==0:
            yield i

gen=generate_first_8_even_numbers()
for i in gen:
    print(i)

print("------------")
def cubes_of_number():
    for i in range(1,6):
        yield i*i*i

gen=cubes_of_number()
print(next(gen))
print(next(gen))
print(next(gen))

print("------------")

for i in gen:
    print(i)

print("------------")   #Generator Expression
gen_exp=(x for x in range(1,11))
for i in gen_exp:
    print(i)

print("------------") #Generator Pipelining
def first_gen():
    for i in range(1,6):
        yield i

def second_gen(first_gen):  #passing generator as an argument
    for i in first_gen:
        yield i*i

gen1=first_gen()
gen2=second_gen(gen1)
for i in gen2:
    print(i)

print("------------")
def gen_countdown(n):
    while n>=1:
        yield n
        n-=1

gen=gen_countdown(6)
for i in gen:
    print(i)