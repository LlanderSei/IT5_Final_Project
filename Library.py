class Library:
    __libraryName = None

    def __init__(self, LibraryName = "default"):
        self.__libraryName = LibraryName;

    def set_library_name(self, libraryName):
        self.__libraryName = libraryName

    def get_library_name(self):
        return self.__libraryName

    def get_filename(self):
        return f"{self.get_library_name()}.txt"