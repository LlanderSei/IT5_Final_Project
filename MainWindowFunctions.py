from tkinter import messagebox as MSGBOX
import customtkinter as CTK
from DatabaseFunctions import DatabaseInteraction

class MainWindowFunctions:
  def __init__(self, SELF):
    self.MW = SELF

    self.__LI_Password_Shown = False
    self.__REG_Password_Shown = False

    self.SET_Window_LoginDatabase()

  def SET_Window_LoginDatabase(self):
    self.MW.SUBWW_LoginDatabase().title('Login to database')
    self.MW.SUBWW_LoginDatabase().geometry(self.MW.CenterAndSize(700, 300))

  def SWITCH_RegisterFrame(self):
    self.MW.GET_RootWindowObject().title('Financial Tracker / Register')
    self.MW.GET_LeftFrameObject('LOGINFRAME').grid_remove()
    self.MW.GET_LeftFrameObject('REGISTERFRAME').grid(row=0, column=0)
    self.SETDEFAULT_RegisterFields()

  def SWITCH_LoginFrame(self):
    self.MW.GET_RootWindowObject().title('Financial Tracker / Login')
    self.MW.GET_LeftFrameObject('REGISTERFRAME').grid_remove()
    self.MW.GET_LeftFrameObject('LOGINFRAME').grid(row=0, column=0) 
    self.SETDEFAULT_LoginFields()

  def VCMD_Validate_Age(self, VALUE):
    if VALUE.isdigit() or VALUE == '': return True
    return False
  
  def VCMD_Validate_Username(self, VALUE):
    if VALUE.isalnum() or '_' in VALUE or VALUE == '': return True
    return False
  
  def FUNC_BTN_LI_Password(self):
    if self.__LI_Password_Shown:
      self.MW.GET_ENTRY_Password_Objects('LOGIN').configure(show='')
      self.MW.GET_BUTTON_Password_Objects('LOGIN').configure(image=self.MW.CTKIMAGE('hide_eye', (40, 20)))
    else:
      self.MW.GET_ENTRY_Password_Objects('LOGIN').configure(show='*')
      self.MW.GET_BUTTON_Password_Objects('LOGIN').configure(image=self.MW.CTKIMAGE('show_eye', (40, 20)))
    
    self.__LI_Password_Shown = not self.__LI_Password_Shown

  def FUNC_BTN_REG_Password(self):
    if self.__REG_Password_Shown:
      self.MW.GET_ENTRY_Password_Objects('REGISTER').configure(show='')
      self.MW.GET_BUTTON_Password_Objects('REGISTER').configure(image=self.MW.CTKIMAGE('hide_eye', (40, 20)))
    else:
      self.MW.GET_ENTRY_Password_Objects('REGISTER').configure(show='*')
      self.MW.GET_BUTTON_Password_Objects('REGISTER').configure(image=self.MW.CTKIMAGE('show_eye', (40, 20)))
    
    self.__REG_Password_Shown = not self.__REG_Password_Shown

  def SETDEFAULT_LoginFields(self):
    self.MW.GET_ENTRY_Password_Objects('LOGIN').configure(show='*')
    self.MW.GET_BUTTON_Password_Objects('LOGIN').configure(image=self.MW.CTKIMAGE('show_eye', (40, 20)))
    self.__LI_Password_Shown = False

    self.MW.GET_STRINGVARS('LOGIN','USERNAME').set('')
    self.MW.GET_STRINGVARS('LOGIN','PASSWORD').set('')

  def SETDEFAULT_RegisterFields(self):
    self.MW.GET_ENTRY_Password_Objects('REGISTER').configure(show='*')
    self.MW.GET_BUTTON_Password_Objects('REGISTER').configure(image=self.MW.CTKIMAGE('show_eye', (40, 20)))
    self.__REG_Password_Shown = False

    self.MW.GET_STRINGVARS('REGISTER','FIRSTNAME').set('')
    self.MW.GET_STRINGVARS('REGISTER','LASTNAME').set('')
    self.MW.GET_STRINGVARS('REGISTER','AGE').set('')
    self.MW.GET_STRINGVARS('REGISTER','ADDRESS').set('')
    self.MW.GET_STRINGVARS('REGISTER','USERNAME').set('')
    self.MW.GET_STRINGVARS('REGISTER','PASSWORD').set('')

  def BUTTON_Login(self):
    USERNAME = self.MW.GET_STRINGVARS('LOGIN','USERNAME').get()
    PASSWORD = self.MW.GET_STRINGVARS('LOGIN','PASSWORD').get()

    if not USERNAME: MSGBOX.showerror('Error', 'Username field is empty!'); return 0
    if not PASSWORD: MSGBOX.showerror('Error', 'Password field is empty!'); return 0

    MSGBOX.showinfo('INPUTTED', f'Inputted: {USERNAME}, {PASSWORD}')

  def BUTTON_Register(self):
    FIRSTNAME = self.MW.GET_STRINGVARS('REGISTER','FIRSTNAME').get()
    LASTNAME = self.MW.GET_STRINGVARS('REGISTER','LASTNAME').get() or None
    AGE = self.MW.GET_STRINGVARS('REGISTER','AGE').get() or None
    ADDRESS = self.MW.GET_STRINGVARS('REGISTER','ADDRESS').get() or None
    USERNAME = self.MW.GET_STRINGVARS('REGISTER','USERNAME').get()
    PASSWORD = self.MW.GET_STRINGVARS('REGISTER','PASSWORD').get()

    if not FIRSTNAME: MSGBOX.showerror('Error', 'First Name field is empty!'); return 0
    if not USERNAME: MSGBOX.showerror('Error', 'Username field is empty!'); return 0
    if not PASSWORD: MSGBOX.showerror('Error', 'Password field is empty!'); return 0

    MSGBOX.showinfo('REGISTER', f'{FIRSTNAME}\n{LASTNAME}\n{AGE}\n{ADDRESS}\n{USERNAME}\n{PASSWORD}')
  
  def SHOW_LoginDatabase(self):
    self.MW.SUBWW_LoginDatabase().deiconify()