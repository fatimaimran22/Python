#DRY (Don't Repeat Yourself) is violated here as:->>>>>>>>
#Notice that every time you want to measure something, you have to repeat:
#start timer
#execute code
#stop timer
#print elapse

print("-----------Without Context Manger-------------")

import time
from time import perf_counter

start=perf_counter()    #start timer

time.sleep(2)   #execute code

end=perf_counter()  #stop timer

print(f"Elapsed: {end-start:.2f} seconds.") # value : start formatting value after colon
#.2 means -> show two digits after the decimal point
#f means return number as floating point


print("-----------With Context Manger-------------") #It makes your timing code reusable and guarantees that the end time is recorded even if an exception occurs.

from contextlib import contextmanager

@contextmanager
def timer():
    start=perf_counter()    #__enter__
    yield   #block of code to execute
    end=perf_counter()  #__exit__
    print(f"Elapsed: {end-start: .2f} seconds.")


with timer():
    time.sleep(2)   #block of code




