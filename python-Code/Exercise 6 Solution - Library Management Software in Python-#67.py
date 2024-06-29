# Exercise 6 Solution - Library Management Software in Python....

class Library:
    def __init__(self):
        self.noBook = 0
        self.books = []
    def addBook(self,book):
        self.books.append(book)
        self.noBook = len(self.books)
    def showInfo(self):
        print(f"The Library has {self.noBook} books")

l1 = Library()
l1.addBook("Harry Potter")
l1.showInfo()