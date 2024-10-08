import tkinter as tk
import customtkinter as ctk  

class Breakdown:
    def __init__(self):
        #self.__parent = parent
        self.__root = ctk.CTk()
        #self.__root.protocol("WM_DELETE_WINDOW", self.__on_close)
        self.Main_Window()
        self.__root.mainloop()

    def __get_root(self):
        return self.__root
    
    def __get_main_window_width(self):
        return self.__get_frame_width(0.8)
    
    def __get_main_window_height(self):
        return self.__get_frame_height(0.8)
    
    def __get_frame_width(self, percentage):
        return int(self.__root.winfo_screenwidth() * percentage)
    
    def __get_frame_height(self, percentage):
        return int(self.__root.winfo_screenheight() * percentage)
    
    def __get_mainframe_width(self, percentage):
        return int(self.__main_frame.winfo_screenwidth() * percentage)
    
    def __get_mainframe_height(self, percentage):
        return int(self.__main_frame.winfo_screenheight() * percentage)
    
    def __on_close(self):
        self.__parent.quit()
        self.__parent.destroy()
        self.__root.destroy()
            
    def Main_Window(self):
        self.__root.title("Expense Tracker/Breakdown")
        self.__root.after(50, lambda: self.__get_fullscreen())
        self.__root.configure(fg_color = "black")
        self.__root.minsize(self.__get_main_window_width(),self.__get_main_window_height())
        self.__main_frames()
    def __get_fullscreen(self):
        return self.__root.state("zoomed")

    def __main_frames(self):
        self.__set_main_frame()
        self.__navigation_frames()
        self.__category_table_frames()
        self.__savings_table_frames()
    
    def __get_main_frame_width(self):
        return self.__get_frame_width(0.9)
    
    def __get_main_frame_height(self):
        return self.__get_frame_height(0.85)
    
    def __set_main_frame(self):
        self.__main_frame = ctk.CTkFrame(self.__get_root(), width=self.__get_main_frame_width(), height= self.__get_main_frame_height(), fg_color="white")
        self.__main_frame.place(relx = 0.5, y =20, anchor= "n")

    def __get_main_frame(self):
        return self.__main_frame
    
    def __navigation_width(self):
        return self.__get_mainframe_width(0.8)
    
    def __navigation_height(self):
        return self.__get_mainframe_height(0.1)
    
    def __category_width(self):
        return self.__get_mainframe_width(0.8)
    
    def __category_height(self):
        return self.__get_mainframe_height(0.3)
    
    def __saving_width(self):
        return self.__get_mainframe_width(0.8)
    
    def __saving_height(self):
        return self.__get_mainframe_height(0.3)
    
    def __navigation_frames(self):
        self.__navigation_header = ctk.CTkFrame(self.__get_main_frame(), width=self.__navigation_width(), height= self.__navigation_height(), fg_color="yellow")
        self.__navigation_header.place(relx = 0.5, rely = 0.025, anchor="n")

    def __category_table_frames(self):
        self.__category_table = ctk.CTkFrame(self.__get_main_frame(), width=self.__category_width(), height= self.__category_height(), fg_color="green")
        self.__category_table.place(relx = 0.5, rely = 0.4, anchor="center")

    def __savings_table_frames(self):
        self.__saving_table = ctk.CTkFrame(self.__get_main_frame(), width=self.__saving_width(), height= self.__saving_height(), fg_color="blue")
        self.__saving_table.place(relx = 0.5, rely = 0.6, anchor="n")
    # def __set_breakdown_frame(self, root):
    #     self.breakdownframe = ctk.CTkFrame(root, width=1000, height=650, fg_color="#696969", corner_radius=0)
    #     self.breakdownframe.place(relx=0.5, rely=0.5, anchor="center")
        
    #     category = ctk.CTkLabel(self.breakdownframe, text="Category", fg_color="#696969", text_color="white", 
    #                                     font=("Poppins", 20))
    #     category.place(x=90, y=130) 


    #     Tool  = ctk.CTkLabel(self.breakdownframe, text="Tool", fg_color="#696969", text_color="white", 
    #                                     font=("Poppins", 20))
    #     Tool.place(x=350, y=130) 

    #     Budget = ctk.CTkLabel(self.breakdownframe, text="Budget", fg_color="#696969", text_color="white", 
    #                                     font=("Poppins", 20))
    #     Budget.place(x=560, y=130) 

    #     Remaining = ctk.CTkLabel(self.breakdownframe, text="Remaining", fg_color="#696969", text_color="white", 
    #                                     font=("Poppins", 20))
    #     Remaining.place(x=790, y=130) 




    #     Needs = ctk.CTkLabel(self.breakdownframe, text="Needs", fg_color="#696969", text_color="black", 
    #                                   font=("Poppins", 20))
    #     Needs.place(x=100, y=240) 


    #     Wants = ctk.CTkLabel(self.breakdownframe, text="Wants", fg_color="#696969", text_color="black", 
    #                                     font=("Poppins", 20))
    #     Wants.place(x=100, y=370) 

    #     button = ctk.CTkButton(self.breakdownframe, text="Breakdown", fg_color="#2c2c2c", text_color="white", 
    #                             font=("Poppins", 15), corner_radius=35, height=50, width=200)
    #     button.place(x=540, y=30)

    #     button = ctk.CTkButton(self.breakdownframe, text="Budgeting", fg_color="#2c2c2c", text_color="white", 
    #                             font=("Poppins", 15), corner_radius=35, height=50, width=200)
    #     button.place(x=750, y=30)







window = Breakdown()
