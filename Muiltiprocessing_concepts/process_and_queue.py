from multiprocessing import Process,Queue
import os

def countdown(name,q):
    print(f"{name}: PID = {os.getpid()}")
    q.put((name))
    for i in range(5,0,-1):
        print(name,i)

if __name__=="__main__":
    processes=[]
    q=Queue()
    for i in range(1,4):
        p=Process(target=countdown,args=(chr(i+64),q))
        processes.append(p)
        p.start()

    for _ in range(3):
        print(f"------{q.get()}-------")

    for p in processes:
        p.join()


    print("All processes Finished")