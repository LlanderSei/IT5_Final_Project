from customtkinter import *
import customtkinter as ctk
from PIL import Image
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
    
    def __get_navigation_header_frame_width(self, percentage):
        return int(self.__navigation_header.winfo_screenheight() * percentage)
    
    def __get_navigation_footer_frame_width(self, percentage):
        return int(self.__navigation_footer.winfo_screenheight() * percentage)
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
        return self.__get_mainframe_width(0.4)

    def __note_height(self):
        return self.__get_mainframe_height(0.3)
    
    def __inputs_width(self):
        return self.__get_mainframe_width(0.3)

    def __inputs_height(self):
        return self.__get_mainframe_height(0.3)
    
    def __username_button_width(self):
        return self.__get_navigation_header_frame_width(0.35)
    
    def __list_button_width(self):
        return self.__get_navigation_header_frame_width(0.2)
    
    def __breakdown_button_width(self):
        return self.__get_navigation_header_frame_width(0.2)
    
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
    
    def __get_image_logo(self):
        return Image.open("default.png").convert("RGBA")
    
    def __usernamebutton(self):
        self.__username_button = ctk.CTkButton(self.__get_navigation_header_frame(), text="Name",width= self.__username_button_width(), height= 50, font=("Poppins",20),fg_color="grey")
        self.__username_button.place(relx=0.25, rely=0.5, anchor="center")
        self.__photo = ctk.CTkImage(light_image= self.__get_image_logo(),
                     dark_image= self.__get_image_logo(),
                     size=(70, 70))
        self.__photoplacement = ctk.CTkLabel(self.__get_navigation_header_frame(), image=self.__photo, text="", fg_color="#696969", corner_radius=10)
        self.__photoplacement.place(relx= 0.1, rely= 0.5, anchor="center")

    def __listbutton(self):
        self.__list_button = ctk.CTkButton(self.__get_navigation_header_frame(), text="List",width= self.__list_button_width(), height= 50, font=("Poppins",20), fg_color="grey")
        self.__list_button.place(relx=0.6, rely=0.5, anchor="center")

    def __breakdownbutton(self):
        self.__breakdown_button = ctk.CTkButton(self.__get_navigation_header_frame(), text="breakdown",width= self.__breakdown_button_width(), height= 50, font=("Poppins",20), fg_color="grey")
        self.__breakdown_button.place(relx=0.85, rely=0.5, anchor="center")

    def __navigation_footer_frame(self):
        self.__navigation_footer = ctk.CTkFrame(self.__get_main_frame(), width= self.__note_width(), height= self.__note_height(), fg_color="yellow")
        self.__navigation_footer.place(relx = 0.7, rely = 0.60, y = -25,anchor="n")
        self.__Logout()
        self.__View_Profile()
        self.__add()
        self.__update()
        self.__delete()
    
    def __get_navigation_footer_width(self):
        return self.__get_navigation_footer_frame_width(0.2)
    
    def __Logout(self):
        self.__logout_button = ctk.CTkButton(self.__get_navigation_footer_frame(), text="Log-out",width= self.__get_navigation_footer_width(), height= 50, font=("Poppins",20),fg_color="grey")
        self.__logout_button.place(relx = 0.3, rely = 0.25, anchor = "center")

    def __View_Profile(self):
        self.__view_button = ctk.CTkButton(self.__get_navigation_footer_frame(), text="View Profile",width= self.__get_navigation_footer_width(), height= 50, font=("Poppins",20),fg_color="grey")
        self.__view_button.place(relx = 0.5, rely = 0.25, anchor = "w")

    def __add(self):
        self.__add_button = ctk.CTkButton(self.__get_navigation_footer_frame(), text="Add",width= self.__get_navigation_footer_width(), height= 50, font=("Poppins",20),fg_color="grey")
        self.__add_button.place(relx = 0.3, rely = 0.55, anchor = "s")

    def __update(self):
        self.__update_button = ctk.CTkButton(self.__get_navigation_footer_frame(), text="Update",width= self.__get_navigation_footer_width(), height= 50, font=("Poppins",20),fg_color="grey")
        self.__update_button.place(relx = 0.64, rely = 0.55, anchor = "s")

    def __delete(self):
        self.__delete_button = ctk.CTkButton(self.__get_navigation_footer_frame(), text="Delete",width= self.__get_navigation_footer_width(), height= 50, font=("Poppins",20),fg_color="grey")
        self.__delete_button.place(relx = 0.46, rely = 0.75, anchor = "s")

    def __income_frame(self):
        self.__income = ctk.CTkFrame(self.__get_main_frame(), width=self.__income_width(), height= self.__income_height(), fg_color="blue")
        self.__income.place(relx = 0.2, rely = 0.35,anchor="center")
        
      #LABELS for the input and correspond to that is their individual entery boxes, starts here and  line 177 
        self.__label_add_savings = ctk.CTkLabel(self.__income, text = "Add Savings:", font = ("Poppins", 16), width = 100, height = 30, fg_color = "black", text_color = "white")
        self.__label_add_savings.place( relx = 0.1, rely = 0.1, anchor = "w")
    
        self.__entry_add_savings = ctk.CTkEntry(self.__income, width=150, height=30, font=("Poppins", 16), fg_color="grey")
        self.__entry_add_savings.place( relx= 0.9, rely = 0.1, anchor = "e")
    
        self.__label_savings = ctk.CTkLabel(self.__income, text = "Savings:", font = ("Poppins", 16), width = 100, height = 30, fg_color = "black", text_color = "white")
        self.__label_savings.place( relx = 0.1, rely = 0.3, anchor = "w")
    
        self.__entry_savings = ctk.CTkEntry(self.__income, width = 150, height = 30, font = ("Poppins", 16), fg_color = "grey")
        self.__entry_savings.place( relx = 0.9, rely = 0.3, anchor = "e")
    
        self.__label_stipend = ctk.CTkLabel(self.__income, text= "Stipend:", font = ("Poppins", 16), width = 100, height = 30, fg_color = "black", text_color= "white")
        self.__label_stipend.place( relx = 0.1, rely = 0.5, anchor = "w")
        
        self.__entry_stipend = ctk.CTkEntry(self.__income, width = 150, height = 30, font = ("Poppins", 16), fg_color = "grey")
        self.__entry_stipend.place( relx = 0.9, rely = 0.5, anchor = "e")
    
        self.__label_month_of = ctk.CTkLabel(self.__income, text = "Month of:", font = ("Poppins", 16), width = 100, height = 30, fg_color = "black", text_color = "white")
        self.__label_month_of.place( relx=0.1, rely=0.7, anchor="w")
    
        self.__entry_month_of = ctk.CTkEntry(self.__income, width  = 150, height = 30, font = ("Poppins", 16), fg_color = "grey")
        self.__entry_month_of.place( relx = 0.9, rely = 0.7, anchor = "e")
    #ENDs here
    
    def __category_frame(self):
        self.__category = ctk.CTkFrame(self.__get_main_frame(), width=self.__category_width(), height= self.__category_height(), fg_color="red")
        self.__category.place(relx = 0.45, rely = 0.35,anchor="center")
        
        #Labels and Entryboxes for category frame
        self.__label_category = ctk.CTkLabel(self.__category, text = "Category", width=150, height=30, font=("Poppins", 16), fg_color="black", text_color = "white") 
        self.__label_category.place( relx = 0.1, rely = 0.1, anchor = "w")
        
        self.__label_needs = ctk.CTkLabel(self.__category, text = "Needs", width=150, height=30, font=("Poppins", 16), fg_color="black", text_color = "white") 
        self.__label_needs.place( relx = 0.1, rely = 0.3, anchor = "w")
        
        self.__label_wants = ctk.CTkLabel(self.__category, text= "Wants:", font = ("Poppins", 16), width = 150, height = 30, fg_color = "black", text_color= "white")
        self.__label_wants.place( relx = 0.1, rely = 0.5, anchor = "w")
        
        self.__label_budget = ctk.CTkLabel(self.__category, text = "Budget", width=150, height=30, font=("Poppins", 16), fg_color="black", text_color = "white") 
        self.__label_budget.place( relx = 0.5, rely = 0.1, anchor = "w")
        
        #Entry boxes
        self.__entry_needs = ctk.CTkEntry(self.__category, width  = 150, height = 30, font = ("Poppins", 16), fg_color = "grey")
        self.__entry_needs.place( relx = 0.9, rely = 0.3, anchor = "e")
        
        self.__entry_wants = ctk.CTkEntry(self.__category, width  = 150, height = 30, font = ("Poppins", 16), fg_color = "grey")
        self.__entry_wants.place( relx = 0.9, rely = 0.5, anchor = "e")
        
    def __note_frame(self):
        self.__note = ctk.CTkFrame(self.__get_main_frame(), width=self.__note_width(), height= self.__note_height(), fg_color="red")
        self.__note.place(relx = 0.5, rely = 0.75, anchor = "e")
        
        self.__label_note = ctk.CTkLabel(self.__note, text = "Note/Reminder:", font = ("Poppins", 20), width = 700, height = 40, fg_color = "black", text_color = "white")
        self.__label_note.place( relx = 0.05, rely = 0.2, anchor = "w")
    
        self.__entry_note = ctk.CTkTextbox(self.__note, width = 700, height = 100, font = ("Poppins", 20), fg_color = "gray")
        self.__entry_note.place( relx = 0.05, rely = 0.5, anchor = "w")

    def __inputs_frame(self):
        self.__input = ctk.CTkFrame(self.__get_main_frame(), width=self.__inputs_width(), height= self.__inputs_height(), fg_color="green")
        self.__input.place(relx = 0.75, rely = 0.35 ,anchor="center")
        
        noteDropdown_var = ctk.StringVar(value = "Needs")
        
        dropdown = ctk.CTkComboBox(self.__input, variable = noteDropdown_var, values = ["Needs", "Wants"], font = ("Poppins", 16), width = 300, height = 50, state = "readonly")
        dropdown.place( relx = 0.2, rely = 0.2, anchor = "w")
        
        self.__label_expenditures = ctk.CTkLabel(self.__input, text= "Expenditures:", font = ("Poppins", 16), width = 150, height = 30, fg_color = "black", text_color= "white")
        self.__label_expenditures.place( relx = 0.1, rely = 0.5, anchor = "w") 
        
        self.__entry_expenditures = ctk.CTkEntry(self.__input,height = 30, font = ("Poppins", 20), fg_color = "gray")
        self.__entry_expenditures.place( relx = 0.5, rely = 0.5, anchor = "w")
        
        self.__label_inputAmount = ctk.CTkLabel(self.__input, text= "Amount:", font = ("Poppins", 16), width = 150, height = 30, fg_color = "black", text_color= "white")
        self.__label_inputAmount.place( relx = 0.1, rely = 0.7, anchor = "w") 
        
        self.__entry_inputAmmount = ctk.CTkEntry(self.__input,height = 30, font = ("Poppins", 20), fg_color = "gray")
        self.__entry_inputAmmount.place( relx = 0.5, rely = 0.7, anchor = "w")
               
        
    
home = Home()
    
 