from multiprocessing import Process, Lock

def func(lock, process):
    lock.acquire()
    try:
        print("Hello World", process)
    finally:
        lock.release()

if __name__=="__main__":
    lock=Lock()
    for num in range(10):
        Process(target=func, args=(lock, num)).start()