from abc import ABC,abstractmethod
from ...app.schemas.ModelEntity import ConversationMessages
class ForMessageRepository(ABC):
    @property
    @abstractmethod
    def messagesHistory(self,message:dict[str,str]):
        return dict()
    @messagesHistory.setter
    def messagesHistory(self,arg:dict[str,str]):
        ...
    @messagesHistory.deleter
    def messagesHistory(self):
        ...
    @property
    @abstractmethod
    def template(self):
        return self._messagesHistory.jinjaTemplateFormat
    @template.setter
    def template(self,template:str):
        self._messagesHistory.jinjaTemplateFormat = template
    @template.deleter
    def template(self):
        self._messagesHistory.jinjaTemplateFormat = ''
    @abstractmethod
    def formatMessagesList(self,messages:ConversationMessages) ->str:
        ...        
    