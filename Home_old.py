from customtkinter import *
import customtkinter as CTK
from PIL import Image
import os

class Home:
  def __init__(self):
    #self.__parent = parent
    self.__root = CTK.CTk()
    #self.__root.protocol("WM_DELETE_WINDOW", self.__on_close)
    self.Main_Window()
    self.__root.mainloop()

  def __get_main_window_width(self):
    return self.__get_frame_width(0.8)
  
  def __get_main_window_height(self):
    return self.__get_frame_height(0.8) 
  
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
    return self.__get_mainframe_width(0.25)
  
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
    self.__main_frame = CTK.CTkFrame(self.__get_root(), width=self.__get_main_frame_width(), height= self.__get_main_frame_height(), fg_color="#696969")
    self.__main_frame.place(relx = 0.5, rely = 0.5 ,anchor= "center")

  def __get_main_frame(self):
    return self.__main_frame
  
  def __navigation_header_frame(self):
    self.__navigation_header = CTK.CTkFrame(self.__get_main_frame(), width=self.__navigation_width(), height= self.__navigation_height(), fg_color="#696969")
    self.__navigation_header.place(relx = 0.5, rely = 0.025, anchor="n")
    self.__usernamebutton()
    self.__listbutton()
    self.__breakdownbutton()
    
  def __usernamebutton(self):    
    self.__username_button = CTK.CTkButton(self.__get_navigation_header_frame(), image=self.CTKIMAGE('logo', (50,50)), text = "Name",width = self.__username_button_width(), height = 60, font = ("Poppins",23, "bold"),fg_color ="#2c2c2c")
    self.__username_button.place(relx=0.15, rely=0.5, anchor="center")
    self.__photoplacement = CTK.CTkLabel(self.__get_navigation_header_frame(), image=self.CTKIMAGE('profile2', (80,80)), text="", fg_color="#2c2c2c", corner_radius=10)
    self.__photoplacement.place(relx= 0.05, rely= 0.5, anchor="center")

  def __get_name_logo(self):
    return Image.open("profile2.png").convert("RGBA")

  def __listbutton(self):
    self.__list_button = CTK.CTkButton(self.__get_navigation_header_frame(), image=self.CTKIMAGE('list', (40,40)), text = "List", corner_radius = 25, width= self.__list_button_width(), height= 50, font=("Poppins",23, "bold"), fg_color="#696969",border_width = 3,border_color = "#000000")
    self.__list_button.place(relx=0.59, rely=0.5, anchor="center")

  def __breakdownbutton(self):
    self.__breakdown_button = CTK.CTkButton(self.__get_navigation_header_frame(), image = self.CTKIMAGE('breakdown', (40,40)), text = "Breakdown", corner_radius = 25, width = self.__breakdown_button_width(), height= 50, font=("Poppins",23, "bold"), fg_color="#696969",border_width = 3,border_color = "#000000")
    self.__breakdown_button.place(relx = 0.830, rely = 0.5, anchor = "center")
    
  def __navigation_footer_frame(self):
    self.__navigation_footer = CTK.CTkFrame(self.__get_main_frame(), width= self.__note_width(), height= self.__note_height(), fg_color="#696969")
    self.__navigation_footer.place(relx = 0.75, rely = 0.973, y = -25,anchor="s")
    self.__Logout()
    self.__View_Profile()
    self.__add()
    self.__update()
    self.__delete()
  
  def __get_navigation_footer_width(self):
    return self.__get_navigation_footer_frame_width(0.2)
  
  def __Logout(self):
    self.__logout_button = CTK.CTkButton(self.__get_navigation_footer_frame(), image = self.CTKIMAGE('logout', (30,30)), text="Log-out", corner_radius = 25 ,width= self.__get_navigation_footer_width(), height= 55, font=("Poppins",20),fg_color="#696969",border_width = 3,border_color = "#000000")
    self.__logout_button.place(relx = 0.70, rely = 0.78, anchor = "s")
      
  def __View_Profile(self):
    self.__view_button = CTK.CTkButton(self.__get_navigation_footer_frame(), image =self.CTKIMAGE('view_profile', (30,30)), text="View Profile", corner_radius = 25 ,width= self.__get_navigation_footer_width(), height= 55, font=("Poppins",20),fg_color="#696969",border_width = 3,border_color = "#000000")
    self.__view_button.place(relx = 0.398, rely = 0.78, anchor = "s")
            

  def __add(self):
    self.__add_button = CTK.CTkButton(self.__get_navigation_footer_frame(), image = self.CTKIMAGE('add',(30,30)),text="Add", corner_radius = 25 ,width = 450 , height= 55, font=("Poppins",20),fg_color="#696969",border_width = 3,border_color = "#000000")
    self.__add_button.place(relx = 0.258, rely = 0.26, anchor = "w")
  
  def __update(self):      
      self.__update_button = CTK.CTkButton(self.__get_navigation_footer_frame(), image =self.CTKIMAGE('changes', (30,30)), text="Update", corner_radius = 25 ,width= self.__get_navigation_footer_width(), height= 55, font=("Poppins",20),fg_color="#696969",border_width = 3,border_color = "#000000")
      self.__update_button.place(relx = 0.398, rely = 0.56, anchor = "s")
  
  def __delete(self):    
    self.__delete_button = CTK.CTkButton(self.__get_navigation_footer_frame(), image =self.CTKIMAGE('bin', (30,30)),text="Delete", corner_radius = 25 ,width= self.__get_navigation_footer_width(), height= 55, font=("Poppins",20),fg_color="#696969",border_width = 3,border_color = "#000000")
    self.__delete_button.place(relx = 0.56, rely = 0.472, anchor = "w")

  def __income_frame(self):
    self.__income = CTK.CTkFrame(self.__get_main_frame(), width=self.__income_width(), height= self.__income_height(), fg_color="#696969")
    self.__income.place(relx = 0.19, rely = 0.35,anchor="center")
      
    #LABELS for the input and correspond to that is their individual entery boxes, starts here and  line 177 
    self.__label_add_savings = CTK.CTkLabel(self.__income, text = "Add Savings:", font = ("Poppins", 25, "bold"), width = 100, height = 30, text_color = "white")
    self.__label_add_savings.place( relx = 0.001, rely = 0.15, anchor = "w")

    self.__entry_add_savings = CTK.CTkEntry(self.__income, width = 270, height = 50, font = ("Poppins", 25), fg_color = "grey")
    self.__entry_add_savings.place( relx= 0.90, rely = 0.15, anchor = "e")

    self.__label_savings = CTK.CTkLabel(self.__income, text = "Savings:", font = ("Poppins", 25, "bold"), width = 100, height = 30, text_color = "white")
    self.__label_savings.place( relx = 0.11, rely = 0.35, anchor = "w")

    self.__entry_savings = CTK.CTkEntry(self.__income, width = 270, height = 50, font = ("Poppins", 25 ), fg_color = "grey")
    self.__entry_savings.place( relx = 0.90, rely = 0.35, anchor = "e")

    self.__label_stipend = CTK.CTkLabel(self.__income, text= "Stipend:", font = ("Poppins", 25, "bold"), width = 100, height = 30, text_color= "white")
    self.__label_stipend.place( relx = 0.12, rely = 0.55, anchor = "w")
    
    self.__entry_stipend = CTK.CTkEntry(self.__income, width = 270, height = 50, font = ("Poppins", 25), fg_color = "grey")
    self.__entry_stipend.place( relx = 0.90, rely = 0.55, anchor = "e")

    self.__label_month_of = CTK.CTkLabel(self.__income, text = "Month of:", font = ("Poppins", 25, "bold"), width = 100, height = 30, text_color = "white")
    self.__label_month_of.place( relx=0.10, rely=0.75, anchor="w")

    self.__entry_month_of = CTK.CTkEntry(self.__income, width  = 270, height = 50, font = ("Poppins", 25), fg_color = "grey")
    self.__entry_month_of.place( relx = 0.90, rely = 0.75, anchor = "e")
  #ENDs here
  def __category_frame(self):
    self.__category = CTK.CTkFrame(self.__get_main_frame(), width=self.__category_width(), height= self.__category_height(), fg_color="#696969")
    self.__category.place(relx = 0.48, rely = 0.35,anchor="center")
      
    #Labels and Entryboxes for category frame
    self.__label_category = CTK.CTkLabel(self.__category, text = "Category", width = 150, height = 30, font = ("Poppins", 30, "bold"), text_color = "white") 
    self.__label_category.place( relx = 0.07, rely = 0.15, anchor = "w")
    
    self.__label_needs = CTK.CTkLabel(self.__category, text = "Needs :", width = 150, height = 30, font = ("Poppins", 25, "bold"), text_color = "white") 
    self.__label_needs.place( relx = 0.1, rely = 0.35, anchor = "w")
    
    self.__label_wants = CTK.CTkLabel(self.__category, text= "Wants :", font = ("Poppins", 25, "bold"), width = 150, height = 30, text_color= "white")
    self.__label_wants.place( relx = 0.1, rely = 0.55, anchor = "w")
    
    self.__label_budget = CTK.CTkLabel(self.__category, text = "Budget", width=150, height=30, font=("Poppins", 30, "bold"), text_color = "white") 
    self.__label_budget.place( relx = 0.45, rely = 0.15, anchor = "w")
    
    #Entry boxes
    self.__entry_needs = CTK.CTkEntry(self.__category, width  = 200, height = 50, font = ("Poppins", 16), fg_color = "grey")
    self.__entry_needs.place( relx = 0.8, rely = 0.35, anchor = "e")
    
    self.__entry_wants = CTK.CTkEntry(self.__category, width  = 200, height = 50, font = ("Poppins", 16), fg_color = "grey")
    self.__entry_wants.place( relx = 0.8, rely = 0.55, anchor = "e")
      
  def __note_frame(self):
    self.__note = CTK.CTkFrame(self.__get_main_frame(), width = 1020 , height= self.__note_height(), fg_color="#696969")
    self.__note.place(relx = 0.275, rely = 0.75, anchor = "center")
        
    self.__label_note = CTK.CTkLabel(self.__note, image = self.CTKIMAGE('notepad',(40,40)), text = "Note/Reminder :", font = ("Poppins", 30), width = self.__note_width(), height = 40, text_color = "white", compound = "left")
    self.__label_note.place( relx = 0.65, rely = 0.12, anchor = "e")

    self.__entry_note = CTK.CTkTextbox(self.__note, width = 850, height = 200, font = ("Poppins", 20), fg_color = "gray")
    self.__entry_note.place( relx = 0.150, rely = 0.50, anchor = "w")
      
  def __inputs_frame(self):
    self.__input = CTK.CTkFrame(self.__get_main_frame(), width=self.__inputs_width(), height= self.__inputs_height(), fg_color="#696969")
    self.__input.place(relx = 0.785, rely = 0.35 ,anchor="center")
    
    noteDropdown_var = CTK.StringVar(value = "Needs")
    
    dropdown = CTK.CTkComboBox(self.__input, variable = noteDropdown_var, values = ["Needs", "Wants"], font = ("Poppins", 30), width = 300, height = 50, state = "readonly")
    dropdown.place( relx = 0.2, rely = 0.2, anchor = "w")
    
    self.__label_expenditures = CTK.CTkLabel(self.__input, text= "Expenditures :", font = ("Poppins", 30), width = 150, height = 30, text_color = "white")
    self.__label_expenditures.place( relx = 0.05, rely = 0.5, anchor = "w") 
    
    self.__entry_expenditures = CTK.CTkEntry(self.__input, width = 250, height = 50, font = ("Poppins", 20), fg_color = "gray")
    self.__entry_expenditures.place( relx = 0.38, rely = 0.5, anchor = "w")
    
    self.__label_inputAmount = CTK.CTkLabel(self.__input, text= "Amount :", font = ("Poppins", 30), width = 150, height = 30, text_color= "white")
    self.__label_inputAmount.place( relx = 0.145, rely = 0.7, anchor = "w") 
    
    self.__entry_inputAmmount = CTK.CTkEntry(self.__input, width = 250, height = 50, font = ("Poppins", 20), fg_color = "gray")
    self.__entry_inputAmmount.place( relx = 0.38, rely = 0.7, anchor = "w")
  
  def CTKIMAGE(self, IMAGENAME, SIZE):
    return CTK.CTkImage(light_image=self.IMAGE(IMAGENAME), dark_image=self.IMAGE(IMAGENAME), size=SIZE)
  
  def IMAGE(self, IMAGENAME):
    match IMAGENAME:
      case 'add': return Image.open(self.GET_RELEVANT_PATHDIR('assets/add.png')).convert('RGBA')
      case 'bin': return Image.open(self.GET_RELEVANT_PATHDIR('assets/bin.png')).convert('RGBA')
      case 'breakdown': return Image.open(self.GET_RELEVANT_PATHDIR('assets/breakdown.png')).convert('RGBA')
      case 'changes': return Image.open(self.GET_RELEVANT_PATHDIR('assets/changes.png')).convert('RGBA')
      case 'hide_pass': return Image.open(self.GET_RELEVANT_PATHDIR('assets/hide_eye.png')).convert('RGBA')
      case 'show_pass': return Image.open(self.GET_RELEVANT_PATHDIR('assets/show_eye.png')).convert('RGBA')
      case 'logo': return Image.open(self.GET_RELEVANT_PATHDIR('assets/logo.png')).convert('RGBA')
      case 'list': return Image.open(self.GET_RELEVANT_PATHDIR('assets/list.png')).convert('RGBA')
      case 'logout': return Image.open(self.GET_RELEVANT_PATHDIR('assets/logout.png')).convert('RGBA')
      case 'notepad': return Image.open(self.GET_RELEVANT_PATHDIR('assets/notepad.png')).convert('RGBA')
      case 'profile2': return Image.open(self.GET_RELEVANT_PATHDIR('assets/profile2.png')).convert('RGBA')
      case 'view_profile': return Image.open(self.GET_RELEVANT_PATHDIR('assets/view.png')).convert('RGBA')
  
  def GET_RELEVANT_PATHDIR(self, IMAGENAME):
    path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(path, IMAGENAME)
  
  
home = Home()