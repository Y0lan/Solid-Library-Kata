import uuid

from UserType import UserTypes

user_in_memory = set()


def generateUniqueIdentificationID():
    return uuid.uuid4()


def signup(user, user_type):
    user.id = generateUniqueIdentificationID()
    user.type = user_type
    print("user [{}] [{}] signed up".format(user.id, user.type))
    print("You can now login with : ", user.id)
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
        print("- {}".format(user.id))
        if user.id == user_id:
            return user
