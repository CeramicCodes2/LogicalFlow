from abc import ABC,abstractmethod
class BaseHandler(ABC):
    @abstractmethod
    def createDocument(self,doc,metha):
        pass
    @abstractmethod
    def handler(self):
        pass
    @abstractmethod
    def extractChunkFromDB(self,message):
        pass
    @abstractmethod
    def commit(self):
        ''' for save the transaction '''