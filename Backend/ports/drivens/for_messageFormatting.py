from abc import ABC,abstractmethod
from ...app.schemas.ModelEntity import ConversationMessages
class ForMessageRepository(ABC):
    @abstractmethod
    @property
    def messagesHistory(self,message:dict[str,str]):
        return dict()
    @messagesHistory.setter
    def messagesHistory(self,arg:dict[str,str]):
        ...
    @messagesHistory.deleter
    def messagesHistory(self):
        ...
    @abstractmethod
    def formatMessagesList(self,messages:ConversationMessages):
        ...        
    