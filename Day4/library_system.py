class LibraryItem:

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def describe(self):
        return f"{self.title} by {self.author}"


class Book(LibraryItem):

    def __init__(self, title, author, year, pages):
        super().__init__(title, author, year)
        self.pages = pages

    def describe(self):
        return f"{self.title} | Pages: {self.pages}"


class EBook(LibraryItem):

    def __init__(self, title, author, year, file_size_mb):
        super().__init__(title, author, year)
        self.file_size_mb = file_size_mb

    def describe(self):
        return f"{self.title} | Size: {self.file_size_mb}MB"


items = [
    Book("Python", "ABC", 2020, 500),
    Book("DSA", "XYZ", 2021, 400),
    EBook("AI", "John", 2023, 10),
    EBook("ML", "Mark", 2022, 8)
]

for item in items:
    print(item.describe())

# isinstance(book, LibraryItem) returns True
# because Book inherits from LibraryItem