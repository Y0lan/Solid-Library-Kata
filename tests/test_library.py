from unittest import TestCase

from authentification import login
from librarian import Librarian
from library import search_book_by_title, search_book_by_author
from member import Member


class Test(TestCase):
    def test_search_book_by_title(self):
        librarian = Librarian()
        librarian.add_book("is_it_there?", "we will find out")
        book = search_book_by_title("is_it_there?")
        self.assertEqual(book[0].title, "is_it_there?")

    def test_mark_borrowed(self):
        librarian = Librarian()
        member = Member()

        # il a pas juste empreinté l'anneau...
        librarian.add_book("borrow me", "Boromir")
        member.borrow("borrow me")
        book = search_book_by_title("borrow me")
        self.assertEqual(book[0].is_borrowed, True)
        self.assertEqual(book[0].borrowed_by, member.id)

    def test_mark_return(self):
        librarian = Librarian()
        member = Member()
        # Ajout d'un livre
        librarian.add_book("borrow me2", "Boromir")

        # Empreint
        member.borrow("borrow me2")
        book = search_book_by_title("borrow me2")
        self.assertEqual(book[0].is_borrowed, True)
        self.assertEqual(book[0].borrowed_by, member.id)

        # Retour
        member.send_back("borrow me2")
        self.assertEqual(book[0].is_borrowed, False)
        self.assertEqual(book[0].borrowed_by, None)

    def test_search_book_by_author(self):
        librarian = Librarian()
        librarian.add_book("is_it_there?", "we will find out")
        book = search_book_by_author("we will find out")
        self.assertEqual(book[0].author, "we will find out")
