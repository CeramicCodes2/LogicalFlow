from abc import ABC,abstractmethod
from Repository.app.schemas.PromptRequest import PromptRequest
class ForQueryPrompt(ABC):
    @abstractmethod
    def getData(self,request:str) -> PromptRequest:
        ...