from abc import ABC,abstractmethod
class ForMessageLogging(ABC):
    def log(self,message:str,status:str) -> None:
        ...
    def logFromList(self,messages:list,status:str) -> None:
        ...
        