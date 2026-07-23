#Pool-> to manage group of worker processes that can execute task in parallel distributing accross multiple CPUs
import multiprocessing
from multiprocessing import Pool,Process,Lock
import os 
import time

LOG_FILE="results.txt"
lock=None


def square(n):
    import random
    time.sleep(random.randint(1,10))
    #start=time.strftime()
    print(f"Square of number {n} is computed by process {os.getpid()}.")
    #time.sleep(1)   #to visualize work
    return n*n

#numbers=[x for x in range(100)]
numbers=[1,2,3,4,5]
if __name__=="__main__":
    with multiprocessing.Pool(3)as pool:
        p=pool.map(square,numbers)
    print(p)

# All the threads should write to the same file and append to it, .txt
# There is one process that then reads the file and then displays it's output (# when every process is not done with it's work, you shouldn't go and read the file)