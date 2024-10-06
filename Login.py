import customtkinter as tk #This is a module that allows the developer to create GUI of tkinter but customizable
from PIL import Image #Allows the use of images as well as transparent background
from LoginSystem import LoginSystem

class Login_Interface(LoginSystem):#Login Interface meaing it has no functions yet please add functions 2nd developer

    def __init__(self):#The constructor by using tk.CTk() i can call root to all of the methods
        self.__root = tk.CTk()

    def Main_Window(self): #The main window it contains the log in interface along with functions which it still not have
        self.__root.title("Expense Tracker")
        self.__root.after(50, lambda: self.__get_fullsceen())
        self.__root.configure(fg_color = "black")
        self.__root.minsize(1400,650)
        self._center_frame()
        self.__root.mainloop()

    def __get_fullsceen(self):
        return self.__root.state("zoomed")
    
    def _center_frame(self):#It is the method that holds all of the frames
        self.__set_login_frame()
        self._set_left_frame()
        self._set_right_frame()
        self.__left_frame_contents()
        self.__rightframe_contents()

    def __get_root(self):#By encapsulating the root it prevents others from calling the root directly and changing it
        return self.__root
    
    def __set_login_frame(self):#It is the frame that holds all of the frame it is located at the middle of the window
        self.__loginframe = tk.CTkFrame(self.__get_root(), width=1400, height=650, fg_color = "#696969", corner_radius=0)
        self.__loginframe.place(relx= 0.5, rely= 0.5, anchor="center")
    
    def __get_login_frame(self):
        return self.__loginframe
    
    def _set_left_frame(self):
        self.__leftFrame = tk.CTkFrame(self.__get_login_frame(), width=700, height=650, fg_color= "#696969", corner_radius=0)
        self.__leftFrame.grid(row=0, column=0)
    
    def __get_left_frame(self):
        return self.__leftFrame
    
    def _set_right_frame(self):
        self.__rightFrame = tk.CTkFrame(self.__get_login_frame(), width=700, height=650, fg_color = "White" , corner_radius=0)
        self.__rightFrame.grid(row=0, column=1)
    
    def __get_right_frame(self):
        return self.__rightFrame
    
    def __left_frame_contents(self):
        self.__photo = tk.CTkImage(light_image=self.__get_image_logo(),
                     dark_image=self.__get_image_logo(),
                     size=(100, 100))
        self.__photoplacement = tk.CTkLabel(self.__get_left_frame(), image=self.__photo, text="", fg_color="#696969")
        self.__photoplacement.place(relx = 0.5, y = 10, anchor="n")  
        self.__get_username()
        self.__get_password()
        self.__get_hide_password()
        self.__get_login()
        self.__get_signup()
    
    def __get_username(self):
        self.__username = tk.CTkLabel(self.__get_left_frame(), text="Username:", font=("Poppins", 20), text_color= "white", fg_color="#696969")
        self.__username.place(relx= 0.5,x = -110, y = 130, anchor= "n")
        self.__username_entry = tk.CTkEntry(self.__get_left_frame(), width= 350, font=("Poppins", 20), corner_radius= 35, fg_color= "#2c2c2c", border_color= "#2c2c2c", border_width= 5, text_color="White", height=50)
        self.__username_entry.place(relx= 0.5, y = 160, anchor= "n")
    
    def __get_password(self):
        self.__password = tk.CTkLabel(self.__get_left_frame(), text="Password:", font=("Poppins", 20), text_color= "white", fg_color="#696969")
        self.__password.place(relx= 0.5,x = -110, y = 240, anchor= "n")
        self.__password_entry = tk.CTkEntry(self.__get_left_frame(), width= 350, font=("Poppins", 20), corner_radius= 35, fg_color= "#2c2c2c", border_color= "#2c2c2c", border_width= 5, text_color="White", show="*", height=50)
        self.__password_entry.place(relx= 0.5, y = 270, anchor= "n")

    def __get_show_password(self):
        self.__photo = tk.CTkImage(light_image=self.__get_image_show_password(),
                     dark_image=self.__get_image_show_password(),
                     size=(40, 25))
        self.__show_password = tk.CTkButton(self.__get_left_frame(), image=self.__photo, text="", fg_color="#2c2c2c", width= 10, border_width= 2, border_color= "#2c2c2c", corner_radius=10)
        self.__show_password.place(relx= 0.5, y = 275, anchor= "n", x = 220)

    def __get_hide_password(self):
        self.__photo = tk.CTkImage(light_image=self.__get_image_hide_password(),
                     dark_image=self.__get_image_hide_password(),
                     size=(50, 35))
        self.__show_password = tk.CTkButton(self.__get_left_frame(), image=self.__photo, text="", fg_color="#2c2c2c", width= 10, border_width= 2, border_color= "#2c2c2c", corner_radius=10)
        self.__show_password.place(relx= 0.5, y = 275, anchor= "n", x = 220)
    def __get_login(self):
        self.__login = tk.CTkButton(self.__get_left_frame(), text="Log-in", width= 200, height= 50, font=("Poppins", 20), fg_color= "#2c2c2c", text_color= "#e1e1e1", corner_radius= 50)
        self.__login.place(relx= 0.5, y = 380, anchor= "n")

    def __get_signup(self):
        self.__sign_up = tk.CTkButton(self.__get_left_frame(), text="Sign-Up", width= 350, height= 70, font=("Poppins", 20), fg_color= "#2c2c2c", text_color="#e1e1e1", corner_radius= 50)
        self.__sign_up.place(relx= 0.5, y = 480, anchor= "n")
        
    def __rightframe_contents(self):
        self.__photo = tk.CTkImage(light_image= self.__get_image_logo(),
                     dark_image= self.__get_image_logo(),
                     size=(200, 200))
        self.__photoplacement = tk.CTkLabel(self.__get_right_frame(), image=self.__photo, text="", fg_color="white")
        self.__photoplacement.place(relx= 0.5, rely= 0.5, anchor="center")

    def __get_image_logo(self):
        return Image.open("default.png").convert("RGBA")
    
    def __get_image_show_password(self):
        return Image.open("updateeye.png").convert("RGBA")
    
    def __get_image_hide_password(self):
        return Image.open("eye.png").convert("RGBA")
    
window = Login_Interface()
window.Main_Window()