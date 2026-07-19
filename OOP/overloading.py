class Calculator:
    def multiply(self,*args):
        prod=1
        for n in args:
            if type(n)==int:
                prod*=n
        return prod

calc=Calculator()
print(calc.multiply(4,5))
print(calc.multiply(4,5,3))

class Printer:
    def print_message(self, name=None):
        if name is not None:
            print(f"Hello {name}!")
        else:
            print("Hello")

p=Printer()
p.print_message()
p.print_message("Fatima")