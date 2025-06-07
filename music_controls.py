# import the libraries needed
from abc import ABC, abstractmethod

# create the abstract class MusicControls
class MusicControls(ABC):
    
    @abstractmethod
    def __set_status(self):
        pass