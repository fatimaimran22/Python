from functools import partial

def power(a,b):
    return a**b

power2=partial(power,b=2)
power4=partial(power,b=4)

print(power2(2))
print(power(2,3))
print(power4(2))
