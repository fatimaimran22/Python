import threading

def work(i):
    print(f"Hello {i}")

threads=[]

for i in range(100):
    t=threading.Thread(target=work, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()


from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor(max_workers=2) as executer:
    for i in range(100):
        executer.submit(work,i)