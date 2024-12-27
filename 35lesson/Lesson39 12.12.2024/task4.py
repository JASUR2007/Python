# 4 .Task: Library SystemCreate a parent class LibraryItem with attributes like title and author.
# Create child classes Book and DVD that add unique attributes such as pages for books and runtime for DVDs.
# Add a method details() to display information about the item.

class LibraryItem:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def details(self):
        return f"Title: {self.title}, Author: {self.author}"

class Book(LibraryItem):
    def __init__(self, title, author, pages):
        super().__init__(title, author)
        self.pages = pages

    def details(self):
        return f"{super().details()}, Pages: {self.pages}"

class DVD(LibraryItem):
    def __init__(self, title, author, runtime):
        super().__init__(title, author)
        self.runtime = runtime

    def details(self):
        return f"{super().details()}, Runtime: {self.runtime} minutes"


book = Book("1984", "George Orwell", 328)
dvd = DVD("Inception", "Christopher Nolan", 148)

print(book.details())
print(dvd.details())

