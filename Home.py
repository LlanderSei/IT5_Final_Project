from customtkinter import *
import customtkinter as ctk

class Home:
    def __init__(self):
        #self.__parent = parent
        self.__root = ctk.CTk()
        #self.__root.protocol("WM_DELETE_WINDOW", self.__on_close)
        self.Main_Window()
        self.__root.mainloop()

    def __get_main_window_width(self):
        return self.__get_frame_width(1)
    
    def __get_main_window_height(self):
        return self.__get_frame_height(1)
    
    def Main_Window(self):
        self.__root.title("Expense Tracker/Home")
        self.__root.after(50, lambda: self.__get_fullscreen())
        self.__root.configure(fg_color = "black")
        self.__root.minsize(self.__get_main_window_width(),self.__get_main_window_height())
        self._center_frame()
     
    def __get_fullscreen(self):
        return self.__root.state("zoomed")
    
    def __get_root(self):
        return self.__root
    
    def __get_frame_width(self, percentage):
        return int(self.__root.winfo_screenwidth() * percentage)

    def __get_mainframe_width(self, percentage):
        return int(self.__main_frame.winfo_screenwidth() * percentage)
    
    def __get_mainframe_height(self, percentage):
        return int(self.__main_frame.winfo_screenheight() * percentage)
    
    def __get_frame_height(self, percentage):
        return int(self.__root.winfo_screenheight() * percentage)
    
    def __get_main_frame_width(self):
        return self.__get_frame_width(0.9)
    
    def __get_main_frame_height(self):
        return self.__get_frame_height(0.85)
    
    def __navigation_width(self):
        return self.__get_mainframe_width(0.8)
    
    def __navigation_height(self):
        return self.__get_mainframe_height(0.1)
    
    def __income_width(self):
        return self.__get_mainframe_width(0.4)
    
    def __income_height(self):
        return self.__get_mainframe_height(0.3)
    
    def __note_width(self):
        return self.__get_mainframe_width(0.4)

    def __note_heigth(self):
        return self.__get_mainframe_height(0.2)
    
    def __category_width(self):
        return self.__get_mainframe_width(0.3)

    def __category_heigth(self):
        return self.__get_mainframe_height(0.55)
    
    def _center_frame(self):#It is the method that holds all of the frames
        self.__set_main_frame()
        self.__navigation_header_frame()
        self.__navigation_footer_frame()
        self.__income_frame()
        self.__note_frame()
        self.__category_dates_frame()

    def __set_main_frame(self):
        self.__main_frame = ctk.CTkFrame(self.__get_root(), width=self.__get_main_frame_width(), height= self.__get_main_frame_height(), fg_color="white")
        self.__main_frame.place(relx = 0.5, y =20, anchor= "n")

    def __get_main_frame(self):
        return self.__main_frame
    
    def __navigation_header_frame(self):
        self.__navigation_header = ctk.CTkFrame(self.__get_main_frame(), width=self.__navigation_width(), height= self.__navigation_height(), fg_color="yellow")
        self.__navigation_header.place(relx = 0.5, rely = 0.025, anchor="n")

    def __navigation_footer_frame(self):
        self.__navigation_footer = ctk.CTkFrame(self.__get_main_frame(), width=self.__navigation_width(), height= self.__navigation_height(), fg_color="yellow")
        self.__navigation_footer.place(relx = 0.5, rely = 0.85, y = -10,anchor="n")

    
    def __income_frame(self):
        self.__income = ctk.CTkFrame(self.__get_main_frame(), width=self.__income_width(), height= self.__income_height(), fg_color="blue")
        self.__income.place(relx = 0.3, rely = 0.35,anchor="center")
    
    def __note_frame(self):
        self.__income = ctk.CTkFrame(self.__get_main_frame(), width=self.__note_width(), height= self.__note_heigth(), fg_color="red")
        self.__income.place(relx = 0.3, rely = 0.7,anchor="center")

    def __category_dates_frame(self):
        self.__income = ctk.CTkFrame(self.__get_main_frame(), width=self.__category_width(), height= self.__category_heigth(), fg_color="green")
        self.__income.place(relx = 0.75, rely = 0.5 ,anchor="center")
    
home = Home()
    
 