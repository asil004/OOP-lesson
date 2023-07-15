from datetime import datetime


class Book:
    count = 0

    def add_count(self):
        Book.count += 1
        return Book.count

    def __init__(self, title: str, author: "Author", pages: int, language: str, created_at: datetime):
        self.id = self.add_count()
        self.title = title
        self.author = author
        self.pages = pages
        self.language = language
        self.created_at = created_at

    def __repr__(self):
        return f'Title: {self.title}'


class Author:
    count = 0

    def add_count(self):
        Author.count += 1
        return Author.count

    def __init__(self, first_name: str, last_name: str, nationality: str, birth_date: datetime):
        self.id = self.add_count()
        self.first_name = first_name
        self.last_name = last_name
        self.nationality = nationality
        self.birth_date = birth_date

    def __repr__(self):
        return self.first_name + ' ' + self.last_name


class Reader:
    count = 0

    def add_count(self):
        Reader.count += 1
        return Reader.count

    def __init__(self, first_name: str, last_name: str, status: bool):
        self.id = self.add_count()
        self.first_name = first_name
        self.last_name = last_name
        self.status = status
        self.books: list["Book"] = []

    def add_book(self, book) -> None:
        self.books.append(book)

    def get_books(self):
        return self.books

    def get_total_books(self):
        return len(self.books)

    def delete_book(self, book_id: int) -> bool:
        for index, book in enumerate(self.books):
            if book.id == book_id:
                del self.books[index]
                return True
        return False


author_date = datetime(1940, 1, 1)
created_at = datetime(2014, 1, 2)
author = Author('Daron', 'Ajemuglu', 'uzbek', author_date)
