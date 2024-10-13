from tkinter import messagebox as MSGBOX
import customtkinter as CTK
import threading
import time
from DatabaseFunctions import DatabaseInteraction
from Home import Home
# from List import List
# from Breakdown import Breakdown

class MainWindowFunctions:
  def __init__(self, MAINWINDOW):
    self.MW = MAINWINDOW
    self.__DBI = DatabaseInteraction()
    self.HOME = Home(self, self.MW)
    # self.LIST = List(self, self.HOME)
    # self.BREAKDOWN = Breakdown(self, self.HOME, self.LIST)

    self.__LI_Password_Shown = False
    self.__REG_Password_Shown = False

    self.__INSTANTIATE_VARIABLES()
    self.SET_Window_LoginDatabase()

    self.HOME.TL_PROTOCOL_Home()

  def __INSTANTIATE_VARIABLES(self):
    self.__DB_Host = CTK.StringVar()
    self.__DB_User = CTK.StringVar()
    self.__DB_Password = CTK.StringVar()
    
    self.__DB_Host.set('localhost')
    self.__DB_User.set('root')
    self.__DB_Password.set('')

  def SET_Window_LoginDatabase(self):
    self.MW.SUBWW_LoginDatabase().title('Login to database')
    self.MW.SUBWW_LoginDatabase().geometry(self.MW.CenterAndSize(400, 200))
    self.MW.SUBWW_LoginDatabase().resizable(False, False)
    self.MW.SUBWW_LoginDatabase().configure(fg_color=self.MW.COLOR('DIMGRAY'))
    self.MW.SUBWW_LoginDatabase().protocol('WM_DELETE_WINDOW', self.SW_PROTOCOL_LoginDatabase)
    self.MW.SUBWW_LoginDatabase().iconbitmap(self.MW.GET_RELEVANT_PATHDIR('assets/logo.ico'))
    
    self.__SET_LoginDatabase_Widgets()

  def SW_PROTOCOL_LoginDatabase(self):
    self.MW.SUBWW_LoginDatabase().withdraw()
    self.MW.GET_RootWindowObject().grab_set()
    
  def SHOW_LoginDatabase(self):
    self.MW.SUBWW_LoginDatabase().deiconify()
    self.MW.SUBWW_LoginDatabase().grab_set()
  
  def __SET_LoginDatabase_Widgets(self):
    CTK.CTkLabel(self.MW.SUBWW_LoginDatabase(), text='HOST', font=('Poppins', 20), text_color='white', width=30, anchor='w').place(x=30, y=20)
    CTK.CTkLabel(self.MW.SUBWW_LoginDatabase(), text='USER', font=('Poppins', 20), text_color='white', width=30, anchor='w').place(x=30, y=60)
    CTK.CTkLabel(self.MW.SUBWW_LoginDatabase(), text='PASSWORD', font=('Poppins', 20), text_color='white', width=30, anchor='w').place(x=30, y=100)
    
    CTK.CTkEntry(self.MW.SUBWW_LoginDatabase(), textvariable=self.__DB_Host, font=('Poppins', 20), text_color='white', width=200, fg_color='black').place(x=160, y=20)
    CTK.CTkEntry(self.MW.SUBWW_LoginDatabase(), textvariable=self.__DB_User, font=('Poppins', 20), text_color='white', width=200, fg_color='black').place(x=160, y=60)
    CTK.CTkEntry(self.MW.SUBWW_LoginDatabase(), textvariable=self.__DB_Password, font=('Poppins', 20), text_color='white', width=200, fg_color='black').place(x=160, y=100)
    
    self.BTN_ConnectDB = CTK.CTkButton(self.MW.SUBWW_LoginDatabase(), text='Connect', height=50, font=('Poppins', 20), text_color='white', border_width=4, border_color='black', fg_color=self.MW.COLOR('VERYDARKGRAY'), command=lambda: self.CMD_BTN_LoginDatabase())
    self.BTN_ConnectDB.place(relx=.35, y=140)
    
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

    if self.__DBI.HasConnection():
      LOGIN = self.__DBI.LoginUser(USERNAME, PASSWORD)
      if LOGIN == 'LOGINSUCCESS':
        MSGBOX.showinfo('Login Success.', 'Login successful!')
        self.PROCEED_To_Home()
      if LOGIN == 'LOGINERROR':
        MSGBOX.showerror('Login Failed', 'Wrong username or password.')
    else:
      self.SHOW_DatabaseNotConnected()
    # MSGBOX.showinfo('INPUTTED', f'Inputted: {USERNAME}, {PASSWORD}')

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

    if self.__DBI.HasConnection():
      REGRESULT = self.__DBI.RegisterUser(FIRSTNAME, LASTNAME, AGE, ADDRESS, USERNAME, PASSWORD)
      if REGRESULT == 'REGSUCCESS': MSGBOX.showinfo('Register success.', 'User successfully registed!')
      elif REGRESULT == 'USERALREADYEXIST': MSGBOX.showerror('Register error.', f"Username '{USERNAME}' already exists.")
      else: MSGBOX.showerror('Error', "Something's wrong...")
    else:
      self.SHOW_DatabaseNotConnected()
    # MSGBOX.showinfo('REGISTER', f'{FIRSTNAME}\n{LASTNAME}\n{AGE}\n{ADDRESS}\n{USERNAME}\n{PASSWORD}')
    self.SETDEFAULT_RegisterFields()
  
  def CMD_BTN_LoginDatabase(self):
    self.BTN_ConnectDB.configure(state='disabled')
    threading.Thread(target=self.ASYNC_DB_Connecting).start()
  
  def ASYNC_DB_Connecting(self):
    LOGINDBRES = self.__DBI.LoginDatabase(self.__DB_Host.get(), self.__DB_User.get(), self.__DB_Password.get())
    time.sleep(3)
    self.MW.GET_RootWindowObject().after(0, self.__HANDLE_DB_Results(LOGINDBRES))
    print(f"Thread {threading.current_thread().name} finished")
    return None
  
  def __HANDLE_DB_Results(self, LOGINDBRES):
    if LOGINDBRES == 'SUCCESSFUL':
      MSGBOX.showinfo('Connection to Database', 'Successfully established connection to the database!')
      self.__DBI.BuildDatabase()
    else:
      MSGBOX.showerror('Connection to Database', 'Login to the Database with the provided credentials were failed.')
    self.BTN_ConnectDB.configure(state='normal')

    # for thread in threading.enumerate():
    #   print(thread.name)

  def SHOW_DatabaseNotConnected(self):
    MSGBOX.showerror('Database not Connected.', 'Connection to a database is not established.\nPlease change the credentials by clicking the DB icon.')

  def PROCEED_To_Home(self):
    self.MW.GET_RootWindowObject().withdraw()
    self.GET_ALL_USER_DATA()
    self.PRELOAD_User_Details()
    self.PRELOAD_List_Details()
    self.UPDATE_Breakdown_Details()
    self.HOME.GET_TL_Root().after(50, lambda: self.HOME.get_fullscreen())

  def UPDATE_INTERFACE(self):
    self.GET_ALL_USER_DATA()
    self.PRELOAD_User_Details()
    self.PRELOAD_List_Details()
    self.UPDATE_Breakdown_Details()
  
  def GET_ALL_USER_DATA(self):
    self.__FIRST_NAME, self.__LAST_NAME, self.__AGE, self.__ADDRESS, self.__NOTES, self.__MONTH_OF = self.__DBI.FetchUserAllInfo('USERINFO')
    self.__ADD_SAVINGS, self.__SAVINGS, self.__STIPEND, self.__BUDGET_NEEDS, self.__BUDGETS_WANTS = self.__DBI.FetchUserAllInfo('BANKS')
    self.__ALL_NEEDS_LIST = self.__DBI.FetchUserAllInfo('NEEDED_OBJECTIVES')
    self.__ALL_WANTS_LIST = self.__DBI.FetchUserAllInfo('WANTED_OBJECTIVES')

  def PRELOAD_User_Details(self):
    self.HOME.Update_Infos('PROFILENAME').set(f'{self.__FIRST_NAME} {self.__LAST_NAME}' if self.__LAST_NAME else self.__FIRST_NAME)
    self.HOME.Update_Infos('ADDSAVINGS').set(self.__ADD_SAVINGS if self.__ADD_SAVINGS else 0)
    self.HOME.Update_Infos('SAVINGS').set(self.__SAVINGS if self.__SAVINGS else 0)
    self.HOME.Update_Infos('STIPEND').set(self.__STIPEND if self.__STIPEND else 0)
    self.HOME.Update_Infos('MONTHOF').set(self.__MONTH_OF if self.__MONTH_OF else '')
    self.HOME.Update_Infos('BUDGETNEEDS').set(self.__BUDGET_NEEDS if self.__BUDGET_NEEDS else 0)
    self.HOME.Update_Infos('BUDGETWANTS').set(self.__BUDGETS_WANTS if self.__BUDGETS_WANTS else 0)
    self.HOME.UPDATE_TXB_Notes(self.__NOTES if self.__NOTES else '')

  def PRELOAD_List_Details(self):
    self.HOME.TL_LIST_Return_Variables('PROFILENAME').set(f'{self.__FIRST_NAME} {self.__LAST_NAME}' if self.__LAST_NAME else self.__FIRST_NAME)
    self.HOME.DEL_ALL_TABLES_LIST()
    self.HOME.HOME_LIST_ModifyTables('NEEDS', self.__ALL_NEEDS_LIST)
    self.HOME.HOME_LIST_ModifyTables('WANTS', self.__ALL_WANTS_LIST)

  def UPDATE_Breakdown_Details(self):
    self.HOME.HOME_CALL_BKDW_VARS('PROFILENAME').set(f'{self.__FIRST_NAME} {self.__LAST_NAME}' if self.__LAST_NAME else self.__FIRST_NAME)

    TOTALNEEDS = TOTALWANTS = 0.0

    for _ID, _NAME, AMOUNTS in self.__ALL_NEEDS_LIST:
      TOTALNEEDS += AMOUNTS
    for _ID, _NAME, AMOUNTS in self.__ALL_WANTS_LIST:
      TOTALWANTS += AMOUNTS

    self.HOME.HOME_CALL_BKDW_VARS('TOTALNEEDS').set(TOTALNEEDS)
    self.HOME.HOME_CALL_BKDW_VARS('TOTALWANTS').set(TOTALWANTS)
    self.HOME.HOME_CALL_BKDW_VARS('BUDGETNEEDS').set(self.__BUDGET_NEEDS)
    self.HOME.HOME_CALL_BKDW_VARS('BUDGETWANTS').set(self.__BUDGETS_WANTS)
    self.HOME.HOME_CALL_BKDW_VARS('SAVINGS').set(self.__SAVINGS)

    self.HOME.HOME_CALL_BKDW_CALCULATIONS()

  def UPDATE_UserDetails(self):
    ADDSAVINGS = self.HOME.Update_Infos('ADDSAVINGS').get()
    SAVINGS = self.HOME.Update_Infos('SAVINGS').get()
    # STIPEND = self.HOME.Update_Infos('STIPEND').get()
    # MONTH_OF = self.HOME.Update_Infos('MONTHOF').get()
    BUDGET_NEEDS = self.HOME.Update_Infos('BUDGETNEEDS').get()
    BUDGET_WANTS = self.HOME.Update_Infos('BUDGETWANTS').get()
    NOTES = self.HOME.GET_TXB_Notes().get('1.0', 'end-1c')

    ADDSAVINGS = float(ADDSAVINGS if ADDSAVINGS else 0)
    SAVINGS = float(SAVINGS if SAVINGS else 0)
    BUDGET_NEEDS = float(BUDGET_NEEDS if BUDGET_NEEDS else 0)
    BUDGET_WANTS = float(BUDGET_WANTS if BUDGET_WANTS else 0)

    self.__DBI.ModifyUser('BANK_INFOS', ADDSAVINGS, SAVINGS, 0, BUDGET_NEEDS, BUDGET_WANTS)
    self.__DBI.ModifyUser('NOTES', NOTES)
    # self.__DBI.ModifyUser('MONTH_OF', MONTH_OF)

  def RUNTIME_UPDATE_BREAKDOWN(self):
    self.GET_ALL_USER_DATA()
    self.UPDATE_Breakdown_Details()

  def ADD_List(self, CATEGORY, *OBJECTS):
    match CATEGORY.upper():
      case 'NEEDS':
        RESULT = self.__DBI.ModifyNeededObjectives('ADD', OBJECTS[0], OBJECTS[1])
        if RESULT == 'NAME_NEEDEDOBJ_DUPE': return 0
      case 'WANTS':
        RESULT = self.__DBI.ModifyWantedObjectives('ADD', OBJECTS[0], OBJECTS[1])
        if RESULT == 'NAME_WANTEDOBJ_DUPE': return 0
    self.UPDATE_INTERFACE()
    return 'ADDSUCCESS'
    
  def UPDATE_List(self, CATEGORY, *OBJECTS):
    "*OBJECTS >> 0: ID, 1: NAME, 2: AMOUNT"
    match CATEGORY.upper():
      case 'NEEDS':
        RESULT = self.__DBI.ModifyNeededObjectives('UPDATE', int(OBJECTS[0]), OBJECTS[1], float(OBJECTS[2]))
        if RESULT == 'NAME_NEEDEDOBJ_DUPE': self.SHOW_MSGBOX_NOTIF('NEEDS_NAMEDUPE', OBJECTS[1]); return 0
      case 'WANTS':
        RESULT = self.__DBI.ModifyWantedObjectives('UPDATE', int(OBJECTS[0]), OBJECTS[1], float(OBJECTS[2]))
        if RESULT == 'NAME_NEEDEDOBJ_DUPE': self.SHOW_MSGBOX_NOTIF('NEEDS_NAMEDUPE', OBJECTS[1]); return 0
    self.UPDATE_INTERFACE()
    
    return 'SUCCESS'

  def DELETE_ITEM_List(self, CATEGORY, ID):
    match CATEGORY.upper():
      case 'NEEDS':
        RESULT = self.__DBI.ModifyNeededObjectives('DELETE', int(ID))
      case 'WANTS':
        RESULT = self.__DBI.ModifyWantedObjectives('DELETE', int(ID))
    MSGBOX.showinfo('Success deletion.', 'The item has been deleted.')
    self.UPDATE_INTERFACE()
    return 'SUCCESS'

  def SHOW_MSGBOX_NOTIF(self, ALERTTYPE, OBJECTS):
    match ALERTTYPE:
      case 'NEEDS_NAMEDUPE': MSGBOX.showerror('ERROR', f'The "{OBJECTS}" in Needs already existed.', parent=self.HOME.GET_TL_Root())
      case 'WANTS_NAMEDUPE': MSGBOX.showerror('ERROR', f'The "{OBJECTS}" in Wants already existed.', parent=self.HOME.GET_TL_Root())

  def GET_TOTAL_NEEDS(self):
    return self.__DBI.get_amount_needs()
  
  def GET_TOTAL_WANTS(self):
    return self.__DBI.get_amount_wants()