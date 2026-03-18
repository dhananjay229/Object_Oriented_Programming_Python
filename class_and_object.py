class User:

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def display(self):
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Password: {self.password}")

user = User("Dhananjay", "[EMAIL_ADDRESS]", "123456")
user.display()


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display(self):
        print(f"Name: {self.name}")
        print(f"Price: {self.price}")
        print(f"Quantity: {self.quantity}")

product = Product("Laptop", 50000, 10)
product.display()