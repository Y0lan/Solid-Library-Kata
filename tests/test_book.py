import unittest
from book import Book


class TestBook(unittest.TestCase):
    def test_book_have_title(self):
        title = "abcde"
        book = Book(title, "author")
        self.assertEqual(book.title, title)

    def test_book_have_author(self):
        author = "ben"
        book = Book("test", author)
        self.assertEqual(book.author, author)


