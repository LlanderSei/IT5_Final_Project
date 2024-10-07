from abc import ABC, abstractmethod
class Blueprint(ABC):
  @abstractmethod
  def Main_Window(self): pass
  
  @abstractmethod
  def _center_frame(self): pass
  
  @abstractmethod
  def _set_left_frame(self): pass

  @abstractmethod
  def _set_right_frame(self): pass