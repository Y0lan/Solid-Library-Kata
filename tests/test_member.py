from unittest import TestCase

from book import Book
from librarian import Librarian
from member import Member


class TestMember(TestCase):
    def test_borrow(self):
        librarian = Librarian()
        librarian.add_book("a", "b")
        librarian.add_book("c", "d")
        librarian.add_book("e", "f")
        librarian.add_book("g", "h")
        librarian.add_book("i", "j")
        librarian.add_book("k", "l")

        member = Member()
        member2 = Member()

        # Return None when borrowing a book already borrowed
        member.borrow("a")
        self.assertIsNone(member.borrow("a"))
        self.assertIsNone(member2.borrow("a"))

        # Return None when borrowing more than 3 books
        member.borrow("c")
        member.borrow("e")
        self.assertIsNone(member.borrow("g"))

        # Return None when borrowing a non existing book
        self.assertIsNone(member2.borrow("fkjerfjkzen"))

        book = Book("xx", "xx")
        book2 = Book("xy", "xx")
        librarian.add_book("xx", "xx")
        librarian.add_book("xy", "xx")

        # Can Borrow
        previous_book_borrowed = member2.number_book_borrowed
        self.assertEqual(member2.borrow("xx").title, book.title)
        self.assertEqual(member2.borrow("xy").borrowed_by, member2.id)
        self.assertEqual(member2.number_book_borrowed, previous_book_borrowed + 2)

    def test_send_back(self):
        librarian = Librarian()
        librarian.add_book("xxxx", "b")

        member1 = Member()
        member2 = Member()

        # can send back a book
        book = member1.borrow("xxxx")
        self.assertEqual(book.is_borrowed, True)
        self.assertEqual(member1.number_book_borrowed, 1)
        member1.send_back("xxxx")
        self.assertEqual(book.is_borrowed, False)
        self.assertEqual(member1.number_book_borrowed, 0)

        # can't send back a book that is not yours
        book = member1.borrow("xxxx")
        self.assertEqual(book.is_borrowed, True)
        member2.send_back("xxxx")
        self.assertEqual(book.is_borrowed, True)
        member1.send_back("xxxx")
        self.assertEqual(book.is_borrowed, False)

        # can't send back a book not borrowed
        book = member1.send_back("xxxx")
        self.assertIsNone(book)




