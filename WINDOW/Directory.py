import os

class ScriptDirectory:
  def __init__(self):
    self.__DIR_SCRIPT = os.path.dirname(os.path.abspath(__file__))
    print(f'Dir: {self.__DIR_SCRIPT}')

  def GET_RELEVANT_PATHDIR(self , OBJECT):
    print(f'Object dir: {os.path.join(self.__DIR_SCRIPT, OBJECT)}')
    return os.path.join(self.__DIR_SCRIPT, OBJECT)