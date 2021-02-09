from unittest import TestCase

from guest import Guest


class TestGuest(TestCase):
    def test_guest_can_be_instanciated(self):
        guest = Guest()
        self.assertIsInstance(guest, Guest)

