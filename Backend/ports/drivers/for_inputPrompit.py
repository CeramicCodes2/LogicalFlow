from abc import ABC,abstractmethod
from Backend.app.schemas.UserRequest import UserRequest

class ForInputPrompt(ABC):
    @abstractmethod
    def processInput(self,input:UserRequest) ->list[str]:
        """ interface for process the user input"""
        ...
    