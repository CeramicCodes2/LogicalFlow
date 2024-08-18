from Backend.app.schemas.ModelEntity import GeneratorModel, ModelEntity
from ...ports.drivers.for_backendLoading import ForBackendLoading
from ...app.backend import Backend
class BackendLoadder(ForBackendLoading):
    def __init__(self,backend:Backend) -> None:
        super().__init__()
        self.backend = backend
    def loadBackend(self, generator: ModelEntity) -> GeneratorModel:
        return self.backend.loadBackend(generator)