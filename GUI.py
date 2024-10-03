import customtkinter as tk
from PIL import Image
#1536, 864

class Login_Interface:

    def __init__(self):
        self.root = tk.CTk()
        self.Main_Window(self.root)

    def Main_Window(self, root):
        self.root = root
        self.root.title("Expense Tracker")
        self.root.after(50, lambda: root.state("zoomed"))
        self.root.configure(fg_color = "black")
        self.center_frame(root)
        self.root.mainloop()

    def center_frame(self, root):
        self.root = root
        self.__set_login_frame(self.root)
        self.__set_left_frame()
        self.__set_right_frame()
        self.__left_frame_contents()
        self.__rightframe_contents()

    def __set_login_frame(self, root):
        self.root = root
        self.loginframe = tk.CTkFrame(self.root, width=1000, height=650, fg_color = "#696969", corner_radius=0)
        self.loginframe.place(relx= 0.5, rely= 0.5, anchor="center")
    
    def __get_login_frame(self):
        return self.loginframe
    
    def __set_left_frame(self):
        self.__leftFrame = tk.CTkFrame(self.__get_login_frame(), width=500, height=650, fg_color= "#696969", corner_radius=0)
        self.__leftFrame.grid(row=0, column=0)
    
    def __get_left_frame(self):
        return self.__leftFrame
    
    def __set_right_frame(self):
        self.__rightFrame = tk.CTkFrame(self.__get_login_frame(), width=500, height=650, fg_color = "White" , corner_radius=0)
        self.__rightFrame.grid(row=0, column=1)
    
    def __get_right_frame(self):
        return self.__rightFrame
    
    def __left_frame_contents(self):
        self.photo = tk.CTkImage(light_image=self.get_image(),
                     dark_image=self.get_image(),
                     size=(100, 100))
        self.photoplacement = tk.CTkLabel(self.__get_left_frame(), image=self.photo, text="", fg_color="#696969")
        self.photoplacement.place(relx = 0.5, y = 10, anchor="n")  
        self.__get_username()
        self.__get_password()
        self.__get_login()
        self.__get_signup()
    
    def __get_username(self):
        self.__username = tk.CTkLabel(self.__get_left_frame(), text="Username", font=("Poppins", 20), text_color= "white", fg_color="#696969")
        self.__username.place(relx= 0.5,x = -110, y = 130, anchor= "n")
        self.__username_entry = tk.CTkEntry(self.__get_left_frame(), width= 350, font=("Poppins", 50), corner_radius= 35, fg_color= "#2c2c2c", border_color= "#2c2c2c", border_width= 5)
        self.__username_entry.place(relx= 0.5, y = 160, anchor= "n")
    
    def __get_password(self):
        self.__password = tk.CTkLabel(self.__get_left_frame(), text="Password", font=("Poppins", 20), text_color= "white", fg_color="#696969")
        self.__password.place(relx= 0.5,x = -110, y = 240, anchor= "n")
        self.__password_entry = tk.CTkEntry(self.__get_left_frame(), width= 350, font=("Poppins", 50), corner_radius= 35, fg_color= "#2c2c2c", border_color= "#2c2c2c", border_width= 5)
        self.__password_entry.place(relx= 0.5, y = 270, anchor= "n")  

    def __get_login(self):
        self.__login = tk.CTkButton(self.__get_left_frame(), text="Log-in", width= 200, height= 50, font=("Poppins", 20), fg_color= "#2c2c2c", text_color= "#e1e1e1", corner_radius= 50)
        self.__login.place(relx= 0.5, y = 380, anchor= "n")

    def __get_signup(self):
        self.sign_up = tk.CTkButton(self.__get_left_frame(), text="Sign-Up", width= 350, height= 70, font=("Poppins", 20), fg_color= "#2c2c2c", text_color="#e1e1e1", corner_radius= 50)
        self.sign_up.place(relx= 0.5, y = 480, anchor= "n")
        
    def __rightframe_contents(self):
        self.photo = tk.CTkImage(light_image= self.get_image(),
                     dark_image= self.get_image(),
                     size=(200, 200))
        self.photoplacement = tk.CTkLabel(self.__get_right_frame(), image=self.photo, text="", fg_color="white")
        self.photoplacement.place(relx= 0.5, rely= 0.5, anchor="center")

    def get_image(self):
        return Image.open("default.png").convert("RGBA")
    
window = Login_Interface()