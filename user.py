import authentification
import usertypes


class User:
    type = usertypes
    id = None

    def __init__(self, user_type):
        authentification.signup(self, user_type)

