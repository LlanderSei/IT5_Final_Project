from MainWindowFunctions import MainWindowFunctions
import customtkinter as CTK
import os
from PIL import Image

class MainWindow:
  def __init__(self):
    self.MWF = MainWindowFunctions(self)
    self.__MainWindow = CTK.CTk()
    
    self.__INSTANTIATE_OBJECTS()
    self.__SET_MainWindow()
    
  def __INSTANTIATE_OBJECTS(self):
    self.__MainFrame = CTK.CTkFrame(self.__MainWindow)
    self.__Login_LeftFrame = CTK.CTkFrame(self.__MainFrame)
    self.__Register_LeftFrame = CTK.CTkFrame(self.__MainFrame)

    self.__LI_USERNAME = CTK.StringVar()
    self.__LI_PASSWORD = CTK.StringVar()

    self.__FIRST_NAME = CTK.StringVar()
    self.__LAST_NAME = CTK.StringVar()
    self.__AGE = CTK.StringVar()
    self.__ADDRESS = CTK.StringVar()
    self.__REG_USERNAME = CTK.StringVar()
    self.__REG_PASSWORD = CTK.StringVar()

    self.__Entry_Width = 375

    self.__LI_Is_Password_Masked = True
    self.__REG_Is_Password_Masked = True

  def GET_RootWindowObject(self):
    return self.__MainWindow

  def __SET_MainWindow(self):
    self.__MainWindow.title('Expense Tracker / Login')
    self.__MainWindow.configure(fg_color='black')
    self.__MainWindow.minsize(self.__GET_MinSizeMainWindow('W', .8), self.__GET_MinSizeMainWindow('H', .8))
    self.__MainWindow.geometry(self.__CenterAndSize(self.__MainWindow._min_width, self.__MainWindow._min_height))

    "INSTANTIATING CHILD WIDGETS"
    self.__SET_MainFrame()
    self.__SET_LeftFrame_Login()
    self.__SET_LeftFrame_Register()
    self.__SET_RightFrame()
    self.__Login_LeftFrame.grid(row=0, column=0)
    
  def __GET_MinSizeMainWindow(self, PARAMETER, PERCENTAGE):
    match PARAMETER:
      case 'W': return self.__MainWindow.winfo_screenwidth() * PERCENTAGE
      case 'H': return self.__MainWindow.winfo_screenheight() * PERCENTAGE
  
  def __GET_FrameSize(self, PARAMETER, PERCENTAGE):
    match PARAMETER:
      case 'W': return self.__MainWindow.winfo_screenwidth() * PERCENTAGE
      case 'H': return self.__MainWindow.winfo_screenheight() * PERCENTAGE

  def __CenterAndSize(self, WIDTH, HEIGHT):
    PosX = (self.__MainWindow.winfo_screenwidth() // 2) - (WIDTH // 2)
    PosY = (self.__MainWindow.winfo_screenheight() // 2) - (HEIGHT // 2)
    return f'{WIDTH}x{HEIGHT}+{PosX}+{PosY}'

  def __GET_PosFrameSizes(self, PARAMETER, PERCENTAGE):
    match PARAMETER:
      case 'W': return self.__GET_FrameSize(PARAMETER, PERCENTAGE)
      case 'H': return self.__MainFrame.winfo_screenheight() * PERCENTAGE
    
  def __SET_MainFrame(self):
    self.__MainFrame.configure(width=self.__GET_FrameSize('W', .8), height=self.__GET_FrameSize('H', 1), fg_color=self.__Colors('DIMGRAY'), corner_radius = 0)
    self.__MainFrame.place(relx=.5, rely=.5, anchor='center')
  
  def __SET_LeftFrame_Login(self):
    "LEFT FRAME LOGIN"
    self.__Login_LeftFrame = CTK.CTkFrame(self.__MainFrame, width=self.__GET_PosFrameSizes('W', .45), height=self.__GET_PosFrameSizes('H', .8), fg_color=self.__Colors('DIMGRAY'))

    "/ LOGO"
    CTK.CTkLabel(self.__Login_LeftFrame, image=self.CTKIMAGE('logo', (100, 100)), text='', fg_color=self.__Colors('DIMGRAY')).place(relx=.5, x=15, y=10, anchor='n')
    "/ LABEL: LOGIN"
    CTK.CTkLabel(self.__Login_LeftFrame, text="LOGIN", fg_color=self.__Colors('DIMGRAY'), text_color="white", font=('Poppins Bold', 50)).place(relx= 0.525, y=120, anchor="n")

    "/ USERNAME"
    CTK.CTkLabel(self.__Login_LeftFrame, text='Username:', font=('Poppins', 20), text_color='white').place(relx=.5, x=-115, y=190, anchor='n')
    CTK.CTkEntry(self.__Login_LeftFrame, width=350, height=50, font=('Poppins', 20), text_color='white', corner_radius=35, fg_color=self.__Colors('VERYDARKGRAY'), border_color=self.__Colors('VERYDARKGRAY'), border_width=5, textvariable=self.__LI_USERNAME).place(relx= .5, y=220, anchor='n')

    "/ PASSWORD"
    CTK.CTkLabel(self.__Login_LeftFrame, text='Password:', font=('Poppins', 20), text_color='white').place(relx=.5, x=-115, y=300, anchor='n')
    self.__LI_ENTRY_Password = CTK.CTkEntry(self.__Login_LeftFrame, width=350, height=50, font=('Poppins', 20), text_color='white', corner_radius=35, fg_color=self.__Colors('VERYDARKGRAY'), border_color=self.__Colors('VERYDARKGRAY'), border_width=5, textvariable=self.__LI_PASSWORD, show='*')
    self.__LI_ENTRY_Password.place(relx= .5, y=330, anchor='n')
    self.__LI_BUTTON_Password = CTK.CTkButton(self.__Login_LeftFrame, image=self.CTKIMAGE('show_eye', (40, 25)), text='', fg_color=self.__Colors('VERYDARKGRAY'), width=10, border_width=2, border_color=self.__Colors('VERYDARKGRAY'), corner_radius=10, command=lambda: self.MWF.BUTTON_LI_Password())
    self.__LI_BUTTON_Password.place(relx= 0.5, y = 340, anchor= "n", x = 220)

    "/ LOGIN BUTTON"
    CTK.CTkButton(self.__Login_LeftFrame, text='Log-In', width=200, height=50, font=('Poppins', 20), fg_color=self.__Colors('VERYDARKGRAY'), text_color= "#e1e1e1", corner_radius= 50).place(relx= 0.5, y = 420, anchor= "n")

    "/ SIGNUP BUTTON"
    CTK.CTkButton(self.__Login_LeftFrame, text="Sign-Up", width= 350, height= 70, font=("Poppins", 20), fg_color=self.__Colors('VERYDARKGRAY'), text_color="#e1e1e1", corner_radius= 50, command=lambda: self.MWF.SWITCH_RegisterFrame()).place(relx= 0.5, y = 500, anchor= "n")

  def __SET_LeftFrame_Register(self):
    "LEFT FRAME REGISTER"
    self.__Register_LeftFrame.configure(width=self.__GET_PosFrameSizes('W', .45), height=self.__GET_PosFrameSizes('H', .8), fg_color=self.__Colors('DIMGRAY'))
    # self.__Register_LeftFrame.grid(row=0, column=0)

    "/ LABEL: REGISTER"
    CTK.CTkLabel(self.__Register_LeftFrame, text="REGISTER", fg_color=self.__Colors('DIMGRAY'), text_color="white", font=('Poppins Bold', 50)).place(relx= 0.525, y=30, anchor="n")
    CTK.CTkLabel(self.__Register_LeftFrame, text="fields with asterisk (*) are required", fg_color=self.__Colors('DIMGRAY'), text_color="white", font=('Poppins', 20)).place(relx= 0.525, y=90, anchor="n")

    "/ FIRST NAME"
    CTK.CTkLabel(self.__Register_LeftFrame, text="*First Name", fg_color=self.__Colors('DIMGRAY'), text_color="white", font=('Poppins Bold', 20)).place(relx= 0.25, y=145, anchor="n")
    CTK.CTkEntry(self.__Register_LeftFrame, font=('Poppins',20), width=self.__Entry_Width, corner_radius=35, fg_color=self.__Colors('VERYDARKGRAY'), height=50, text_color="white", border_color= self.__Colors('VERYDARKGRAY'), textvariable=self.__FIRST_NAME).place(relx = 0.65, y=135, anchor="n")
    "/ LAST NAME"
    CTK.CTkLabel(self.__Register_LeftFrame, text="Last Name", fg_color=self.__Colors('DIMGRAY'), text_color="white", font=('Poppins', 20)).place(relx=0.25, y=210, anchor="n")
    CTK.CTkEntry(self.__Register_LeftFrame, font=('Poppins', 20), width=self.__Entry_Width, corner_radius=35, fg_color=self.__Colors('VERYDARKGRAY'), height=50, text_color="white", border_color= self.__Colors('VERYDARKGRAY'), textvariable=self.__LAST_NAME).place(relx = 0.65, y=200,anchor="n")
    "/ AGE"
    CTK.CTkLabel(self.__Register_LeftFrame, text="Age", fg_color=self.__Colors('DIMGRAY'), text_color="white", font=('Poppins',20)).place(relx=0.25, y=275, anchor="n")
    CTK.CTkEntry(self.__Register_LeftFrame, font=('Poppins',20), width=self.__Entry_Width, corner_radius=35, fg_color=self.__Colors('VERYDARKGRAY'), height=50, text_color="white", border_color=self.__Colors('VERYDARKGRAY'), textvariable=self.__AGE).place(relx = 0.65, y=265,anchor="n") 
    "/ ADDRESS"
    CTK.CTkLabel(self.__Register_LeftFrame, text="Address", fg_color=self.__Colors('DIMGRAY'), text_color="white", font=('Poppins',20)).place(relx=0.25, y=340, anchor="n")
    CTK.CTkEntry(self.__Register_LeftFrame, font=('Poppins',20), width=self.__Entry_Width, corner_radius=35, fg_color=self.__Colors('VERYDARKGRAY'), height=50, text_color="white", border_color=self.__Colors('VERYDARKGRAY'), textvariable=self.__ADDRESS).place(relx = 0.65, y=330,anchor="n")
    "/ USERNAME"
    CTK.CTkLabel(self.__Register_LeftFrame, text="*Username", fg_color=self.__Colors('DIMGRAY'), text_color="white", font=('Poppins Bold',20)).place(relx=0.25, y=405, anchor="n")
    CTK.CTkEntry(self.__Register_LeftFrame, font=('Poppins',20), width=self.__Entry_Width, corner_radius=35, fg_color=self.__Colors('VERYDARKGRAY'), height=50, text_color="white", border_color=self.__Colors('VERYDARKGRAY'), textvariable=self.__REG_USERNAME).place(relx = 0.65, y=395,anchor="n")

    "/ PASSWORD"
    CTK.CTkLabel(self.__Register_LeftFrame, text="*Password", fg_color=self.__Colors('DIMGRAY'), text_color="white", font=('Poppins Bold',20)).place(relx=0.25, y=470, anchor="n")
    self.__REG_ENTRY_Password = CTK.CTkEntry(self.__Register_LeftFrame, font=('Poppins',20), width=self.__Entry_Width * .8, corner_radius=35, fg_color=self.__Colors('VERYDARKGRAY'), height=50, text_color="white", border_color=self.__Colors('VERYDARKGRAY'), show='*', textvariable=self.__REG_PASSWORD)
    self.__REG_ENTRY_Password.place(relx = 0.6, y=460,anchor="n")
    self.__REG_BUTTON_Password = CTK.CTkButton(self.__Register_LeftFrame, text='', image=self.CTKIMAGE('show_eye', (40, 20)), fg_color=self.__Colors('VERYDARKGRAY'), border_color=self.__Colors('VERYDARKGRAY'), border_width=2, corner_radius=10, width=10, command= lambda: self.MWF.BUTTON_LI_Password_Register())
    self.__REG_BUTTON_Password.place(relx= 0.61, y = 470, anchor= "n", x = 180)

    "/ REGISTER AND RETURN BUTTON"
    CTK.CTkButton(self.__Register_LeftFrame, text="Register", width=500, height= 50, font=("Poppins", 20), fg_color= self.__Colors('VERYDARKGRAY'), text_color="#e1e1e1", corner_radius= 35).place(relx= 0.55, y = 550, anchor= "n")
    CTK.CTkButton(self.__Register_LeftFrame, text="Return to Log-In", width=500, height= 50, font=("Poppins", 20), fg_color= self.__Colors('VERYDARKGRAY'), text_color="#e1e1e1", corner_radius=35, command=lambda: self.MWF.SWITCH_LoginFrame()).place(relx= 0.55, y = 615, anchor= "n")

  def __SET_RightFrame(self):
    self.__Static_RightFrame = CTK.CTkFrame(self.__MainFrame, width=self.__GET_PosFrameSizes('W', .45), height=self.__GET_PosFrameSizes('H', .8), fg_color='WHITE')
    self.__Static_RightFrame.grid(row=0, column=1)
    CTK.CTkLabel(self.__Static_RightFrame, image=self.CTKIMAGE('logo', (200, 200)), text='', fg_color='white').place(relx= 0.5, rely= 0.5, anchor="center")

  def __Colors(self, COLORNAME):
    match COLORNAME:
      case 'DIMGRAY': return '#696969'
      case 'VERYDARKGRAY': return '#2c2c2c'
      case 'VERYLIGHTGRAY': return '#e1e1e1'

  def IMAGE(self, IMAGENAME):
    match IMAGENAME:
      case 'logo': return Image.open(self.GET_RELEVANT_PATHDIR('assets/logo.png')).convert('RGBA')
      case 'hide_eye': return Image.open(self.GET_RELEVANT_PATHDIR('assets/hide_eye.png')).convert('RGBA')
      case 'show_eye': return Image.open(self.GET_RELEVANT_PATHDIR('assets/show_eye.png')).convert('RGBA')

  def CTKIMAGE(self, IMAGENAME, SIZE: tuple = None):
    return CTK.CTkImage(light_image=self.IMAGE(IMAGENAME), dark_image=self.IMAGE(IMAGENAME), size=SIZE)
  
  def GET_RELEVANT_PATHDIR(self, PATHNAME):
    DIR_SCRIPT = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(DIR_SCRIPT, PATHNAME)
  
  def GET_LeftFrameObject(self, FRAMEOBJECT):
    match FRAMEOBJECT:
      case 'LOGINFRAME': return self.__Login_LeftFrame
      case 'REGISTERFRAME': return self.__Register_LeftFrame

  def GET_STRINGVARS(self, IDENTITY, VAR):
    match IDENTITY:
      case 'LOGIN':
        match VAR:
          case 'USERNAME': return self.__LI_USERNAME
          case 'PASSWORD': return self.__LI_PASSWORD
      case 'REGISTER':
        match VAR:
          case 'FIRSTNAME': return self.__FIRST_NAME
          case 'LASTNAME': return self.__LAST_NAME
          case 'AGE': return self.__AGE
          case 'ADDRESS': return self.__ADDRESS
          case 'USERNAME': return self.__REG_USERNAME
          case 'PASSWORD': return self.__REG_PASSWORD
  
  def SET_STRINGVARS_TO_EMPTY(self, IDENTITY):
    match IDENTITY:
      case 'LOGIN':
          self.__LI_USERNAME.set()
          self.__LI_PASSWORD.set()
      case 'REGISTER':
          self.__FIRST_NAME.set()
          self.__LAST_NAME.set()
          self.__AGE.set()
          self.__ADDRESS.set()
          self.__REG_USERNAME.set()
          self.__REG_PASSWORD.set()

  def GET_ENTRY_Password_Objects(self, IDENTITY):
    match IDENTITY:
      case 'LOGIN': return self.__LI_ENTRY_Password
      case 'REGISTER': return self.__REG_ENTRY_Password

    self.__LI_ENTRY_Password.configure(show='')
    self.__LI_BUTTON_Password.configure()

  def GET_BUTTON_Password_Objects(self, IDENTITY):
    match IDENTITY:
      case 'LOGIN': return self.__LI_BUTTON_Password
      case 'REGISTER': return self.__REG_BUTTON_Password

  def Is_Password_Masked(self, MODE, IDENTITY, *SWITCH):
    match MODE:
      case 'SET':
        match IDENTITY:
          case 'LOGIN': self.__LI_Is_Password_Masked = SWITCH
          case 'REGISTER': self.__REG_Is_Password_Masked = SWITCH
      case 'GET':
        match IDENTITY:
          case 'LOGIN': return self.__LI_Is_Password_Masked
          case 'REGISTER': return self.__REG_Is_Password_Masked

  def RUN_MainWindow(self):
    self.__MainWindow.mainloop()
    
mw = MainWindow()
mw.RUN_MainWindow()