class Library:
    books = set()

    def search_book_by_title(self, title):
        book = [book for book in self.books if book.title == title]
        if len(book) > 0:
            return book[0]
        else:
            return None

    def search_book_by_author(self, author):
        book = [book for book in self.books if book.author == author]
        if len(book) > 0:
            return book
        else:
            return None


LIBRARY = Library()
