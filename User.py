from abc import ABC, abstractmethod
class User(ABC):
    @abstractmethod
    def set_name(self):
        pass
    @abstractmethod
    def get_name(self):
        pass
    @abstractmethod
    def display_books(self):
        pass
    @abstractmethod
    def search_books(self):
        pass
    @abstractmethod
    def load_books(self):
        pass
class Librarian(User):
    __name = None
    def set_name(self, name):
        self.__name = name
    
    def get_name(self):
        return self.__name
    
    def display_books(self, my_lib, libraryName):
        print(f" Library Name: {libraryName}")
        print("------------------------------")
        for i,book in enumerate(my_lib):
            print(f"{i+1}. Title: {book['title']} by {book['author']} (PUBLISHED) {book['year']}")
        
        print("------------------------------")
    
    def search_books(self, my_lib, searchBook):
        isFound = False
        for i,book in enumerate(my_lib):
            if searchBook == book['title']:
                print(f"{i+1}. Title: {book['title']} by {book['author']} (PUBLISHED) {book['year']}")
                isFound = True
                break
        if not isFound:
            print("Book was not found")
        
    def add_books(self, title, author, year, filepath):
        with open(filepath, "a") as fileWriter:
            fileWriter.write(f"{title},{author},{year}\n")

    def load_books(self,filepath):
        my_lib = []
        with open(filepath, "r") as fileReader:
            for line in fileReader.readlines():
                split = line.strip("\n").split(",")
                print(split)
                catch = {'title': split[0], 'author': split[1], 'year': split[2]}
                my_lib.append(catch)
        return my_lib
    
    def delete_books(self, filepath, deleteBook, my_lib):
        isFound = False
        with open(filepath, "w") as FileWriter:
            for i,book in enumerate(my_lib):
                if deleteBook != book['title']:
                    FileWriter.write(f"{book['title']},{book['author']},{book['year']}")
                    isFound = True;
            if not isFound:
                print("Book was not found")
            if isFound:
                print("Book was deleted")

class Readers(User):
    __name = None
    def set_name(self, name):
        self.__name = name
    
    def get_name(self):
        return self.__name
    
    def display_books(self, my_lib, libraryName):
        print(f" Library Name: {libraryName}")
        print("------------------------------")
        for i,book in enumerate(my_lib):
            print(f"{i+1}. Title: {book['title']} by {book['author']} (PUBLISHED) {book['year']}")
        
        print("------------------------------")
    
    def search_books(self, my_lib, searchBook):
        isFound = False
        for i,book in enumerate(my_lib):
            if searchBook == book['title']:
                print(f"{i+1}. Title: {book['title']} by {book['author']} (PUBLISHED) {book['year']}")
                isFound = True
                break
        if not isFound:
            print("Book was not found")

    def load_books(self,filepath):
        my_lib = []
        with open(filepath, "r") as fileReader:
            for line in fileReader.readlines():
                split = line.strip("\n").split(",")
                catch = {'title': split[0], 'author': split[1], 'year': split[2]}
                my_lib.append(catch)
        return my_lib