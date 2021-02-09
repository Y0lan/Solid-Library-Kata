import unittest

from authentification import generate_unique_identification, login, find_user_by_id
from guest import Guest
from librarian import Librarian
from member import Member


class TestAuthentification(unittest.TestCase):
    def test_user_can_signup(self):
        guest = Guest()
        member = Member()
        librairian = Librarian()

        self.assertEqual(guest.id, 0)
        self.assertIsNotNone(member.id)
        self.assertIsNotNone(librairian.id)

    def test_user_can_login(self):
        member = Member()
        is_logged_in = login(member.id)
        self.assertEqual(is_logged_in, member)
        self.assertNotEqual(is_logged_in, "ékjefbkjhezb")

    def test_can_find_user_by_id(self):
        member = Member()
        found = find_user_by_id(member.id)
        self.assertEqual(member, found)
