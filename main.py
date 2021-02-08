import random

from Authentification import login, signup
from Book import Book
from Guest import Guest
from Librarian import Librarian
from Library import Library
from Member import Member


def main():
    current_user = None
    print("generation of a librarian...")
    librarian = Librarian()
    print("generation of a guest...")
    choice = 0
    while choice not in [1, 2]:
        print("\t1. Login")
        print("\t2. Signup")
        print("\t3. Guest")
        choice = int(input("-> "))
        if choice == 1:
            while current_user is None:
                user_id = input("enter an id\n")
                current_user = login(user_id)
            print(current_user.id)


if __name__ == '__main__':
    main()
