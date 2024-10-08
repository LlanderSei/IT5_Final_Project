import customtkinter as ctk 
from LoginSystem import LoginSystem
from PIL import Image

class Registration_Interface(LoginSystem):
    def __init__(self, parent):
        self.__parent = parent
        self.__root = ctk.CTkToplevel(self.__parent)
        self.__root.protocol("WM_DELETE_WINDOW", self.__on_close)
        self.Main_Window()

    def __on_close(self):
        self.__parent.quit()
        self.__parent.destroy()
        self.__root.destroy()
            
    def Main_Window(self):
        self.__root.title("Expense Tracker")
        self.__root.after(50, lambda: self.__get_fullscreen())
        self.__root.configure(fg_color = "black")
        self.__root.minsize(1400,650)
        self._center_frame()
     
    def __get_fullscreen(self):
        return self.__root.state("zoomed")
    
    def _center_frame(self):
        self.__set_registration_frame()
        self._set_left_frame()
        self._set_right_frame()

        self.__is_student = ctk.StringVar(value="No")
        self.__has_kids = ctk.StringVar(value="Without")

        self.create_registration_form()
        self.__rightframe_contents()  
    
    def __get_frame_width(self, percentage):
        return int(self.__root.winfo_screenwidth() * percentage)

    def __get_loginframe_width(self):
        return self.__get_frame_width(0.8)

    def __get_leftframe_width(self):
        return self.__get_frame_width(0.45)

    def __get_rightframe_width(self):
        return self.__get_frame_width(0.45)
    

    def __set_registration_frame(self):
        self.__registrationframe = ctk.CTkFrame(self.__root, width=self.__get_loginframe_width(), height=650, fg_color="#696969", corner_radius=0)
        self.__registrationframe.place(relx=0.5, rely=0.5, anchor="center")

    def __get_registration_frame(self):
        return self.__registrationframe

    def _set_left_frame(self):
        self.__leftFrame = ctk.CTkFrame(self.__get_registration_frame(), width=self.__get_leftframe_width(), height=650, fg_color="#696969", corner_radius=0)
        self.__leftFrame.grid(row=0, column=0)

    def __get_left_frame(self):
        return self.__leftFrame

    def _set_right_frame(self):
        self.__rightFrame = ctk.CTkFrame(self.__get_registration_frame(), width=self.__get_rightframe_width(), height=650, fg_color="white", corner_radius=0)
        self.__rightFrame.grid(row=0, column=1)

    def __get_right_frame(self):
        return self.__rightFrame

    def __get_font(self):
        return ("Poppins", 20)
    
    def __get_entry_width(self):
        return 250
    
    def create_registration_form(self):
        self.__set_first_name()
        self.__set_last_name()
        self.__set_age()
        self.__set_address()
        self.__set_username()
        self.__set_password()
        self.__get_hide_password()
        self.__set_students()
        self.__set_kids()
        self.__set_signup()

    def __set_first_name(self):
        self.__first_name = ctk.CTkLabel(self.__get_left_frame(), text="First Name", fg_color="#696969", text_color="white", font=self.__get_font())
        self.__first_name.place(relx= 0.2, y=30, anchor="n")
        self.__first_name_entry = ctk.CTkEntry(self.__get_left_frame(), font=self.__get_font(), width=self.__get_entry_width(), corner_radius=35, fg_color="#2c2c2c", height=50, text_color="white", border_color= "#2c2c2c")
        self.__first_name_entry.place(relx = 0.5, y= 20, anchor="n")  
           
    def __set_last_name(self):
        self.__last_name = ctk.CTkLabel(self.__get_left_frame(), text="Last Name", fg_color="#696969", text_color="white", font=self.__get_font())
        self.__last_name.place(relx=0.2, y=90, anchor="n")
        self.__last_name_entry = ctk.CTkEntry(self.__get_left_frame(), font=self.__get_font(), width=self.__get_entry_width(), corner_radius=35, fg_color="#2c2c2c", height=50, text_color="white", border_color= "#2c2c2c")
        self.__last_name_entry.place(relx = 0.5, y=80,anchor="n")  
    
    def __set_age(self):
        self.__age = ctk.CTkLabel(self.__get_left_frame(), text="Age", fg_color="#696969", text_color="white", font=self.__get_font())
        self.__age.place(relx=0.2, y=150, anchor="n")
        self.__age_entry = ctk.CTkEntry(self.__get_left_frame(), font=self.__get_font(), width=self.__get_entry_width(), corner_radius=35, fg_color="#2c2c2c", height=50, text_color="white", border_color= "#2c2c2c")
        self.__age_entry.place(relx = 0.5, y=140,anchor="n")  
    
    def __set_address(self):
        self.__address = ctk.CTkLabel(self.__get_left_frame(), text="Address", fg_color="#696969", text_color="white", font=self.__get_font())
        self.__address.place(relx=0.2, y=210, anchor="n")
        self.__address_entry = ctk.CTkEntry(self.__get_left_frame(), font=self.__get_font(), width=self.__get_entry_width(), corner_radius=35, fg_color="#2c2c2c", height=50, text_color="white", border_color= "#2c2c2c")
        self.__address_entry.place(relx = 0.5, y=200,anchor="n")  
    
    def __set_username(self):
        self.__reg_username = ctk.CTkLabel(self.__get_left_frame(), text="Username", fg_color="#696969", text_color="white", font=self.__get_font())
        self.__reg_username.place(relx=0.2, y=270, anchor="n")
        self.__reg_username_entry = ctk.CTkEntry(self.__get_left_frame(), font=self.__get_font(), width=self.__get_entry_width(), corner_radius=35, fg_color="#2c2c2c", height=50, text_color="white", border_color= "#2c2c2c")
        self.__reg_username_entry.place(relx = 0.5, y=260,anchor="n")  
    
    def __set_password(self):
        self.__reg_password = ctk.CTkLabel(self.__get_left_frame(), text="Password", fg_color="#696969", text_color="white", font=self.__get_font())
        self.__reg_password.place(relx=0.2, y=330, anchor="n")
        self.__reg_password_entry = ctk.CTkEntry(self.__get_left_frame(), font=self.__get_font(), width=self.__get_entry_width(), corner_radius=35, fg_color="#2c2c2c", height=50, text_color="white", border_color= "#2c2c2c", show="*")  
        self.__reg_password_entry .place(relx = 0.5, y=320,anchor="n")
    
    def __set_students(self):
        self.__students = ctk.CTkLabel(self.__get_left_frame(), text="Student", fg_color="#696969", text_color="white", font=self.__get_font())
        self.__students.place(relx=0.2, y=390, anchor="n")
        self.__students_checkbox_yes = ctk.CTkCheckBox(self.__get_left_frame(), text="Yes", variable=self.__is_student, onvalue="Yes", 
                offvalue="No", fg_color="#696969", text_color="white", 
                font=('Poppins', 25), height=50, width=30, border_width=2, corner_radius=0, border_color= "#2c2c2c")
        self.__students_checkbox_yes.place(relx=0.4, y=380,anchor="n")

        self.__students_checkbox_no = ctk.CTkCheckBox(self.__get_left_frame(), text="No", variable=self.__is_student, onvalue="No", 
                offvalue="Yes", fg_color="#696969", text_color="white", 
                font=('Poppins', 25), height=50, width=30, border_width=2, corner_radius=0, border_color= "#2c2c2c")
        self.__students_checkbox_no.place(relx = 0.5, y=380,anchor="n", x=42.5)  

    def __set_kids(self):
        self.__kids = ctk.CTkLabel(self.__get_left_frame(), text="Kids", fg_color="#696969", text_color="white", font=self.__get_font())
        self.__kids.place(relx=0.2, y=450, anchor="n")

        
        self.__kids_checkbox_yes = ctk.CTkCheckBox(self.__get_left_frame(), text="With", variable=self.__has_kids, onvalue="With", 
                offvalue="Without", fg_color="#696969", text_color="white", 
                font=('Poppins', 25), height=30, width=30, border_width=2, corner_radius=0, border_color= "#2c2c2c")
        self.__kids_checkbox_yes.place(relx=0.4, y=440,anchor="n", x=5)

        self.__kids_checkbox_no = ctk.CTkCheckBox(self.__get_left_frame(), text="Without", variable=self.__has_kids, onvalue="Without", 
                offvalue="With", fg_color="#696969", text_color="white", 
                font=('Poppins', 25), height=30, width=30, border_width=2, corner_radius=0 , border_color= "#2c2c2c")
        self.__kids_checkbox_no.place(relx=0.6, y=440,anchor="n")
    
    def __set_signup(self):
        self.__signup = ctk.CTkButton(self.__get_left_frame(), text="Sign-Up", fg_color="#2c2c2c", text_color="white", 
                      font=self.__get_font(), corner_radius=35, height=50, width=self.__get_entry_width())
        self.__signup.place(relx=0.5, y=500,anchor="n")

    def __rightframe_contents(self):
        self.__photo = ctk.CTkImage(light_image=self.get_image(),
                                   dark_image=self.get_image(),
                                   size=(200, 200))
        self.__photoplacement = ctk.CTkLabel(self.__get_right_frame(), image=self.__photo, text="", fg_color="white")
        self.__photoplacement.place(relx=0.5, rely=0.5, anchor="center")

    def get_image(self):
        return Image.open("default.png").convert("RGBA")

    def __get_image_show_password(self):
        return Image.open("updateeye.png").convert("RGBA")
    
    def __get_image_hide_password(self):
        return Image.open("eye.png").convert("RGBA")
    
    def __get_show_password(self):
        self.__photo = ctk.CTkImage(light_image=self.__get_image_show_password(),
                     dark_image=self.__get_image_show_password(),
                     size=(40, 25))
        self.__show_password = ctk.CTkButton(self.__get_left_frame(), image=self.__photo, text="", fg_color="#2c2c2c", width= 10, border_width= 2, border_color= "#2c2c2c", corner_radius=10)
        self.__show_password.place(relx= 0.5, y = 330, anchor= "n", x = 180)

    def __get_hide_password(self):
        self.__photo = ctk.CTkImage(light_image=self.__get_image_hide_password(),
                     dark_image=self.__get_image_hide_password(),
                     size=(40, 25))
        self.__show_password = ctk.CTkButton(self.__get_left_frame(), image=self.__photo, text="", fg_color="#2c2c2c", width= 10, border_width= 2, border_color= "#2c2c2c", corner_radius=10)
        self.__show_password.place(relx= 0.5, y = 330, anchor= "n", x = 180)
