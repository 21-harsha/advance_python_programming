from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print("Paid ₹", amount, "using Credit Card.")

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print("Paid ₹", amount, "using PayPal.")


class BitcoinPayment(PaymentStrategy):
    def pay(self, amount):
        print("Paid ₹", amount, "using Bitcoin.")

class PaymentProcessor:

    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def process_payment(self, amount):
        self.strategy.pay(amount)


amount = float(input("Enter payment amount: "))

print("\nChoose Payment Method")
print("1. Credit Card")
print("2. PayPal")
print("3. Bitcoin")

choice = int(input("Enter your choice: "))

if choice == 1:
    strategy = CreditCardPayment()
elif choice == 2:
    strategy = PayPalPayment()
elif choice == 3:
    strategy = BitcoinPayment()
else:
    print("Invalid Choice")
    exit()

processor = PaymentProcessor(strategy)
processor.process_payment(amount)

print("\nSwitch Payment Method")
print("1. Credit Card")
print("2. PayPal")
print("3. Bitcoin")

choice = int(input("Enter new choice: "))

if choice == 1:
    processor.set_strategy(CreditCardPayment())
elif choice == 2:
    processor.set_strategy(PayPalPayment())
elif choice == 3:
    processor.set_strategy(BitcoinPayment())
else:
    print("Invalid Choice")
    exit()

processor.process_payment(amount)