class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"Book: {self.title} by {self.author}, Price: ₹{self.price}"

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', price={self.price})"


b1 = Book("Python Basics", "Guido", 500)
b2 = Book("Advanced Python", "Rossum", 800)

print(b1)              # __str__
print([b1, b2])        # __repr__