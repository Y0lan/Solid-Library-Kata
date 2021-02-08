from UserType import UserTypes
from User import User


class Guest(User):
    def __init__(self, library):
        super().__init__(UserTypes.GUEST.value)
        self.library = library


