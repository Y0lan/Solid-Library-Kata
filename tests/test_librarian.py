from unittest import TestCase

from librarian import Librarian
from library import LIBRARY


class TestLibrarian(TestCase):
    def test_add_book(self):
        librarian = Librarian()
        previous_length = len(LIBRARY)
        librarian.add_book("title", "author")
        self.assertEqual(previous_length + 1, len(LIBRARY))
