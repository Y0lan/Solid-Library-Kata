from Book import Book
from Library import LIBRARY
from User import User
from UserType import UserTypes


class Librarian(User):
    type = UserTypes.LIBRARIAN.value

    def __init__(self):
        super().__init__(self.type)
        self.library = LIBRARY

    def add_book(self, title, author):
        book = Book(title, author)
        self.library.books.add(book)
        print('librarian added a book [ {}, {} ]'.format(book.title, book.author))


