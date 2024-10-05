import os
class Login:
  def __init__(self): pass
    # self.__USERNAME__ = self.__PASSWORD__ = str
  
  def enterUsername(self, USERNAME):
    USERNAMEFOUND = False
    for ITEMS in ...:
      if ... == USERNAME.strip().lower():
        ...
        USERNAMEFOUND = True
    if not USERNAMEFOUND:
      return f'Username "{USERNAME}" don\'t exist in this database.'
    
  def __matchPassword__(self, USERNAME): ...

  def __notifyMissing(self):...

class SignUp:
  __FULLNAME = __PASSWORD = __EMAIL = str
  pass

class UserDatabase:
  pass