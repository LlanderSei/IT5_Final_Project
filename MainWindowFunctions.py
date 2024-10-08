class MainWindowFunctions:
  def __init__(self, MainWindowInstance):
    self.MainWindow = MainWindowInstance

  def SHOW_RegisterFrame(self):
    self.MainWindow.GET_MainWindowObject().title('Financial Tracker / Register')
    self.MainWindow.Change_Current_Frame('REGISTER')
    self.MainWindow.GET_RegisterFrameObject().place(relx=.5, rely=.5, anchor = 'center')
    self.MainWindow.GET_RegisterFrameObject().place_configure(relwidth=.975, relheight=.8)
    self.MainWindow.GET_LoginFrameObject().place_forget()
  
  def SHOW_LoginFrame(self):
    self.MainWindow.GET_MainWindowObject().title('Financial Tracker / Login')
    self.MainWindow.Change_Current_Frame('LOGIN')
    self.MainWindow.GET_LoginFrameObject().place(relx=.5, rely=.5, anchor = 'center')
    self.MainWindow.GET_LoginFrameObject().place_configure(relwidth=.975, relheight=.8)
    self.MainWindow.GET_RegisterFrameObject().place_forget()