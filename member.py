from library import LIBRARY, mark_borrowed, search_book_by_title, mark_return
from user import User
from usertypes import UserTypes


class Member(User):
    type = UserTypes.MEMBERS.value
    number_book_borrowed = 0

    def __init__(self):
        super().__init__(self.type)
        self.library = LIBRARY

    def borrow(self, title=""):
        if self.number_book_borrowed == 3:
            print("You already borrowed 3 book, please send one back...")
            return

        book = search_book_by_title(title)
        if book is None:
            print("Can't borrow a book that does not exist or is already borrowed...")
            return
        book = book[0]
        if book.is_borrowed:
            print("This book is unavailable until ", book.borrowed_until)
            return

        book = mark_borrowed(title, self.id)
        self.number_book_borrowed += 1
        print("{} is_borrowed successfully, please give it back before {}".format(book.title, book.borrowed_until))

    def send_back(self, title=""):
        book = search_book_by_title(title)
        if book is None:
            print("Can't send a book that does not exist...")
            return
        book = book[0]
        if not book.is_borrowed or not book.borrowed_by == self.id:
            print("This book is not yours")
            return
        mark_return(title)
        print("{} returned successfully".format(book.title))
        self.number_book_borrowed -= 1
