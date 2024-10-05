import customtkinter as tk
from PIL import Image
#1536, 864

class Login_Interface:

    def Main_Window(self, root):
        self.root = root
        self.root.title("Expense Tracker")
        self.root.after(50, lambda: root.state("zoomed"))
        self.root.configure(fg_color = "black")
        self.center_frame(root)
        self.root.mainloop()

    def center_frame(self, root):
        self.root = root
        self.loginframe = tk.CTkFrame(self.root, width=1000, height=650, fg_color = "#696969", corner_radius=0)
        self.loginframe.place(relx= 0.5, rely= 0.5, anchor="center")
        self.leftFrame = tk.CTkFrame(self.loginframe, width=500, height=650, fg_color= "#696969", corner_radius=0)
        self.leftFrame.grid(row=0, column=0)
        self.rightFrame = tk.CTkFrame(self.loginframe, width=500, height=650, fg_color = "White" , corner_radius=0)
        self.rightFrame.grid(row=0, column=1)
        self.left_frame_contents(self.leftFrame)
        self.rightframe_contents(self.rightFrame)

    def left_frame_contents(self, leftFrame):
        self.leftFrame = leftFrame
        self.photo_image = Image.open("logo.png").convert("RGBA")
        self.photo = tk.CTkImage(light_image=self.photo_image,
                     dark_image=self.photo_image,
                     size=(100, 100))
        self.photoplacement = tk.CTkLabel(self.leftFrame, image=self.photo, text="", fg_color="#696969")
        self.photoplacement.place(relx = 0.5, y = 10, anchor="n")
        self.username = tk.CTkLabel(self.leftFrame, text="Username", font=("Poppins", 20), text_color= "white", fg_color="#696969")
        self.username.place(relx= 0.5,x = -110, y = 130, anchor= "n")
        self.username_entry = tk.CTkEntry(self.leftFrame, width= 350, font=("Poppins", 50), corner_radius= 35, fg_color= "#2c2c2c", border_color= "#2c2c2c", border_width= 5)
        self.username_entry.place(relx= 0.5, y = 160, anchor= "n")  
        self.password = tk.CTkLabel(self.leftFrame, text="Password", font=("Poppins", 20), text_color= "white", fg_color="#696969")
        self.password.place(relx= 0.5,x = -110, y = 240, anchor= "n")
        self.password_entry = tk.CTkEntry(self.leftFrame, width= 350, font=("Poppins", 50), corner_radius= 35, fg_color= "#2c2c2c", border_color= "#2c2c2c", border_width= 5)
        self.password_entry.place(relx= 0.5, y = 270, anchor= "n")  
        self.login = tk.CTkButton(self.leftFrame, text="Log-in", width= 200, height= 50, font=("Poppins", 20), fg_color= "#2c2c2c", text_color= "#e1e1e1", corner_radius= 50, hover_color = "purple")
        self.login.place(relx= 0.5, y = 380, anchor= "n")
        self.sign_up = tk.CTkButton(self.leftFrame, text="Sign-Up", width= 350, height= 70, font=("Poppins", 20), fg_color= "#2c2c2c", text_color="#e1e1e1", corner_radius= 50, hover_color = "purple")
        self.sign_up.place(relx= 0.5, y = 480, anchor= "n")
    
    def rightframe_contents(self, rightFrame):
        self.rightFrame = rightFrame
        self.photo_image = Image.open("logo.png").convert("RGBA")
        self.photo = tk.CTkImage(light_image= self.photo_image,
                     dark_image= self.photo_image,
                     size=(200, 200))
        self.photoplacement = tk.CTkLabel(self.rightFrame, image=self.photo, text="", fg_color="white")
        self.photoplacement.place(relx= 0.5, rely= 0.5, anchor="center")
root = tk.CTk()
window = Login_Interface()
window.Main_Window(root)