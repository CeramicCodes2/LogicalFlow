from Backend.app.schemas.ModelEntity import GeneratorModel,ModelEntity
from ...ports.drivens.for_BackendLoading import ForBackendLoading
class BackendLoading(ForBackendLoading):
    def loadBackend(self,model:ModelEntity) -> GeneratorModel:
        MOCK_BACKEND = lambda messages: ['hello world','python llm']
        return MOCK_BACKEND