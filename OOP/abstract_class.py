from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

    @abstractmethod
    def receipt(self):
        pass

class CreditCard(Payment):
    def pay(self, amount):
        print(f"Amount payed from card: {amount} dollars.")
    
    def receipt(self):
        print("Credit Card Receipt Printed!")

class PayPal(Payment):
    def pay(self, amount):
        print(f"Amount payed from paypal: {amount} dollars.")
    
    def receipt(self):
        print("PayPal Receipt Emailed!")


cred=CreditCard()
cred.pay(500)
cred.receipt()

paypal=PayPal()
paypal.pay(1000)
paypal.receipt()
