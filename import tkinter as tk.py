import tkinter as tk
import customtkinter as ctk  
from PIL import Image

class Registration_Interface:
    def __init__(self, root):
        self.root = root
        self.root.after(50, lambda: root.state("zoomed"))  
        
        self.__set_login_frame(root)
        self.__set_left_frame()
        self.__set_right_frame()

        self.is_student = tk.StringVar(value="No")
        self.has_kids = tk.StringVar(value="Without")

        self.create_registration_form()
        self.__rightframe_contents()  

    def __set_login_frame(self, root):
        self.loginframe = ctk.CTkFrame(root, width=1000, height=650, fg_color="#696969", corner_radius=0)
        self.loginframe.place(relx=0.5, rely=0.5, anchor="center")

    def __get_login_frame(self):
        return self.loginframe

    def __set_left_frame(self):
        self.__leftFrame = ctk.CTkFrame(self.__get_login_frame(), width=500, height=650, fg_color="#696969", corner_radius=0)
        self.__leftFrame.grid(row=0, column=0)

    def __get_left_frame(self):
        return self.__leftFrame

    def __set_right_frame(self):
        self.__rightFrame = ctk.CTkFrame(self.__get_login_frame(), width=500, height=650, fg_color="white", corner_radius=0)
        self.__rightFrame.grid(row=0, column=1)

    def __get_right_frame(self):
        return self.__rightFrame

    def create_registration_form(self):
        label_font = ("Poppins", 15)
        entry_width = 250

        tk.Label(self.__get_left_frame(), text="First Name", bg="#696969", fg="white", font=label_font).place(relx=0.2, rely=0.10, anchor="center")
        self.first_name = ctk.CTkEntry(self.__get_left_frame(), font=label_font, width=entry_width, corner_radius=35, fg_color="#2c2c2c", height=50, text_color="white")
        self.first_name.place(x=150, y=40)  

        tk.Label(self.__get_left_frame(), text="Last Name", bg="#696969", fg="white", font=label_font).place(relx=0.2, rely=0.19, anchor="center")
        self.last_name = ctk.CTkEntry(self.__get_left_frame(), font=label_font, width=entry_width, corner_radius=35, fg_color="#2c2c2c", height=50, text_color="white")
        self.last_name.place(x=150, y=100)  

        tk.Label(self.__get_left_frame(), text="Age", bg="#696969", fg="white", font=label_font).place(relx=0.2, rely=0.28, anchor="center")
        self.age = ctk.CTkEntry(self.__get_left_frame(), font=label_font, width=entry_width, corner_radius=35, fg_color="#2c2c2c", height=50, text_color="white")
        self.age.place(x=150, y=160)  

        tk.Label(self.__get_left_frame(), text="Address", bg="#696969", fg="white", font=label_font).place(relx=0.2, rely=0.37, anchor="center")
        self.address = ctk.CTkEntry(self.__get_left_frame(), font=label_font, width=entry_width, corner_radius=35, fg_color="#2c2c2c", height=50, text_color="white")
        self.address.place(x=150, y=220)  

        tk.Label(self.__get_left_frame(), text="Username", bg="#696969", fg="white", font=label_font).place(relx=0.2, rely=0.46, anchor="center")
        self.reg_username = ctk.CTkEntry(self.__get_left_frame(), font=label_font, width=entry_width, corner_radius=35, fg_color="#2c2c2c", height=50, text_color="white")
        self.reg_username.place(x=150, y=280)  

        tk.Label(self.__get_left_frame(), text="Password", bg="#696969", fg="white", font=label_font).place(relx=0.2, rely=0.56, anchor="center")
        self.reg_password = ctk.CTkEntry(self.__get_left_frame(), font=label_font, width=entry_width, corner_radius=35, fg_color="#2c2c2c", height=50, text_color="white")  
        self.reg_password.place(x=150, y=340)  

        tk.Label(self.__get_left_frame(), text="Student", bg="#696969", fg="white", font=label_font).place(relx=0.2, rely=0.65, anchor="center")
        tk.Label(self.__get_left_frame(), text="Kids", bg="#696969", fg="white", font=label_font).place(relx=0.2, rely=0.75, anchor="center")

        ctk.CTkCheckBox(self.__get_left_frame(), text="Yes", variable=self.is_student, onvalue="Yes", 
                offvalue="No", fg_color="#696969", text_color="white", 
                font=('Poppins', 25), height=50, width=30, border_width=2, corner_radius=0).place(x=160, y=400)

        ctk.CTkCheckBox(self.__get_left_frame(), text="No", variable=self.is_student, onvalue="No", 
                offvalue="Yes", fg_color="#696969", text_color="white", 
                font=('Poppins', 25), height=50, width=30, border_width=2, corner_radius=0).place(x=250, y=400)  

        ctk.CTkCheckBox(self.__get_left_frame(), text="With", variable=self.has_kids, onvalue="With", 
                offvalue="Without", fg_color="#696969", text_color="white", 
                font=('Poppins', 25), height=30, width=30, border_width=2, corner_radius=0).place(x=160, y=470)

        ctk.CTkCheckBox(self.__get_left_frame(), text="Without", variable=self.has_kids, onvalue="Without", 
                offvalue="With", fg_color="#696969", text_color="white", 
                font=('Poppins', 25), height=30, width=30, border_width=2, corner_radius=0).place(x=250, y=470)

        ctk.CTkButton(self.__get_left_frame(), text="Sign-Up", fg_color="#2c2c2c", text_color="white", 
                      font=label_font, corner_radius=35, height=50, width=entry_width).place(x=115, y=540)

    def __rightframe_contents(self):
        self.photo = ctk.CTkImage(light_image=self.get_image(),
                                   dark_image=self.get_image(),
                                   size=(200, 200))
        self.photoplacement = ctk.CTkLabel(self.__get_right_frame(), image=self.photo, text="", fg_color="white")
        self.photoplacement.place(relx=0.5, rely=0.5, anchor="center")

    def get_image(self):
        return Image.open("default.png").convert("RGBA")

if __name__ == "__main__":
    root = tk.Tk()
    window = Registration_Interface(root)
    root.mainloop()
