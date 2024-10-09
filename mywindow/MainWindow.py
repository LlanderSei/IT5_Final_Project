import customtkinter as CTK
import os
from PIL import Image, ImageTk
from MainWindowFunctions import MainWindowFunctions

class MainWindow:
  __Window_W = __Window_H = int
  __Current_Frame = 'LOGIN'

  "Instantiate objects for the window to run."
  def __init__(self):
    self.__Current_Frame, self.__Window_W, self.__Window_H

    self.MainWindow = CTK.CTk()
    self.__LoginFrame = CTK.CTkFrame(self.MainWindow)
    self.__RegisterFrame = CTK.CTkFrame(self.MainWindow)
    self.__ConnectDBWindow = CTK.CTkToplevel()
    self.__ConnectDBWindow.withdraw()

    self.MWF = MainWindowFunctions(self)
    self.__SETUP_MainWindow()
    self.__SETUP_ConnectToDBWindow()

  def GET_MainWindowObject(self):
    "Returns the MainWindow object. Useful to reach this out from other classes."
    return self.MainWindow
  
  def GET_LoginFrameObject(self):
    "Returns the LoginFrame object. Useful to reach this out from other classes."
    return self.__LoginFrame

  def GET_RegisterFrameObject(self):
    "Returns the RegisterFrame object. Useful to reach this out from other classes."
    return self.__RegisterFrame

  def GET_ConnecToDBWindowObject(self):
    return self.__ConnectDBWindow

  def GET_ScreenWindowSize(self, PARAMETER):
    "Gets the screen size."
    match PARAMETER:
      case 'W': return self.MainWindow.winfo_screenwidth()
      case 'H': return self.MainWindow.winfo_screenheight()

  def __SETUP_MainWindow(self):
    "Instantiating objects for MainWindow to function."
    self.MainWindow.title('Financial Tracker / Login')
    self.MainWindow.config(background = self.__COLORS('GRAY2'))
    self.MainWindow.geometry(self.CenterAndSize(self.__MW_MinWindowSize('W'), self.__MW_MinWindowSize('H')))
    self.MainWindow.minsize(self.__MW_MinWindowSize('W'), self.__MW_MinWindowSize('H'))
    self.MainWindow.iconbitmap(self.GET_RELEVANT_PATHDIR('assets/logo.ico'))
    # self.MainWindow.bind("<Configure>", self.__EVT_Resizable_Frame)

    self.__SETUP_LoginFrame()
    self.__SETUP_RegisterFrame()
    self.MainWindow.protocol("WM_DELETE_WINDOW", self.__ON_Closing)
  
  def CenterAndSize(self, WIDTH, HEIGHT):
    "Gets the provided WIDTH and HEIGHT then automatically centers them."
    X = (self.GET_ScreenWindowSize('W') // 2) - (WIDTH // 2)
    Y = (self.GET_ScreenWindowSize('H') // 2) - (HEIGHT // 2)
    return f'{WIDTH}x{HEIGHT}+{X}+{Y}'
  
  def __MW_MinWindowSize(self, PARAMETER):
    "The minimum window size of the MainWindow."
    match PARAMETER:
      case 'W': return 850
      case 'H': return 650

  def __EVT_Resizable_Frame(self, *EVENT):
    if hasattr(self, '__Current_Frame'):
      self.__Window_W = self.MainWindow.winfo_width() * .9
      self.__Window_H = self.MainWindow.winfo_height() * .9
      self.__UPDATE_Frame_Size(self.__Current_Frame)

  def __UPDATE_Frame_Size(self, TARGETFRAME = 'LOGIN'):
    match TARGETFRAME:
      case 'LOGIN': self.__LoginFrame.place_configure(width=self.__Window_W, height=self.__Window_H)
      case 'REGISTER': self.__RegisterFrame.place_configure(width=self.__Window_W, height=self.__Window_H)

  def Change_Current_Frame(self, TARGETFRAME):
    self.__Current_Frame = TARGETFRAME
    match TARGETFRAME:
      case 'LOGIN': self.__LoginFrame.place(relx=.5, rely=.5, anchor = 'center')
      case 'REGISTER': self.__RegisterFrame.place(relx=.5, rely=.5, anchor = 'center')
    self.__EVT_Resizable_Frame()

  def __SETUP_LoginFrame(self):
    self.__LoginFrame.configure(width = self.__MW_MinWindowSize('W'), height = self.__MW_MinWindowSize('H'), fg_color = self.__COLORS('GRAY3'), bg_color = self.__COLORS('GRAY2'), border_width = 10, border_color = 'black', corner_radius = 10)
    self.__SETUP_LoginFrame_Widgets()
    self.__LoginFrame.place(relx=.5, rely=.5, anchor = 'center')
    self.__LoginFrame.place_configure(relwidth=.975, relheight=.8)
  
  def __SETUP_LoginFrame_Widgets(self):
    CTK.CTkLabel(self.__LoginFrame, text='', anchor='center', fg_color=self.__COLORS('DIRTYWHITE'), width=397, height=494).place(relx=.5, rely=.5, x=0, y=-247)
    CTK.CTkLabel(self.__LoginFrame, text='', anchor='center', fg_color=self.__COLORS('DIRTYWHITE'), image=self.__CTKIMAGE('logo', (200, 200))).place(relx=.5, rely=.5, x=100, y=-100)

    CTK.CTkLabel(self.__LoginFrame, text='LOGIN', font=('Poppins Bold',30), anchor='center', bg_color=self.__COLORS('GRAY3')).place(relx=.5, rely=.5, x=-250, y=-220)
    
    CTK.CTkLabel(self.__LoginFrame, text='Username:', font=('Poppins',20), anchor='e', bg_color=self.__COLORS('GRAY3')).place(relx=.5, rely=.5, x=-370, y=-180)
    CTK.CTkEntry(self.__LoginFrame, font=('Poppins',20), bg_color=self.__COLORS('GRAY3'), border_color=self.__COLORS('BLACK1'), width=350, border_width=5, corner_radius=35, height=30).place(relx=.5, rely=.5, x=-370, y=-150)

    CTK.CTkLabel(self.__LoginFrame, text='Password:', font=('Poppins',20), anchor='e', bg_color=self.__COLORS('GRAY3')).place(relx=.5, rely=.5, x=-370, y=-80)
    CTK.CTkEntry(self.__LoginFrame, font=('Poppins',20), bg_color=self.__COLORS('GRAY3'), fg_color=self.__COLORS('GRAY5'), border_color=self.__COLORS('BLACK1'), width=350, border_width=5, corner_radius=35, height=30).place(relx=.5, rely=.5, x=-370, y=-50)
    CTK.CTkButton(self.__LoginFrame, text='', bg_color=self.__COLORS('GRAY5'), fg_color=self.__COLORS('GRAY3'), border_color=self.__COLORS('BLACK1'), width=30, border_width=2, corner_radius=20, height=30, image=self.__CTKIMAGE('show_eye', (30, 20))).place(relx=.5, rely=.5, x=-95, y=-40)

    CTK.CTkButton(self.__LoginFrame, text='Login', font=('Poppins',20), bg_color=self.__COLORS('GRAY3'), fg_color=self.__COLORS('GRAY4'), border_color=self.__COLORS('BLACK1'), width=330, border_width=5, corner_radius=35, height=30).place(relx=.5, rely=.5, x=-360, y=90)
    CTK.CTkButton(self.__LoginFrame, text='Sign-up', font=('Poppins',20), bg_color=self.__COLORS('GRAY3'), fg_color=self.__COLORS('GRAY4'), border_color=self.__COLORS('BLACK1'), width=330, border_width=5, corner_radius=35, height=30, command=lambda: self.MWF.SHOW_RegisterFrame()).place(relx=.5, rely=.5, x=-360, y=150)

  def __SETUP_RegisterFrame(self):
    self.__RegisterFrame.configure(width = self.__MW_MinWindowSize('W'), height = self.__MW_MinWindowSize('H'), fg_color = self.__COLORS('GRAY3'), bg_color = self.__COLORS('GRAY2'), border_width = 10, border_color = 'black', corner_radius = 10)
    self.__SETUP_RegisterFrame_Widgets()
    
  def __SETUP_RegisterFrame_Widgets(self):
    CTK.CTkLabel(self.__RegisterFrame, text='', anchor='center', fg_color=self.__COLORS('DIRTYWHITE'), width=397, height=494).place(relx=.5, rely=.5, x=0, y=-247)
    CTK.CTkLabel(self.__RegisterFrame, text='', anchor='center', fg_color=self.__COLORS('DIRTYWHITE'), image=self.__CTKIMAGE('logo', (200, 200))).place(relx=.5, rely=.5, x=100, y=-100)
    CTK.CTkLabel(self.__RegisterFrame, text='REGISTER', font=('Poppins Bold',30), anchor='center', bg_color=self.__COLORS('GRAY3')).place(relx=.5, rely=.5, x=-270, y=-240)
    CTK.CTkLabel(self.__RegisterFrame, text='fields with asterisk (*) are required', font=('Poppins',15), anchor='center', bg_color=self.__COLORS('GRAY3')).place(relx=.5, rely=.5, x=-340, y=-200)

    CTK.CTkLabel(self.__RegisterFrame, text='*First Name:', font=('Poppins Bold',17), anchor='center', bg_color=self.__COLORS('GRAY3')).place(relx=.5, rely=.5, x=-370, y=-150)
    CTK.CTkEntry(self.__RegisterFrame, font=('Poppins Bold',13), bg_color=self.__COLORS('GRAY3'), border_color=self.__COLORS('BLACK1'), width=220, border_width=2, corner_radius=35, height=13).place(relx=.5, rely=.5, x=-240, y=-150)

    CTK.CTkLabel(self.__RegisterFrame, text='Last Name:', font=('Poppins',17), anchor='center', bg_color=self.__COLORS('GRAY3')).place(relx=.5, rely=.5, x=-370, y=-110)
    CTK.CTkEntry(self.__RegisterFrame, font=('Poppins Bold',13), bg_color=self.__COLORS('GRAY3'), border_color=self.__COLORS('BLACK1'), width=220, border_width=2, corner_radius=35, height=13).place(relx=.5, rely=.5, x=-240, y=-110)

    CTK.CTkLabel(self.__RegisterFrame, text='Age:', font=('Poppins',17), anchor='center', bg_color=self.__COLORS('GRAY3')).place(relx=.5, rely=.5, x=-370, y=-70)
    CTK.CTkEntry(self.__RegisterFrame, font=('Poppins Bold',13), bg_color=self.__COLORS('GRAY3'), border_color=self.__COLORS('BLACK1'), width=50, border_width=2, corner_radius=35, height=13).place(relx=.5, rely=.5, x=-240, y=-70)

    CTK.CTkLabel(self.__RegisterFrame, text='Address:', font=('Poppins',17), anchor='center', bg_color=self.__COLORS('GRAY3')).place(relx=.5, rely=.5, x=-370, y=-30)
    CTK.CTkEntry(self.__RegisterFrame, font=('Poppins Bold',13), bg_color=self.__COLORS('GRAY3'), border_color=self.__COLORS('BLACK1'), width=220, border_width=2, corner_radius=35, height=13).place(relx=.5, rely=.5, x=-240, y=-30)

    CTK.CTkLabel(self.__RegisterFrame, text='*Username:', font=('Poppins Bold',17), anchor='center', bg_color=self.__COLORS('GRAY3')).place(relx=.5, rely=.5, x=-370, y=10)
    CTK.CTkEntry(self.__RegisterFrame, font=('Poppins Bold',13), bg_color=self.__COLORS('GRAY3'), border_color=self.__COLORS('BLACK1'), width=220, border_width=2, corner_radius=35, height=13).place(relx=.5, rely=.5, x=-240, y=10)

    CTK.CTkLabel(self.__RegisterFrame, text='*Password:', font=('Poppins Bold',17), anchor='center', bg_color=self.__COLORS('GRAY3')).place(relx=.5, rely=.5, x=-370, y=50)
    CTK.CTkEntry(self.__RegisterFrame, font=('Poppins Bold',13), bg_color=self.__COLORS('GRAY3'), border_color=self.__COLORS('BLACK1'), width=220, border_width=2, corner_radius=35, height=13).place(relx=.5, rely=.5, x=-240, y=50)
    CTK.CTkButton(self.__RegisterFrame, text='', bg_color=self.__COLORS('GRAY5'), fg_color=self.__COLORS('GRAY3'), border_color=self.__COLORS('BLACK1'), width=10, border_width=2, corner_radius=20, height=5, image=self.__CTKIMAGE('show_eye', (15, 10))).place(relx=.5, rely=.5, x=-55, y=55)

    CTK.CTkLabel(self.__RegisterFrame, text='Student', font=('Poppins',17), anchor='center', bg_color=self.__COLORS('GRAY3')).place(relx=.5, rely=.5, x=-370, y=90)
    CTK.CTkCheckBox(self.__RegisterFrame, text='No', font=('Poppins Bold',13), bg_color=self.__COLORS('GRAY3'), border_color=self.__COLORS('BLACK1'), width=220, border_width=2, corner_radius=35, height=13).place(relx=.5, rely=.5, x=-240, y=90)

    CTK.CTkLabel(self.__RegisterFrame, text='Has Kids', font=('Poppins',17), anchor='center', bg_color=self.__COLORS('GRAY3')).place(relx=.5, rely=.5, x=-370, y=130)
    CTK.CTkCheckBox(self.__RegisterFrame, text='No', font=('Poppins Bold',13), bg_color=self.__COLORS('GRAY3'), border_color=self.__COLORS('BLACK1'), width=220, border_width=2, corner_radius=35, height=13).place(relx=.5, rely=.5, x=-240, y=130)

    CTK.CTkButton(self.__RegisterFrame, text='Register', font=('Poppins',15), bg_color=self.__COLORS('GRAY3'), fg_color=self.__COLORS('GRAY4'), border_color=self.__COLORS('BLACK1'), width=130, border_width=5, corner_radius=35, height=20).place(relx=.5, rely=.5, x=-190, y=180)
    CTK.CTkButton(self.__RegisterFrame, text='Back', font=('Poppins',15), bg_color=self.__COLORS('GRAY3'), fg_color=self.__COLORS('GRAY4'), border_color=self.__COLORS('BLACK1'), width=130, border_width=5, corner_radius=35, height=20, command=lambda: self.MWF.SHOW_LoginFrame()).place(relx=.5, rely=.5, x=-340, y=180)

  def __ON_Closing(self):
    self.MainWindow.destroy()

  def __SETUP_ConnectToDBWindow(self):
    self.__ConnectDBWindow.title('Connect to a database.')
    self.__ConnectDBWindow.geometry(self.CenterAndSize(500,250))

  def __COLORS(self, COLORNAME):
    ":COLORNAME: available colors provided"
    match COLORNAME:
      case 'BLACK1': return '#242524'
      case 'DIRTYWHITE': return '#DEDAC8'
      case 'GRAY1': return '#838383'
      case 'GRAY2': return '#BFBFBF'
      case 'GRAY3': return '#797979'
      case 'GRAY4': return '#474747'
      case 'GRAY5': return '#313131'

  def __IMAGE(self, IMAGENAME):
    "Returns the image provided by the pathname."
    match IMAGENAME:
      case 'show_eye': return Image.open(self.GET_RELEVANT_PATHDIR('assets/show_eye.png')).convert('RGBA')
      case 'logo': return Image.open(self.GET_RELEVANT_PATHDIR('assets/logo.png')).convert('RGBA')
      case 'logoico': return Image.open(self.GET_RELEVANT_PATHDIR('assets/logo.ico'))

  def __CTKIMAGE(self, IMAGENAME, SIZE = tuple):
    return CTK.CTkImage(light_image=self.__IMAGE(IMAGENAME), dark_image=self.__IMAGE(IMAGENAME), size=SIZE)

  def __IMAGETK(self, IMAGENAME):
    return ImageTk.PhotoImage(self.__IMAGE(IMAGENAME))

  def GET_RELEVANT_PATHDIR(self, PATHNAME):
    DIR_SCRIPT = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(DIR_SCRIPT, PATHNAME)

  def RUN_MainWindow(self):
    self.MainWindow.mainloop()