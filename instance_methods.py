class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Withdrawn {amount}. New balance: {self.balance}")

    def display(self):
        print(f"Balance: {self.balance}")

account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)
account.display()
