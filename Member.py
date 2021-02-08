from datetime import date
from dateutil.relativedelta import relativedelta

from Library import LIBRARY
from User import User
from UserType import UserTypes


class Member(User):
    type = UserTypes.MEMBERS.value
    number_book_borrowed = 0

    def __init__(self, library):
        super().__init__(self.type)
        self.library = LIBRARY

    def borrow(self, title=""):
        if self.number_book_borrowed == 3:
            print("You already borrowed 3 book, please send one back...")
            return

        book = self.library.search_book_by_title(title)
        if book is None:
            print("Can't borrow a book that does not exist...")
            return
        if book.is_borrowed:
            print("This book is unavailable until ", book.borrowedUntil)
            return

        book.is_borrowed = True
        book.borrowedAt = date.today()
        book.borrowedUntil = book.borrowedAt + relativedelta(weeks=+3)
        book.borrowedBy = self.id
        self.number_book_borrowed += 1
        print("{} is_borrowed successfully, please give it back before {}".format(book.title, book.borrowedUntil))

    def send_back(self, title=""):
        book = self.library.search_book_by_title(title)
        if book is None:
            print("Can't send a book that does not exist...")
            return
        if not book.is_borrowed or not book.borrowed_by == self.id:
            print("This book is not yours")
            return

        book.is_borrowed = False
        book.borrowedAt = None
        book.borrowedUntil = None
        book.borrowedBy = None
        self.number_book_borrowed -= 1
