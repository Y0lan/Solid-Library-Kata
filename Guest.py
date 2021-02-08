from Library import LIBRARY
from UserType import UserTypes
from User import User


class Guest(User):
    def __init__(self):
        super().__init__(UserTypes.GUEST.value)
        self.library = LIBRARY


