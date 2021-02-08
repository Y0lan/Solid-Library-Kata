from Authentification import login, signup
from Guest import Guest
from Librarian import Librarian
from Library import LIBRARY
from Member import Member
from UserType import UserTypes


def connection():
    current_user = None
    choice = 0
    while choice not in [1, 2, 3, 4]:
        print("\t1. Login")
        print("\t2. Signup")
        print("\t3. Guest")
        print("\t4. Quit")
        choice = int(input("-> "))
        if choice == 1:
            while current_user is None:
                user_id = str(input("enter an id\n"))
                current_user = login(user_id)
            return current_user
        if choice == 2:
            return Member()
        if choice == 3:
            return Guest()
        if choice == 4:
            quit()


def guest_menu():
    choice = 0
    book = None
    while choice not in [1, 2, 3, 4]:
        print("\t1. Search a book by title")
        print("\t2. Search books by author")
        print("\t3. See all books")
        print("\t4. Logout")
        choice = int(input("-> "))

    if choice == 1:
        while book is None:
            title = input('title\n->')
            book = LIBRARY.search_book_by_title(title)
    if choice == 2:
        while book is None:
            author = input('author\n->')
            book = LIBRARY.search_book_by_author(author)
    if choice == 3:
        LIBRARY.show_all_books()
    if choice == 4:
        return connection()
    if book is not None:
        LIBRARY.show_all_books(book)
    guest_menu()


def librarian_menu(librarian):
    choice = 0
    while choice not in [1, 2, 3, 4]:
        print("\t1. Add a book")
        print("\t2. Show all book")
        print("\t3. Display all book borrowed")
        print("\t4. Display all book borrowed with date to give back expired")
        print("\t5. Logout")
        choice = int(input("-> "))

    if choice == 1:
        title = input("title: ")
        author = input("author: ")
        librarian.add_book(title, author)
    if choice == 2:
        LIBRARY.show_all_books()
    if choice == 3:
        LIBRARY.show_all_books(borrowed=True)
    if choice == 4:
        pass
    if choice == 5:
        return connection()
    librarian_menu(librarian)


def main():
    current_user = None
    print("generation of a librarian...")
    librarian = Librarian()
    librarian.add_book("toto", "tom")
    librarian.add_book("toto II", "tom")
    librarian.add_book("xx21", "tim")
    librarian.add_book("xx22", "tim")
    librarian.add_book("Investir dans le btc", "Elon Musk")
    current_user = Member()
    current_user.borrow("xx22")
    current_user = connection()
    if current_user.type == UserTypes.GUEST.value:
        current_user = guest_menu()

    if current_user.type == UserTypes.LIBRARIAN.value:
        current_user = librarian_menu(current_user)


if __name__ == '__main__':
    main()
