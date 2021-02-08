import Authentification
import UserType


class User:
    type = UserType
    id = None

    def __init__(self, user_type):
        Authentification.signup(self, user_type)

