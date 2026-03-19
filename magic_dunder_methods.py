# __init__
# __str__
# __len__

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"{self.title} by {self.author}, Price: ${self.price}"

    def __len__(self):
        return len(self.title)

maths = Book("Mathematics", "John Doe", 10)
print(maths)
print(len(maths))