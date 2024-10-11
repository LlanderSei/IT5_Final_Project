from customtkinter import *
import customtkinter as ctk
from PIL import Image
import os
from List import List
from Breakdown import Breakdown
from tkinter import messagebox as MSGBOX

class Home:
    def __init__(self, SUBPARENT, MAIN):
        self.__PT = MAIN
        self.__SP = SUBPARENT

        self.__root = ctk.CTkToplevel(self.__PT.GET_RootWindowObject())
        self.__root.protocol("WM_DELETE_WINDOW", self.TL_PROTOCOL_Home)
        self.__root.withdraw()

        self.__List = List(self, self.__SP)
        self.__Breakdown = Breakdown(self, self.__SP)
        
        
        self.__INITIATE_OBJECTS()
        self.Main_Window()
        # self.__root.mainloop()

    def TL_PROTOCOL_Home(self):
        self.__root.withdraw()
        self.__List.GET_TL_RootList().withdraw()
        self.__Breakdown.TL_Get_Root_Breakdown().withdraw()
        self.__PT.GET_RootWindowObject().deiconify()
    
    def GET_TL_Root(self):
        return self.__root
    
    def __INITIATE_OBJECTS(self):
        self.__PROFILENAME = ctk.StringVar()
        self.__ADD_SAVINGS = ctk.StringVar()
        self.__SAVINGS = ctk.StringVar()
        self.__STIPEND = ctk.StringVar()
        self.__MONTH_OF = ctk.StringVar()
        self.__BUDGET_NEEDS = ctk.StringVar()
        self.__BUDGET_WANTS = ctk.StringVar()
        self.__NOTES = ctk.StringVar()

        self.__EXPCATEGORY = ctk.StringVar(value= 'Needs')
        self.__EXPENDITURES = ctk.StringVar()
        self.__EXPAMOUNT = ctk.StringVar()

        self.__root.bind('<KeyPress>', self.ROOT_EVT_KeyPressed)

    def Update_Infos(self, INFO):
        match INFO:
            case 'PROFILENAME': return self.__PROFILENAME
            case 'ADDSAVINGS': return self.__ADD_SAVINGS
            case 'SAVINGS': return self.__SAVINGS
            case 'STIPEND': return self.__STIPEND
            case 'MONTHOF': return self.__MONTH_OF
            case 'BUDGETNEEDS': return self.__BUDGET_NEEDS
            case 'BUDGETWANTS': return self.__BUDGET_WANTS
            case 'NOTES': return self.__NOTES
    
    def ROOT_EVT_KeyPressed(self, EVT):
        self.__SP.UPDATE_UserDetails()

    def ADD_Objectives(self):
        if not self.__EXPENDITURES.get(): MSGBOX.showerror('ERROR', 'Expenditures cannot be empty!', parent=self.__root); return 0
        if not self.__EXPAMOUNT.get(): MSGBOX.showerror('ERROR', 'Amount cannot be empty!', parent=self.__root); return 0

        RESULT = self.__SP.ADD_List(self.__EXPCATEGORY.get(), self.__EXPENDITURES.get(), float(self.__EXPAMOUNT.get()))
        if RESULT == 'ADDSUCCESS': MSGBOX.showinfo('Item Added', 'Item successfully added.')

    def VMCD_Entry_OnlyFloat(self, VALUE):
        if VALUE == '': return True
        if VALUE.replace('.', '', 1).isdigit() and VALUE.count('.') <= 1: return True
        return False

    def TL_LIST_Return_Variables(self, OBJECT):
        return self.__List.TL_LIST_Return_Variables(OBJECT)

    def __get_main_window_width(self):
        return self.__get_frame_width(0.8)
    
    def __get_main_window_height(self):
        return self.__get_frame_height(0.8)
    
    def Main_Window(self):
        self.__root.title("Expense Tracker/Home")
        self.__root.configure(fg_color = "black")
        self.__root.minsize(self.__get_main_window_width(),self.__get_main_window_height())
        self._center_frame()
     
    def get_fullscreen(self):
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
        return self.__get_frame_width(0.8)
    
    def __get_main_frame_height(self):
        return self.__get_frame_height(0.8)
    
    def __navigation_width(self):
        return self.__get_mainframe_width(0.8)
    
    def __navigation_height(self):
        return self.__get_mainframe_height(0.1)
    
    def __get_navigation_header_frame(self):
        return self.__navigation_header
    
    def __get_navigation_footer_frame(self):
        return self.__navigation_footer
    
    def __income_width(self):
        return self.__get_mainframe_width(0.25)
    
    def __income_height(self):
        return self.__get_mainframe_height(0.3)
    
    def __category_width(self):
        return self.__get_mainframe_width(0.250)
    
    def __category_height(self):
        return self.__get_mainframe_height(0.3)
    
    def __note_width(self):
        return self.__get_mainframe_width(0.35)

    def __note_height(self):
        return self.__get_mainframe_height(0.3)
    
    def __inputs_width(self):
        return self.__get_mainframe_width(0.3)

    def __inputs_height(self):
        return self.__get_mainframe_height(0.3)
    
    def __username_button_width(self):
        return self.__get_navigation_header_frame_width(0.35)
    
    def __list_button_width(self):
        return self.__get_navigation_header_frame_width(0.275)
    
    def __breakdown_button_width(self):
        return self.__get_navigation_header_frame_width(0.275)
    
    def _center_frame(self):#It is the method that holds all of the frames
        self.__set_main_frame()
        self.__navigation_header_frame()
        self.__navigation_footer_frame()
        self.__income_frame()
        self.__category_frame()
        self.__note_frame()
        self.__inputs_frame()

    def __set_main_frame(self):
        self.__main_frame = ctk.CTkFrame(self.__get_root(), width=self.__get_main_frame_width(), height= self.__get_main_frame_height(), fg_color="#696969")
        self.__main_frame.place(relx = 0.5, rely = 0.5 ,anchor= "center")

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
        
        self.__username_button = ctk.CTkButton(self.__get_navigation_header_frame(), image = self.__name_pht, text = "Name",width = self.__username_button_width(), height = 60, font = ("Poppins",23, "bold"),fg_color ="#2c2c2c", textvariable=self.__PROFILENAME, corner_radius= 25)
        self.__username_button.place(relx=0.25, rely=0.5, anchor="center")
        self.__photo = ctk.CTkImage(light_image= self.__get_image_logo(),
                     dark_image= self.__get_image_logo(),
                     size=(70, 70))
        self.__photoplacement = ctk.CTkLabel(self.__get_navigation_header_frame(), image=self.__photo, text="", fg_color="#696969")
        self.__photoplacement.place(relx= 0.05, rely= 0.5, anchor="center")

    def __get_name_logo(self):
        return Image.open(self.GET_RELEVANT_PATHDIR('assets/profile2.png')).convert("RGBA")

    def __listbutton(self):
        self.__list_pht = ctk.CTkImage(light_image = self.__get_list_logo(), dark_image = self.__get_list_logo(), size=(40,40))
        
        self.__list_button = ctk.CTkButton(self.__get_navigation_header_frame(), image = self.__list_pht, text = "List", corner_radius = 25, width= self.__list_button_width(), height= 50, font=("Poppins",23, "bold"), fg_color="#696969",border_width = 3,border_color = "#000000", command=lambda: self.__List.TL_List_Show())
        self.__list_button.place(relx=0.59, rely=0.5, anchor="center")

    def __get_list_logo(self):
        return Image.open(self.GET_RELEVANT_PATHDIR('assets/list.png')).convert("RGBA")

    def __breakdownbutton(self):
        self.__breakdown_pht = ctk.CTkImage(light_image = self.__get_breakdown_logo(), dark_image = self.__get_breakdown_logo(), size=(40,40))
        
        self.__breakdown_button = ctk.CTkButton(self.__get_navigation_header_frame(), image = self.__breakdown_pht, text = "Breakdown", corner_radius = 25, width = self.__breakdown_button_width(), height= 50, font=("Poppins",23, "bold"), fg_color="#696969",border_width = 3,border_color = "#000000", command=lambda: self.__Breakdown.TL_Breakdown_Show())
        self.__breakdown_button.place(relx = 0.830, rely = 0.5, anchor = "center")
    
    def __get_breakdown_logo(self):
        return Image.open(self.GET_RELEVANT_PATHDIR('assets/breakdown.png')).convert("RGBA")
    
    def __navigation_footer_frame(self):
        self.__navigation_footer = ctk.CTkFrame(self.__get_main_frame(), width= self.__note_width(), height= self.__note_height(), fg_color="#696969")
        self.__navigation_footer.place(relx = 0.75, rely = 0.973, y = -25,anchor="s")
        self.__Logout()
        self.__View_Profile()
        self.__add()
        self.__update()
        self.__delete()
    
    def __get_navigation_footer_width(self):
        return self.__get_navigation_footer_frame_width(0.2)
    
    def __Logout(self):
        self.__logout_pht = ctk.CTkImage(light_image = self.__get_logout_logo(), dark_image = self.__get_logout_logo(), size=(30,30))
        
        self.__logout_button = ctk.CTkButton(self.__get_navigation_footer_frame(), image = self.__logout_pht, text="Log-out", corner_radius = 25 ,width= self.__get_navigation_footer_width(), height= 55, font=("Poppins",20),fg_color="#696969",border_width = 3,border_color = "#000000")
        self.__logout_button.place(relx = 0.673, rely = 0.86, anchor = "s")
        
    def __get_logout_logo(self):
        return Image.open(self.GET_RELEVANT_PATHDIR('assets/logout.png')).convert("RGBA")   

    def __View_Profile(self):
        self.__viewprofile_pht = ctk.CTkImage(light_image = self.__get_viewprofile_logo(), dark_image = self.__get_viewprofile_logo(), size=(30,30))
        
        self.__view_button = ctk.CTkButton(self.__get_navigation_footer_frame(), image = self.__viewprofile_pht, text="View Profile", corner_radius = 25 ,width= self.__get_navigation_footer_width(), height= 55, font=("Poppins",18),fg_color="#696969",border_width = 3,border_color = "#000000")
        self.__view_button.place(relx = 0.320, rely = 0.85, anchor = "s")
        
    def __get_viewprofile_logo(self):
        return Image.open(self.GET_RELEVANT_PATHDIR('assets/view.png')).convert("RGBA")
        

    def __add(self):
        self.__add_pht = ctk.CTkImage(light_image = self.__get_list_logo(), dark_image = self.__get_add_logo(), size=(30,30))
        
        self.__add_button = ctk.CTkButton(self.__get_navigation_footer_frame(), image = self.__add_pht,text="Add", corner_radius = 25 ,width = 370 , height= 55, font=("Poppins",20),fg_color="#696969",border_width = 3,border_color = "#000000", command=lambda: self.ADD_Objectives())
        self.__add_button.place(relx = 0.158, rely = 0.26, anchor = "w")

    def __get_add_logo(self):
        return Image.open(self.GET_RELEVANT_PATHDIR('assets/add.png')).convert("RGBA")
    

    def __update(self):
        self.__update_pht = ctk.CTkImage(light_image = self.__get_list_logo(), dark_image = self.__get_update_logo(), size=(30,30))
        
        self.__update_button = ctk.CTkButton(self.__get_navigation_footer_frame(), image = self.__update_pht, text="Update", corner_radius = 25 ,width= self.__get_navigation_footer_width(), height= 55, font=("Poppins",20),fg_color="#696969",border_width = 3,border_color = "#000000")
        self.__update_button.place(relx = 0.320, rely = 0.6, anchor = "s")

    def __get_update_logo(self):
        return Image.open(self.GET_RELEVANT_PATHDIR('assets/changes.png')).convert("RGBA")
    
    def __delete(self):
        self.__delete_pht = ctk.CTkImage(light_image = self.__get_list_logo(), dark_image = self.__get_delete_logo(), size=(30,30))
        
        self.__delete_button = ctk.CTkButton(self.__get_navigation_footer_frame(), image = self.__delete_pht,text="Delete", corner_radius = 25 ,width= self.__get_navigation_footer_width(), height= 55, font=("Poppins",20),fg_color="#696969",border_width = 3,border_color = "#000000")
        self.__delete_button.place(relx = 0.507, rely = 0.491, anchor = "w")

    def __get_delete_logo(self):
        return Image.open(self.GET_RELEVANT_PATHDIR('assets/bin.png')).convert("RGBA")

    def __income_frame(self):
        self.__income = ctk.CTkFrame(self.__get_main_frame(), width=self.__income_width(), height= self.__income_height(), fg_color="#696969")
        self.__income.place(relx = 0.19, rely = 0.35,anchor="center")
        
      #LABELS for the input and correspond to that is their individual entery boxes, starts here and  line 177 
        self.__label_add_savings = ctk.CTkLabel(self.__income, text = "Add Savings:", font = ("Poppins", 25, "bold"), width = 100, height = 30, text_color = "white")
        self.__label_add_savings.place( relx = 0.001, rely = 0.15, anchor = "w")
    
        self.__entry_add_savings = ctk.CTkEntry(self.__income, width = 190, height = 50, font = ("Poppins", 25), fg_color = "grey", textvariable=self.__ADD_SAVINGS, validate='key', validatecommand=(self.__root.register(self.VMCD_Entry_OnlyFloat), '%P'))
        self.__entry_add_savings.place( relx= 0.88, rely = 0.15, anchor = "e")
    
        self.__label_savings = ctk.CTkLabel(self.__income, text = "Savings:", font = ("Poppins", 25, "bold"), width = 100, height = 30, text_color = "white")
        self.__label_savings.place( relx = 0.11, rely = 0.35, anchor = "w")
    
        self.__entry_savings = ctk.CTkEntry(self.__income, width = 190, height = 50, font = ("Poppins", 25 ), fg_color = "grey", textvariable=self.__SAVINGS, validate='key', validatecommand=(self.__root.register(self.VMCD_Entry_OnlyFloat), '%P'))
        self.__entry_savings.place( relx = 0.88, rely = 0.35, anchor = "e")
    
        self.__label_stipend = ctk.CTkLabel(self.__income, text= "Stipend:", font = ("Poppins", 25, "bold"), width = 100, height = 30, text_color= "white")
        self.__label_stipend.place( relx = 0.12, rely = 0.55, anchor = "w")
        
        self.__entry_stipend = ctk.CTkEntry(self.__income, width = 190, height = 50, font = ("Poppins", 25), fg_color = "grey", textvariable=self.__STIPEND, validate='key', validatecommand=(self.__root.register(self.VMCD_Entry_OnlyFloat), '%P'))
        self.__entry_stipend.place( relx = 0.88, rely = 0.55, anchor = "e")
    
        self.__label_month_of = ctk.CTkLabel(self.__income, text = "Month of:", font = ("Poppins", 25, "bold"), width = 100, height = 30, text_color = "white")
        self.__label_month_of.place( relx=0.10, rely=0.75, anchor="w")
    
        self.__entry_month_of = ctk.CTkEntry(self.__income, width  = 190, height = 50, font = ("Poppins", 25), fg_color = "grey", textvariable=self.__MONTH_OF)
        self.__entry_month_of.place( relx = 0.88, rely = 0.75, anchor = "e")
    #ENDs here
    def __category_frame(self):
        self.__category = ctk.CTkFrame(self.__get_main_frame(), width=self.__category_width(), height= self.__category_height(), fg_color="#696969")
        self.__category.place(relx = 0.48, rely = 0.35,anchor="center")
        
        #Labels and Entryboxes for category frame
        self.__label_category = ctk.CTkLabel(self.__category, text = "Category", width = 150, height = 30, font = ("Poppins", 30, "bold"), text_color = "white") 
        self.__label_category.place( relx = 0.003, rely = 0.15, anchor = "w")
        
        self.__label_needs = ctk.CTkLabel(self.__category, text = "Needs:", width = 150, height = 30, font = ("Poppins", 25, "bold"), text_color = "white") 
        self.__label_needs.place( relx = 0.006, rely = 0.35, anchor = "w")
        
        self.__label_wants = ctk.CTkLabel(self.__category, text= "Wants:", font = ("Poppins", 25, "bold"), width = 150, height = 30, text_color= "white")
        self.__label_wants.place( relx = 0.006, rely = 0.55, anchor = "w")
        
        self.__label_budget = ctk.CTkLabel(self.__category, text = "Budget", width=150, height=30, font=("Poppins", 30, "bold"), text_color = "white") 
        self.__label_budget.place( relx = 0.450, rely = 0.15, anchor = "w")
        
        #Entry boxes
        self.__entry_needs = ctk.CTkEntry(self.__category, width  = 180, height = 50, font = ("Poppins", 16), fg_color = "grey", textvariable=self.__BUDGET_NEEDS, validate='key', validatecommand=(self.__root.register(self.VMCD_Entry_OnlyFloat), '%P'))
        self.__entry_needs.place( relx = 0.780, rely = 0.35, anchor = "e")
        
        self.__entry_wants = ctk.CTkEntry(self.__category, width  = 180, height = 50, font = ("Poppins", 16), fg_color = "grey", textvariable=self.__BUDGET_WANTS, validate='key', validatecommand=(self.__root.register(self.VMCD_Entry_OnlyFloat), '%P'))
        self.__entry_wants.place( relx = 0.780, rely = 0.55, anchor = "e")
        
    def __note_frame(self):
        self.__note = ctk.CTkFrame(self.__get_main_frame(), width = 720 , height= self.__note_height(), fg_color="#696969")
        self.__note.place(relx = 0.3, rely = 0.75, anchor = "center")
        
        self.__get_note_pht = ctk.CTkImage(light_image = self.__get_list_logo(), dark_image = self.__get_note_logo(), size=(40,40))
        
        self.__label_note = ctk.CTkLabel(self.__note, image = self.__get_note_pht, text = "Note/Reminder :", font = ("Poppins", 30), width = self.__note_width(), height = 40, text_color = "white", compound = "left")
        self.__label_note.place( relx = 0.610, rely = 0.08, anchor = "e")
    
        self.__entry_note = ctk.CTkTextbox(self.__note, width = 570, height = 200, font = ("Poppins", 25), fg_color = "gray")
        self.__entry_note.place( relx = 0.1, rely = 0.55, anchor = "w")
    
    def UPDATE_TXB_Notes(self, NEWTEXT):
        self.__entry_note.delete('1.0','end')
        self.__entry_note.insert('1.0', f'{NEWTEXT}')
    
    def GET_TXB_Notes(self):
        return self.__entry_note
        
    def __get_note_logo(self):
        return Image.open(self.GET_RELEVANT_PATHDIR('assets/notepad.png')).convert("RGBA")

    def __inputs_frame(self):
        self.__input = ctk.CTkFrame(self.__get_main_frame(), width=self.__inputs_width(), height= self.__inputs_height(), fg_color="#696969")
        self.__input.place(relx = 0.770, rely = 0.35 ,anchor="center")
        
        
        dropdown = ctk.CTkComboBox(self.__input, variable = self.__EXPCATEGORY, values = ["Needs", "Wants"], font = ("Poppins", 30), width = 300, height = 50, state = "readonly")
        dropdown.place( relx = 0.2, rely = 0.2, anchor = "w")
        
        self.__label_expenditures = ctk.CTkLabel(self.__input, text= "Expenditures:", font = ("Poppins", 25), width = 150, height = 30, text_color = "white")
        self.__label_expenditures.place( relx = 0.05, rely = 0.5, anchor = "w") 
        
        self.__entry_expenditures = ctk.CTkEntry(self.__input, width = 250, height = 50, font = ("Poppins", 20), fg_color = "gray", textvariable=self.__EXPENDITURES)
        self.__entry_expenditures.place( relx = 0.38, rely = 0.5, anchor = "w")
        
        self.__label_inputAmount = ctk.CTkLabel(self.__input, text= "Amount:", font = ("Poppins", 25), width = 150, height = 30, text_color= "white")
        self.__label_inputAmount.place( relx = 0.115, rely = 0.7, anchor = "w") 
        
        self.__entry_inputAmmount = ctk.CTkEntry(self.__input, width = 250, height = 50, font = ("Poppins", 20), fg_color = "gray", validate='key', validatecommand=(self.__root.register(self.VMCD_Entry_OnlyFloat), '%P'), textvariable=self.__EXPAMOUNT)
        self.__entry_inputAmmount.place( relx = 0.38, rely = 0.7, anchor = "w")
        
    def GET_RELEVANT_PATHDIR(self, IMAGENAME):
      path = os.path.dirname(os.path.abspath(__file__))
      return os.path.join(path, IMAGENAME)