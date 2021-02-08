from datetime import date

from dateutil.relativedelta import relativedelta


class Library:
    books = set()

    def mark_borrowed(self, title, user_id):
        book = self.search_book_by_title(title)
        self.books.remove(book)
        book.is_borrowed = True
        book.borrowedAt = date.today()
        book.borrowedUntil = book.borrowedAt + relativedelta(weeks=+3)
        book.borrowedBy = user_id
        self.books.add(book)
        return book

    def search_book_by_title(self, title):
        book = [book for book in self.books if book.title == title]
        if len(book) > 0:
            return book
        else:
            print("can not find a book with title:", title)
            return None

    def search_book_by_author(self, author):
        book = [book for book in self.books if book.author == author]
        if len(book) > 0:
            return book
        else:
            print("can not find a book with author:", author)
            return None

    def show_all_books(self, search_in=None, borrowed=None):
        print('\n')
        collection = self.books
        if search_in:
            collection = search_in

        for book in collection:
            if borrowed:
                if book.is_borrowed == borrowed:
                    print("{} written by {} [due date: {} for user {}]".format(book.title, book.author,
                                                                               book.borrowed_until,
                                                                               book.borrowed_by))
            else:
                print("{} written by {} [available: {}]".format(book.title, book.author, not book.is_borrowed))

        print('\n')


LIBRARY = Library()
