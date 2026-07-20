import threading

def work(n):
    print("Working", n)

threads=[]

for i in range(5):
    t=threading.Thread(target=work, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()