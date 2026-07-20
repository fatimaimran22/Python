import multiprocessing

def square(n):
    return n*n

def cube(n):
    return n*n*n

def factorial(n):
    if n==1:
        return 1
    return factorial(n-1)*n

def is_prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
        
    return True

if __name__=="__main__":
    pool=multiprocessing.Pool()
    numbers=[1,2,3,4,5]
    square_of_numbers=pool.map(square,numbers)
    print(square_of_numbers)
    pool.close()
    pool.join()

    with multiprocessing.Pool() as pool:    #automatically closes pool
        result=pool.map(cube,numbers)

    print(result)

    number = [5, 6, 7, 8, 9]
    with multiprocessing.Pool(3) as pool:
        fact=pool.map(factorial,number)

    print(f"Factorial of {number}: {fact}")

    num = [17, 18, 19, 20, 23]
    with multiprocessing.Pool() as pool:
        is_prime_num=pool.map(is_prime,num)

    print(is_prime_num)
