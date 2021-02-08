from librarian import Librarian
from menus import show_menu


def setup():
    print("generation of a librarian...")
    librarian = Librarian()
    librarian.add_book("toto", "tom")
    librarian.add_book("toto II", "tom")
    librarian.add_book("xx21", "tim")
    librarian.add_book("xx22", "tim")
    librarian.add_book("Investir dans le btc", "Elon Musk")


def main():
    setup()
    show_menu()


if __name__ == '__main__':
    main()
