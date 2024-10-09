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
    
    def __get_navigation_header_frame(self):
        return self.__navigation_header
    
    def __get_navigation_footer_frame(self):
        return self.__navigation_footer
    
    def __income_width(self):
        return self.__get_mainframe_width(0.2)
    
    def __income_height(self):
        return self.__get_mainframe_height(0.3)
    
    def __category_width(self):
        return self.__get_mainframe_width(0.2)
    
    def __category_height(self):
        return self.__get_mainframe_height(0.3)
    
    def __note_width(self):
        return self.__get_mainframe_width(0.8)

    def __note_height(self):
        return self.__get_mainframe_height(0.2)
    
    def __inputs_width(self):
        return self.__get_mainframe_width(0.3)

    def __inputs_height(self):
        return self.__get_mainframe_height(0.3)
    
    def _center_frame(self):#It is the method that holds all of the frames
        self.__set_main_frame()
        self.__navigation_header_frame()
        self.__navigation_footer_frame()
        self.__income_frame()
        self.__category_frame()
        self.__note_frame()
        self.__inputs_frame()

    def __set_main_frame(self):
        self.__main_frame = ctk.CTkFrame(self.__get_root(), width=self.__get_main_frame_width(), height= self.__get_main_frame_height(), fg_color="white")
        self.__main_frame.place(relx = 0.5, y =20, anchor= "n")

    def __get_main_frame(self):
        return self.__main_frame
    
    def __navigation_header_frame(self):
        self.__navigation_header = ctk.CTkFrame(self.__get_main_frame(), width=self.__navigation_width(), height= self.__navigation_height(), fg_color="yellow")
        self.__navigation_header.place(relx = 0.5, rely = 0.025, anchor="n")
        self.__usernamebutton()
        self.__listbutton()
        self.__breakdownbutton()

    def __usernamebutton(self):
        self.__username_button = ctk.CTkButton(self.__get_navigation_header_frame(), text="Name",width= 100, height= 50, font=("Poppins",20),fg_color="grey")
        self.__username_button.place(relx=0.1, rely=0.5, anchor="center")

    def __listbutton(self):
        self.__list_button = ctk.CTkButton(self.__get_navigation_header_frame(), text="List",width= 100, height= 50, font=("Poppins",20), fg_color="grey")
        self.__list_button.place(relx=0.5, rely=0.5, anchor="center")

    def __breakdownbutton(self):
        self.__breakdown_button = ctk.CTkButton(self.__get_navigation_header_frame(), text="breakdown",width= 100, height= 50, font=("Poppins",20), fg_color="grey")
        self.__breakdown_button.place(relx=0.7, rely=0.5, anchor="center")

    def __navigation_footer_frame(self):
        self.__navigation_footer = ctk.CTkFrame(self.__get_main_frame(), width=self.__navigation_width(), height= self.__navigation_height(), fg_color="yellow")
        self.__navigation_footer.place(relx = 0.5, rely = 0.85, y = -10,anchor="n")
        self.__Logout()
        self.__View_Profile()
        self.__add()
        self.__update()
        self.__delete()
    
    def __Logout(self):
        self.__logout_button = ctk.CTkButton(self.__get_navigation_footer_frame(), text="Name",width= 100, height= 50, font=("Poppins",20),fg_color="grey")
        self.__logout_button.place(relx=0.1, rely=0.5, anchor="center")

    def __View_Profile(self):
        self.__view_button = ctk.CTkButton(self.__get_navigation_footer_frame(), text="Name",width= 100, height= 50, font=("Poppins",20),fg_color="grey")
        self.__view_button.place(relx=0.2, rely=0.5, anchor="center")

    def __add(self):
        self.__add_button = ctk.CTkButton(self.__get_navigation_footer_frame(), text="Name",width= 100, height= 50, font=("Poppins",20),fg_color="grey")
        self.__add_button.place(relx=0.3, rely=0.5, anchor="center")

    def __update(self):
        self.__update_button = ctk.CTkButton(self.__get_navigation_footer_frame(), text="Name",width= 100, height= 50, font=("Poppins",20),fg_color="grey")
        self.__update_button.place(relx=0.4, rely=0.5, anchor="center")

    def __delete(self):
        self.__delete_button = ctk.CTkButton(self.__get_navigation_footer_frame(), text="Name",width= 100, height= 50, font=("Poppins",20),fg_color="grey")
        self.__delete_button.place(relx=0.5, rely=0.5, anchor="center")

    def __income_frame(self):
        self.__income = ctk.CTkFrame(self.__get_main_frame(), width=self.__income_width(), height= self.__income_height(), fg_color="blue")
        self.__income.place(relx = 0.2, rely = 0.35,anchor="center")
    
    def __category_frame(self):
        self.__category = ctk.CTkFrame(self.__get_main_frame(), width=self.__category_width(), height= self.__category_height(), fg_color="red")
        self.__category.place(relx = 0.45, rely = 0.35,anchor="center")

    def __note_frame(self):
        self.__note = ctk.CTkFrame(self.__get_main_frame(), width=self.__note_width(), height= self.__note_height(), fg_color="red")
        self.__note.place(relx = 0.5, rely = 0.7,anchor="center")

    def __inputs_frame(self):
        self.__input = ctk.CTkFrame(self.__get_main_frame(), width=self.__inputs_width(), height= self.__inputs_height(), fg_color="green")
        self.__input.place(relx = 0.75, rely = 0.35 ,anchor="center")
    
home = Home()
    
 