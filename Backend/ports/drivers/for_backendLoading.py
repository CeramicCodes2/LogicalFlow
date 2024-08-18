from abc import ABC,abstractmethod
from app.schemas.ModelEntity import GeneratorModel,ModelEntity
class ForBackendLoading(ABC):
    @abstractmethod
    def loadBackend(self,generator:ModelEntity)->GeneratorModel:
        ...
