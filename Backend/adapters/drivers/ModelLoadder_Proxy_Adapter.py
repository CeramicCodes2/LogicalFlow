from Backend.app.schemas.ModelEntity import GeneratorModel, ModelEntity
from ...ports.drivers.for_backendLoading import ForModelLoading
from ...app.backend import Backend
class ModelLoadder(ForModelLoading):
    def __init__(self,backend:Backend) -> None:
        super().__init__()
        self.backend = backend
    def loadModel(self, generator: ModelEntity) -> GeneratorModel:
        return self.backend.loadModel(generator)