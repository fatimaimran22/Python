from multiprocessing import Process,Value, Array

def func(num,arr):
    num.value=3.1415927
    for i in range(len(arr)):
        arr[i]=-arr[i]

if __name__=="__main__":
    num=Value('d',0.0)
    arr=Array('i',range(10))

    p=Process(target=func, args=(num,arr))
    p.start()
    p.join()

    print(num.value)
    print(arr[:])
    
