from Backend.app.schemas.ModelEntity import GeneratorModel
from ...ports.drivens.for_BackendLoading import ForBackendLoading
class BackendLoading_llamaCpp(ForBackendLoading):
    def loadBackend(self) -> GeneratorModel:
        
        return super().loadBackend()