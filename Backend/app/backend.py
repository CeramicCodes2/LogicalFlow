from .schemas.ModelEntity import ConversationMessages
from ..ports.drivers.for_inputPrompit import ForInputPrompt
from ..ports.drivers.for_ModelLoading import ForModelLoading
from ..ports.drivens.for_queryPrompt import ForQueryPrompt
from ..ports.drivens.for_messageLogging import ForMessageLogging
from ..ports.drivens.for_messageFormatting import ForMessageRepository
from ..ports.drivens.for_BackendLoading import ForBackendLoading
from .schemas.UserRequest import UserRequest,Message
from .schemas.ModelEntity import GeneratorModel,ModelEntity

class Backend(ForModelLoading,ForInputPrompt):
    
    def __init__(self,userQuery:ForQueryPrompt,messagesRepository:ForMessageRepository,log:ForMessageLogging,backendLoader:ForBackendLoading) -> None:
        self.userQuery = userQuery
        self.generator = None
        self.messagesRepository = messagesRepository
        self.log = log   
        self.loadder = backendLoader     
        super().__init__()
    def loadModel(self,specsEntity:ModelEntity)->GeneratorModel:
        self.specsEntity = specsEntity
        self.queryExpansionMessage = Message(content=self.specsEntity.systemQueryExpansion,rol='system')
        self.generator = self.loadder.loadBackend(specsEntity)
        
        return self.generator
    def processInput(self, input: UserRequest):
        if not(self.generator):
            raise NameError('no se ha cargado ningun modelo en memoria ...')
        # 1) generates the question using the query expansion tecnique
        
        consumedMessage = self.queryExpansionMessage.content.format(user_input=input)
        
        alucinationResponse = self.generator(self.messagesRepository.formatMessagesList(consumedMessage))
        
        # concatenate the user query
        
        self.log.logFromList(messages=alucinationResponse,status='info')
        
        
        # 2) we use the RAG for recave information abaout a certain theme
        
        recvData = self.userQuery.getData(request=alucinationResponse)
        self.log.logFromList(messages=recvData.queryRequest,status='info')
        
        
        return recvData.queryRequest
    