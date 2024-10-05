import customtkinter as tk

class YourApp:
    def center_frame(self, root):
        self.root = root
       
        self.loginframe = tk.CTkFrame(self.root, width=1000, height=650, fg_color="#696969", corner_radius=0)
        self.loginframe.place(relx=0.5, rely=0.5, anchor="center")

        self.canvas = tk.CTkCanvas(self.loginframe, width=1000, height=650, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self.create_radial_gradient()

        self.leftFrame = tk.CTkFrame(self.loginframe, width=500, height=650, fg_color="#696969", corner_radius=0)
        self.leftFrame.pack(side="left", fill="both", expand=True)
        
        self.rightFrame = tk.CTkFrame(self.loginframe, width=500, height=650, fg_color="White", corner_radius=0)
        self.rightFrame.pack(side="right", fill="both", expand=True)

        self.left_frame_contents(self.leftFrame)
        self.right_frame_contents(self.rightFrame)

    def create_radial_gradient(self):
        width = 1000
        height = 650
        center_x = width // 2
        center_y = height // 2
        max_radius = min(center_x, center_y)

        for radius in range(max_radius, 0, -1):
            ratio = radius / max_radius

            r = int(128 * (1 - ratio))  
            g = int(128 * (1 - ratio))  
            b = int(128 * (1 - ratio))  
            
            color = f'#{r:02x}{g:02x}{b:02x}'
            
            self.canvas.create_oval(center_x - radius, center_y - radius, center_x + radius, center_y + radius, fill=color, outline="")

    def left_frame_contents(self, frame):
        
        pass

    def right_frame_contents(self, frame):
        
        pass

if __name__ == "__main__":
    root = tk.CTk()
    app = YourApp()
    app.center_frame(root)
    root.mainloop()