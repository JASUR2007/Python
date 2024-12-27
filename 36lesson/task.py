# Task 1: Library Management System
# Create a LibraryItem base class with:

# Attributes:
# title (string)
# author (string)
# publication_year (int)
# Methods:
# display_info(): Prints the item's details.
# Create subclasses for Book and Magazine:

# Book:
# Additional attribute: genre (string)
# Override display_info() to include genre.
# Magazine:
# Additional attribute: issue_number (int)
# Override display_info() to include issue number.
# Objective: Practice creating subclasses and overriding methods.

class LibraryItem:
    def __init__(self, title:str, author:str, publication_year: int):
        self.title=title
        self.author=author
        self.publication_year=publication_year
    def display_info(self):
        return f'the title is {self.title}, author is {self.author}, publication year is {self.publication_year}'

class Book(LibraryItem):
    def __init__(self, title:str, author:str, publication_year: int, genre:str):
        super().__init__(title,author, publication_year)
        self.genre=genre
    def display_info(self):
        return f'{super().display_info()}, genre is {self.genre}' 


class Magazine(LibraryItem):
    def __init__(self, title:str, author:str, publication_year: int, issue_number:int):
        super().__init__(title,author, publication_year)
        self.issue_number=issue_number
    def display_info(self):
        return f'{super().display_info()}, issue number is {self.issue_number}'

book=Book('Harry Potter','Someone', 1998, 'science' )
print(book.display_info())

magaizne=Magazine('Times', 'NewYork scienstists', 2005, 100)
print(magaizne.display_info())