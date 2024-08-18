from abc import ABC,abstractmethod
from ...app.schemas.ModelEntity import GeneratorModel,ModelEntity
class ForModelLoading(ABC):
    @abstractmethod
    def loadModel(self,generator:ModelEntity)->GeneratorModel:
        ...
