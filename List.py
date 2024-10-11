import customtkinter as ctk
from PIL import Image
from tkinter import ttk
import os
class List:
    def __init__(self, parent):
        self.__parent = parent
        self.__root = ctk.CTkToplevel(self.__parent.GET_TL_Root())
        self.__root.protocol("WM_DELETE_WINDOW", self.TL_PROTOCOL_List)
        self.__root.withdraw()
        self.Main_Window()

    def TL_List_Show(self):
        self.__root.deiconify()
        self.__root.after(50, self.__root.state('zoomed'))

    def TL_PROTOCOL_List(self):
        self.__root.withdraw()

    def GET_TL_RootList(self):
        return self.__root
    
    def __get_main_window_width(self):
        return self.__get_frame_width(1)
    
    def __get_main_window_height(self):
        return self.__get_frame_height(1)
    
    def Main_Window(self):
        self.__root.title("Expense Tracker/List")
        # self.__root.after(50, lambda: self.__get_fullscreen())
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
    
    def __get_main_frame_width(self):
        return self.__get_frame_width(0.8)
    
    def __get_main_frame_height(self):
        return self.__get_frame_height(0.8)
    
    def __navigation_width(self):
        return self.__get_mainframe_width(0.8)
    
    def __navigation_height(self):
        return self.__get_mainframe_height(0.1)
    
    def __get_navigation_header_frame(self):
        return self.__navigation_header
    
    def __username_button_width(self):
        return self.__get_navigation_header_frame_width(0.35)
    
    def __list_button_width(self):
        return self.__get_navigation_header_frame_width(0.2)
    
    def __breakdown_button_width(self):
        return self.__get_navigation_header_frame_width(0.2)
    
    def __get_table_list_width(self):
        return self.__get_mainframe_width(0.8)
    
    def __get_table_list_height(self):
        return self.__get_mainframe_height(0.5)
    
    def _center_frame(self):#It is the method that holds all of the frames
        self.__set_main_frame()
        self.__navigation_header_frame()
        self.__table_list_frame()

    def __set_main_frame(self):
        self.__main_frame = ctk.CTkFrame(self.__get_root(), width=self.__get_main_frame_width(), height= self.__get_main_frame_height(), fg_color="#696969")
        self.__main_frame.place(relx = 0.5, rely = 0.5, anchor= "center")

    def __get_main_frame(self):
        return self.__main_frame
    
    def __navigation_header_frame(self):
        self.__navigation_header = ctk.CTkFrame(self.__get_main_frame(), width=self.__navigation_width(), height= self.__navigation_height(), fg_color="#696969")
        self.__navigation_header.place(relx = 0.5, rely = 0.025, anchor="n")
        self.__usernamebutton()
        self.__listbutton()
        self.__breakdownbutton()
    
    def __get_image_logo(self):
        return Image.open(self.GET_RELEVANT_PATHDIR('assets/logo.png')).convert("RGBA")
    
    def __usernamebutton(self):
        self.__name_pht = ctk.CTkImage(light_image = self.__get_name_logo(), dark_image = self.__get_name_logo(), size=(50,50))

        self.__username_button = ctk.CTkButton(self.__get_navigation_header_frame(),image = self.__name_pht, text="Name",width= self.__username_button_width(), height= 50, font=("Poppins",20),fg_color="grey")
        self.__username_button.place(relx=0.25, rely=0.5, anchor="center")
        self.__photo = ctk.CTkImage(light_image= self.__get_image_logo(),
                     dark_image= self.__get_image_logo(),
                     size=(70, 70))
        self.__photoplacement = ctk.CTkLabel(self.__get_navigation_header_frame(), image=self.__photo, text="", fg_color="#696969", corner_radius=10)
        self.__photoplacement.place(relx= 0.1, rely= 0.5, anchor="center")

    def __get_name_logo(self):
        return Image.open(self.GET_RELEVANT_PATHDIR('assets/profile2.png')).convert("RGBA")
    
    def __listbutton(self):
        self.__list_pht = ctk.CTkImage(light_image = self.__get_list_logo(), dark_image = self.__get_list_logo(), size=(40,40))

        self.__list_button = ctk.CTkButton(self.__get_navigation_header_frame(),image = self.__list_pht, text="List",width= self.__list_button_width(), height= 50, font=("Poppins",20), fg_color="#2c2c2c")
        self.__list_button.place(relx=0.6, rely=0.5, anchor="center")

    def __get_list_logo(self):
        return Image.open(self.GET_RELEVANT_PATHDIR('assets/list.png')).convert("RGBA")
    
    def __breakdownbutton(self):
        self.__breakdown_pht = ctk.CTkImage(light_image = self.__get_breakdown_logo(), dark_image = self.__get_breakdown_logo(), size=(40,40))

        self.__breakdown_button = ctk.CTkButton(self.__get_navigation_header_frame(), image = self.__breakdown_pht, text="breakdown",width= self.__breakdown_button_width(), height= 50, font=("Poppins",20), fg_color="grey")
        self.__breakdown_button.place(relx=0.85, rely=0.5, anchor="center")

    def __get_breakdown_logo(self):
        return Image.open(self.GET_RELEVANT_PATHDIR('assets/breakdown.png')).convert("RGBA")
    
    def __table_list_frame(self):
        self.__table_list = ctk.CTkFrame(self.__get_main_frame(), width=self.__get_table_list_width(), height= self.__get_table_list_height(), fg_color="#696969")
        self.__table_list.place(relx = 0.5, rely = 0.5, anchor="center")
        self.__table_needs()
        self.__table_wants()

    def __get_table_list_frame(self):
        return self.__table_list
    
    def __table_needs(self):
        self.__style_needs = ttk.Style()
        self.__style_needs.configure("Needs.Treeview", font=("Poppins", 20), rowheight=85, bordercolor="Black", borderwidth=2,background="black", fieldbackground="black", foreground="white")
        self.__style_needs.configure("Needs.Treeview.Heading", font=("Poppins", 25, "bold"),bordercolor="Black", borderwidth=2, padding=(5,10))
        self.__table_display_needs = ttk.Treeview(self.__get_table_list_frame(), columns=('id','col1', 'col2'),show= 'headings', style="Needs.Treeview")
        self.__table_display_needs.heading('id', text= 'ID')
        self.__table_display_needs.heading('col1', text= 'Needs')
        self.__table_display_needs.heading('col2', text= 'Amount')
        self.__table_display_needs.column('id', width= 50, stretch= False,anchor="center")
        self.__table_display_needs.column('col1', width= 100, stretch= True,anchor="center")
        self.__table_display_needs.column('col2', width= 100, stretch= True,anchor="center")
        self.__table_display_needs.place(relx=0.25, rely=0.1, relheight=1, relwidth= 0.4,anchor="n")
        self.__table_display_needs.insert('','end', values=('', '', '',))
        self.__table_display_needs.insert('','end', values=('', '', ''))
        self.__table_display_needs.bind("<ButtonPress-1>", self.handle_click_category_needs)

    def __table_wants(self):
        self.__style_wants = ttk.Style()
        self.__style_wants .configure("Wants.Treeview", font=("Poppins", 20), rowheight=85, bordercolor="Black", borderwidth=2,background="black", fieldbackground="black", foreground="white")
        self.__style_wants .configure("Wants.Treeview.Heading", font=("Poppins", 25, "bold"),bordercolor="Black", borderwidth=2, padding=(5,10))
        self.__table_display_wants = ttk.Treeview(self.__get_table_list_frame(), columns=('id','col3', 'col4'),show= 'headings', style="Wants.Treeview")
        self.__table_display_wants.heading('id', text= 'ID.')
        self.__table_display_wants.heading('col3', text= 'Wants')
        self.__table_display_wants.heading('col4', text= 'Amount')
        self.__table_display_wants.column('id', width= 50, stretch= False,anchor="center")
        self.__table_display_wants.column('col3', width= 100, stretch= True,anchor="center")
        self.__table_display_wants.column('col4', width= 100, stretch= True,anchor="center")
        self.__table_display_wants.place(relx=0.75, rely=0.1, relheight=1, relwidth= 0.4,anchor="n")
        self.__table_display_wants.insert('','end', values=('', '', ''))
        self.__table_display_wants.insert('','end', values=('', '', ''))
        self.__table_display_wants.bind("<ButtonPress-1>", self.handle_click_category_wants)

    def handle_click_category_needs(self, event):
        """Handle the click event for both preventing drag and clearing selection."""
        # Check if the click is on a separator (to prevent dragging)
        if self.__table_display_needs.identify_region(event.x, event.y) == "separator":
            return "break"  # Prevent dragging if clicked on a separator

        # Handle clearing selection on double click
        selected_item = self.__table_display_needs.selection()
        current_focus = self.__table_display_needs.focus()

        if selected_item:
            if current_focus == selected_item[0]:
                # Deselect if the same item is clicked again
                self.__table_display_needs.selection_remove(selected_item[0])
                self.__table_display_needs.selection_clear()
                return "break"  # Prevent any further processing

        # Update the last clicked item
        self.last_clicked_item = current_focus

    def handle_click_category_wants(self, event):
        """Handle the click event for both preventing drag and clearing selection."""
        # Check if the click is on a separator (to prevent dragging)
        if self.__table_display_wants.identify_region(event.x, event.y) == "separator":
            return "break"  # Prevent dragging if clicked on a separator

        # Handle clearing selection on double click
        selected_item = self.__table_display_wants.selection()
        current_focus = self.__table_display_wants.focus()

        if selected_item:
            if current_focus == selected_item[0]:
                # Deselect if the same item is clicked again
                self.__table_display_wants.selection_remove(selected_item[0])
                self.__table_display_wants.selection_clear()
                return "break"  # Prevent any further processing

        # Update the last clicked item
        self.last_clicked_item = current_focus

    def GET_RELEVANT_PATHDIR(self, IMAGENAME):
      path = os.path.dirname(os.path.abspath(__file__))
      return os.path.join(path, IMAGENAME)
# window = List()