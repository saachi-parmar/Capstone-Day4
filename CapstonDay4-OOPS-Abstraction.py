# Abstraction ----------------------------------------------------

from abc import abstractmethod

class Payment:
    
    @abstractmethod
    def process_payment(self):
        pass
    
class CreditCardPayment:
    
    def process_payment(self):
        print("Processing Credit Card Payement")
        
payment = CreditCardPayment()
payment.process_payment()

print("\n")