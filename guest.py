from library import LIBRARY
from usertypes import UserTypes
from user import User


class Guest(User):
    def __init__(self):
        super().__init__(UserTypes.GUEST.value)
        self.library = LIBRARY


