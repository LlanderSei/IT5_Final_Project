class MainWindowFunctions:
  def __init__(self, SELF):
    self.MW = SELF

  def SWITCH_RegisterFrame(self):
    self.MW.GET_RootWindowObject().title('Financial Tracker / Register')
    self.MW.GET_LeftFrameObject('LOGINFRAME').grid_remove()
    self.MW.GET_LeftFrameObject('REGISTERFRAME').grid(row=0, column=0)

  def SWITCH_LoginFrame(self):
    self.MW.GET_RootWindowObject().title('Financial Tracker / Login')
    self.MW.GET_LeftFrameObject('REGISTERFRAME').grid_remove()
    self.MW.GET_LeftFrameObject('LOGINFRAME').grid(row=0, column=0)

  def BUTTON_LI_Password(self):
    if self.MW.Is_Password_Masked('GET', 'LOGIN'):
      self.MW.GET_ENTRY_Password_Objects('LOGIN').configure(show='')
      self.MW.GET_BUTTON_Password_Objects('LOGIN').configure(image=self.MW.CTKIMAGE('hide_eye', (40, 20)))
      self.MW.Is_Password_Masked('SET', 'LOGIN', False)
    else:
      self.MW.GET_ENTRY_Password_Objects('LOGIN').configure(show='*')
      self.MW.GET_BUTTON_Password_Objects('LOGIN').configure(image=self.MW.CTKIMAGE('show_eye', (40, 20)))
      self.MW.Is_Password_Masked('SET', 'LOGIN', True)

  def BUTTON_Login(self):...

  def BUTTON_Register(self):...