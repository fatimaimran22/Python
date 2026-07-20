def decorator(func):
    def wrapper():
        print("Function Started")
        func()
        print("Function Ended")

    return wrapper

@decorator
def func():
    print("I am a Function")

func()