from User import Readers, Librarian
from Books import Books
from Library import Library

test = Library()
libraryName = input("Enter the name of the library: ")
test.set_library_name(libraryName)

choice = int(input("[1]Reader or [2]Librarian: "))
match choice:
    case 1:
        user = Readers()
        userName = input("Enter your name: ")
        user.set_name(userName)
        while True:
            option = int(input(f"User: {user.get_name()}\n[1] Display Books\n[2] Search Books\n[3] Exit\nInput: "))
            match option:
                case 1:
                    my_lib = user.load_books(test.get_filename())
                    user.display_books(my_lib, test.get_library_name())
                case 2:
                    my_lib = user.load_books(test.get_filename())
                    searchBook = input("Enter the title of the book you are looking for: ")
                    user.search_books(my_lib, searchBook)
                case 3:
                    exit()
    case 2:
        librarian = Librarian()
        librarianName = input("Enter your name: ")
        librarian.set_name(librarianName)
        book = Books()
        while True:
            option = int(input(f"Librarian: {librarian.get_name()}\n[1] Add Books\n[2] Display Books\n[3] Search Books\n[4] Delete Books\n[5] Exit\nInput: "))
            match option:
                case 1:
                    numOfBooks = int(input("Enter the number of books you want to add: "))
                    for i in range(numOfBooks):
                        title = input("Enter the title of the book: ")
                        book.set_title(title)
                        author = input("Enter the author of the book: ")
                        book.set_author(author)
                        year = int(input("Enter the year of the book: "))
                        book.set_year(year)
                        print("")
                        librarian.add_books(book.get_title(), book.get_author(), book.get_year(), test.get_filename())
                case 2:
                    my_lib = librarian.load_books(test.get_filename())
                    librarian.display_books(my_lib, test.get_library_name())
                case 3:
                    my_lib = librarian.load_books(test.get_filename())
                    searchBook = input("Enter the title of the book you are looking for: ")
                    librarian.search_books(my_lib, searchBook)
                case 4:
                    my_lib = librarian.load_books(test.get_filename())
                    deleteBook = input("Enter the title of the book you want to delete: ")
                    librarian.delete_books(test.get_filename(),deleteBook)
                case 5:
                    exit()