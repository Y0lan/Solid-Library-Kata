from datetime import date
from dateutil.relativedelta import relativedelta


def search_book_by_title(title):
    book = [book for book in LIBRARY if book.title == title]
    if len(book) > 0:
        return book
    else:
        print("can not find a book with title:", title)


def mark_borrowed(title, user_id):
    book = search_book_by_title(title)
    if book:
        book = book[0]
        LIBRARY.remove(book)
        book.is_borrowed = True
        book.borrowed_at = date.today()
        book.borrowed_until = book.borrowed_at + relativedelta(months=+1)
        book.borrowed_by = user_id
        LIBRARY.add(book)
        return book


def mark_return(title):
    book = search_book_by_title(title)
    if book:
        book = book[0]
        LIBRARY.remove(book)
        book.is_borrowed = False
        book.borrowed_at = None
        book.borrowed_until = None
        book.borrowed_by = None
        LIBRARY.add(book)
        return book


def search_book_by_author(author):
    book = [book for book in LIBRARY if book.author == author]
    if len(book) > 0:
        return book
    else:
        print("can not find a book with author:", author)


def show_all_books(search_in=None, borrowed=None):
    print('\n')
    collection = LIBRARY
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


LIBRARY = set()
