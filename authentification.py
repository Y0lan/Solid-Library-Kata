import uuid
from usertypes import UserTypes

user_in_memory = set()


def generate_unique_identification():
    return str(uuid.uuid4())


def signup(user, user_type):
    user.id = generate_unique_identification()
    user.type = user_type
    if user.type is not UserTypes.GUEST.value:
        print("user [{}] [{}] signed up".format(user.id, user.type))
        print("You can now login with : ", user.id)
    else:
        user.id = 0
    user_in_memory.add(user)
    return user


def login(user_id):
    user = find_user_by_id(user_id)
    if user:
        print("user [{}] [{}] logged in".format(user.id, user.type))
        return user
    print("no user found with id", user_id)
    return None


def find_user_by_id(user_id):
    for user in user_in_memory:
        if user.id == user_id:
            return user
    return None
