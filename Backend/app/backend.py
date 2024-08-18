from Backend.app.schemas.ModelEntity import ConversationMessages
from ..ports.drivers.for_inputPrompit import ForInputPrompt
from ..ports.drivers.for_backendLoading import ForBackendLoading
from ..ports.drivens.for_queryPrompt import ForQueryPrompt
from ..ports.drivens.for_messageLogging import ForMessageLogging
from ..ports.drivens.for_messageFormatting import ForMessageRepository

from .schemas import UserRequest,Message
from .schemas.ModelEntity import GeneratorModel,ModelEntity

class Backend(ForBackendLoading,ForInputPrompt):
    
    def __init__(self,userQuery:ForQueryPrompt,messagesRepository:ForMessageRepository,log:ForMessageLogging) -> None:
        self.userQuery = userQuery
        self.generator = None
        self.messagesRepository = messagesRepository
        self.log = log        
        super().__init__()
    def loadBackend(self,specsEntity:ModelEntity)->GeneratorModel:
        self.specsEntity = specsEntity
        self.queryExpansionMessage = Message(content=self.specsEntity.systemQueryExpansion,rol='system')
        self.generator = GeneratorModel.generator
    def processInput(self, input: UserRequest):
        if not(self.generator):
            raise NameError('no se ha cargado ningun modelo en memoria ...')
        # 1) generates the question using the query expansion tecnique
        
        consumedMessage = self.queryExpansionMessage.content.format(user_input=input)
        
        alucinationResponse = self.generator(self.messagesRepository.formatMessagesList(consumedMessage)).split('\n')
        
        # concatenate the user query
        
        self.logFromList(message=alucinationResponse,status='info')
        
        
        # 2) we use the RAG for recave information abaout a certain theme
        
        recvData = self.userQuery.getData(request=alucinationResponse)
        self.logFromList(recvData.queryRequest)
        
        
        return recvData.queryRequest
    