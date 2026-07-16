def Print_n_till_1(n):
    if n==1:
        print(n)
        return
    print(n)
    Print_n_till_1(n-1)

def Print_1_till_n(n):
    if n==1:
        print(n)
        return
    Print_1_till_n(n-1)
    print(n)

def Sum_first_n(n):
    if n==0:
        return 0
    return n+Sum_first_n(n-1)

def Factorial(n):
    if n==1:
        return 1
    return Factorial(n-1)*n

def Power(a,b):
    if(b==1):
        return a
    return Power(a,b-1)*a

def Count_Digits(n):
    if n==0:
        return 0
    return Count_Digits(n//10)+1
    
def FindMax(numbers):
    if len(numbers) == 1:
        return numbers[0]
    
    max=FindMax(numbers[:-1])
    if max < numbers[-1]:
        return numbers[-1]
    else:
        return max
    
def SumOfList(numbers):
    if len(numbers)==1:
        return numbers[0]
    
    return numbers[-1]+SumOfList(numbers[:-1])

def ReverseAString(string, index):
    if index==0:
        return string[0]
    return string[index]+ReverseAString(string, index-1)

def Fibonacci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return Fibonacci(n-1)+Fibonacci(n-2)

def isPalindrome(string, L, R):
    if L>=R:
        return True
    if string[L]!=string[R]:
        return False
    return isPalindrome(string,L+1,R-1)


Print_n_till_1(6)
Print_1_till_n(6)
print(f"Sum: {Sum_first_n(5)}")
print(f"Factorial: {Factorial(5)}")
print(f"Power: {Power(2,3)}")
print(f"CountDigits {Count_Digits(456)}")
numbers = [2,4,6,8]
print(FindMax(numbers))
print(SumOfList(numbers))
print(ReverseAString("Fatima",len("Fatima")-1))
print(Fibonacci(7))
print(isPalindrome("madam", 0, len("madam") - 1))