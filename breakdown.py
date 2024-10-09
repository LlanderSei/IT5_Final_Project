import tkinter as tk
import customtkinter as ctk  
from tkinter import ttk
from PIL import Image
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
    
    def __get_navigation_frame_width(self, percentage):
        return int(self.__navigation_header.winfo_screenheight() * percentage)
    
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
        return self.__get_frame_width(0.8)
    
    def __get_main_frame_height(self):
        return self.__get_frame_height(0.8)
    
    def __set_main_frame(self):
        self.__main_frame = ctk.CTkFrame(self.__get_root(), width=self.__get_main_frame_width(), height= self.__get_main_frame_height(), fg_color="#696969")
        self.__main_frame.place(relx = 0.5, rely=0.5, anchor= "center")

    def __get_main_frame(self):
        return self.__main_frame
    
    def __get_navigation_frame(self):
        return self.__navigation_header
    
    def __get_category_table_frame(self):
        return self.__category_table
    
    def __get_savings_table_frame(self):
        return self.__saving_table
    
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
    
    def __username_button_width(self):
        return self.__get_navigation_frame_width(0.35)
    
    def __list_button_width(self):
        return self.__get_navigation_frame_width(0.2)
    
    def __breakdown_button_width(self):
        return self.__get_navigation_frame_width(0.2)
    
    def __navigation_frames(self):
        self.__navigation_header = ctk.CTkFrame(self.__get_main_frame(), width=self.__navigation_width(), height= self.__navigation_height(), fg_color="#696969")
        self.__navigation_header.place(relx = 0.5, rely = 0.025, anchor="n")
        self.__usernamebutton()
        self.__listbutton()
        self.__breakdownbutton()

    def __category_table_frames(self):
        self.__category_table = ctk.CTkFrame(self.__get_main_frame(), width=self.__category_width(), height= self.__category_height(), fg_color="#696969")
        self.__category_table.place(relx = 0.5, rely = 0.4, anchor="center")
        self.__category()

    def __savings_table_frames(self):
        self.__saving_table = ctk.CTkFrame(self.__get_main_frame(), width=self.__saving_width(), height= self.__saving_height(), fg_color="#696969")
        self.__saving_table.place(relx = 0.5, rely = 0.6, anchor="n")
        self.__savings()
    
    def __get_image_logo(self):
        return Image.open("default.png").convert("RGBA")
    
    def __usernamebutton(self):
        self.__username_button = ctk.CTkButton(self.__get_navigation_frame(), text="Name",width= self.__username_button_width(), height= 50, font=("Poppins",20),fg_color="grey")
        self.__username_button.place(relx=0.25, rely=0.5, anchor="center")
        self.__photo = ctk.CTkImage(light_image= self.__get_image_logo(),
                     dark_image= self.__get_image_logo(),
                     size=(70, 70))
        self.__photoplacement = ctk.CTkLabel(self.__get_navigation_frame(), image=self.__photo, text="", fg_color="#696969", corner_radius=10)
        self.__photoplacement.place(relx= 0.1, rely= 0.5, anchor="center")

    def __listbutton(self):
        self.__list_button = ctk.CTkButton(self.__get_navigation_frame(), text="List",width= self.__list_button_width(), height= 50, font=("Poppins",20), fg_color="grey")
        self.__list_button.place(relx=0.6, rely=0.5, anchor="center")

    def __breakdownbutton(self):
        self.__breakdown_button = ctk.CTkButton(self.__get_navigation_frame(), text="breakdown",width= self.__breakdown_button_width(), height= 50, font=("Poppins",20), fg_color="#2c2c2c")
        self.__breakdown_button.place(relx=0.85, rely=0.5, anchor="center")

    def __category(self):
        self.__style_category = ttk.Style()
        self.__style_category.configure("Category.Treeview", font=("Poppins", 20), bordercolor="Black", borderwidth=5, rowheight=130, background="#696969", fieldbackground="#696969", foreground="black")
        self.__style_category.configure("Category.Treeview.Heading", font=("Poppins", 25, "bold"),
                                        padding=(5,10),
                                        bordercolor="Black",
                                        borderwidth=2,
                                        foreground="black",
                                        )
        self.__category_table_display = ttk.Treeview(self.__get_category_table_frame(), columns= ('Category', 'Total', 'Budget', 'Remaining'), show= 'headings', height=2, style="Category.Treeview")
        self.__category_table_display.heading('Category', text= 'Category')
        self.__category_table_display.heading('Total', text= 'Total')
        self.__category_table_display.heading('Budget', text= 'Budget')
        self.__category_table_display.heading('Remaining', text= 'Remaining')
        self.__category_table_display.column('Category', width= 100, stretch= True, anchor="center")
        self.__category_table_display.column('Total', width= 100, stretch= True, anchor="center")
        self.__category_table_display.column('Budget', width= 100, stretch= True, anchor="center")
        self.__category_table_display.column('Remaining', width= 100, stretch= True, anchor="center")
        self.__category_table_display.insert('','end', values=('Needs', '', '', ''))
        self.__category_table_display.insert('','end', values=('Wants', '', '', ''))
        self.__category_table_display.place(relx=0.5, rely=0.5, relheight=1, relwidth= 1,anchor="center")
        self.__category_table_display.bind("<ButtonPress-1>", self.prevent_drag_category)
        self.__category_table_display.bind("<ButtonPress-1>", self.clear_selection_on_double_click_category)
    def clear_selection_on_double_click_category(self, event):
        """Handle clearing selection if the same row is clicked twice."""
        selected_item = self.__category_table_display.selection()
        if selected_item:
            # Check if the item clicked is already selected
            current_focus = self.__category_table_display.focus()
            if current_focus == selected_item[0]:
                # Deselect if the same item is clicked again
                self.__category_table_display.selection_remove(selected_item[0])
                self.__category_table_display.selection_clear()

    def clear_selection_on_double_click_savings(self, event):
        """Handle clearing selection if the same row is clicked twice."""
        selected_item = self.__savings_table_display.selection()
        if selected_item:
            # Check if the item clicked is already selected
            current_focus = self.__savings_table_display.focus()
            if current_focus == selected_item[0]:
                # Deselect if the same item is clicked again
                self.__savings_table_display.selection_remove(selected_item[0])
                self.__savings_table_display.selection_clear()
                
    def prevent_drag_category(self,event):
        if self.__category_table_display.identify_region(event.x, event.y) == "separator":
    
            return "break"
    def prevent_drag_savings(self,event):   
        if self.__savings_table_display.identify_region(event.x, event.y) == "separator":
            return "break"

    def __savings(self):
        self.__style_savings = ttk.Style()
        self.__style_savings.configure("Savings.Treeview", font=("Poppins", 20), rowheight=85, bordercolor="Black", borderwidth=2,background="black", fieldbackground="black", foreground="white")
        self.__style_savings.configure("Savings.Treeview.Heading", font=("Poppins", 25, "bold"),bordercolor="Black", borderwidth=2, padding=(5,10))
        self.__savings_table_display = ttk.Treeview(self.__get_savings_table_frame(), columns= ('Savings', 'Amount'), show= 'headings', height=3, style="Savings.Treeview")
        self.__savings_table_display.heading('Savings', text= 'Savings')
        self.__savings_table_display.heading('Amount', text= 'Amount')
        self.__savings_table_display.column('Savings', width= 100, stretch= True,anchor="center")
        self.__savings_table_display.column('Amount', width= 100, stretch= True, anchor="center")
        self.__savings_table_display.place(relx=0.5, rely=0.5, relheight=1, relwidth= 1,anchor="center")
        self.__savings_table_display.insert('','end', values=('Savings:', ''))
        self.__savings_table_display.insert('','end', values=('Total Expenses:', ''))
        self.__savings_table_display.insert('','end', values=('Remaining:', ''))
        self.__savings_table_display.bind("<ButtonPress-1>", self.prevent_drag_savings)
        self.__savings_table_display.bind("<ButtonPress-1>", self.clear_selection_on_double_click_savings)
window = Breakdown()
