class Bank:
    def __init__(self, user, balance):
        self.__balance = balance
        self.user = user

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited {amount}. New balance: {self.__balance}")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount
            print(f"Withdrawn {amount}. New balance: {self.__balance}")

    def display(self):
        print(f"User: {self.user}")
        print(f"Balance: {self.__balance}")

user = Bank("Dhananjay", 1000)
user.deposit(500)
user.withdraw(200)
user.display()

