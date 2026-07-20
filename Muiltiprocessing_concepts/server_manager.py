from multiprocessing import Process, Manager

def func(d,l):
    d[1]="1"
    d["2"]=2
    d[0.25]=None

    l.reverse()

if __name__=="__main__":
    with Manager() as manager:
        mylist=manager.list(range(10))  #shared list 
        mydict=manager.dict()  #shared dict

        p=Process(target=func, args=(mydict,mylist))
        p.start()
        p.join()

        print(mydict)
        print(mylist)
        