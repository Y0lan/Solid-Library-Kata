from authentification import login
from library import show_all_books, search_book_by_title, search_book_by_author
from member import Member
from usertypes import UserTypes


def main_menu():
    current_user = None
    choice = 0
    while choice not in [1, 2, 3, 4]:
        print("\t1. Login")
        print("\t2. Signup")
        print("\t3. Guest")
        print("\t4. Quit")
        try:
            choice = int(input("-> "))
        except Exception as e:
            print(e)
        if choice == 1:
            while current_user is None:
                user_id = str(input("enter an id\n"))
                current_user = login(user_id)
            return show_menu(current_user)
        if choice == 2:
            Member()
            show_menu()
        if choice == 3:
            return guest_menu()
        if choice == 4:
            quit()


def guest_menu():
    choice = 0
    while choice not in [1, 2, 3, 4]:
        print("\t1. Search a book by title")
        print("\t2. Search books by author")
        print("\t3. See all books")
        print("\t4. Menu")
        try:
            choice = int(input("-> "))
        except Exception as e:
            print(e)
    book = search_books(choice)
    if choice == 4:
        return main_menu()
    if book is not None:
        show_all_books(book)
    guest_menu()


def librarian_menu(librarian):
    choice = 0
    while choice not in [1, 2, 3, 4]:
        print("\t1. Add a book")
        print("\t2. Show all book")
        print("\t3. Display all book borrowed")
        print("\t4. Logout")
        try:
            choice = int(input("-> "))
        except Exception as e:
            print(e)

    if choice == 1:
        title = input("title: ")
        author = input("author: ")
        librarian.add_book(title, author)
    if choice == 2:
        show_all_books()
    if choice == 3:
        show_all_books(borrowed=True)
    if choice == 4:
        return main_menu()
    librarian_menu(librarian)


def search_books(choice):
    book = None
    if choice == 1:
        while book is None:
            title = input('title\n->')
            book = search_book_by_title(title)
            return book
    if choice == 2:
        while book is None:
            author = input('author\n->')
            book = search_book_by_author(author)
    if choice == 3:
        show_all_books()
    return book


def find_book_title():
    book = None
    title = None
    while book is None:
        title = input('title\n->')
        book = search_book_by_title(title)
    return title


def member_menu(member):
    choice = 0
    book = None
    while choice not in [1, 2, 3, 4, 5, 6]:
        print("\t1. Search a book by title")
        print("\t2. Search books by author")
        print("\t3. See all books")
        print("\t4. Borrow book")
        print("\t5. Return book")
        print("\t6. Logout")
        try:
            choice = int(input("-> "))
        except Exception as e:
            print(e)
    book = search_books(choice)
    if book is not None:
        show_all_books(book)
    if choice == 4:
        title = find_book_title()
        member.borrow(title)
    if choice == 5:
        title = find_book_title()
        member.send_back(title)
    if choice == 6:
        return main_menu()
    member_menu(member)


def show_menu(current_user=None):
    while current_user is None:
        current_user = main_menu()
    if current_user.type == UserTypes.LIBRARIAN.value:
        current_user = librarian_menu(current_user)
    if current_user.type == UserTypes.MEMBERS.value:
        member_menu(current_user)
