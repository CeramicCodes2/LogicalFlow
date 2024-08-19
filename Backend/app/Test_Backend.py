import unittest 
from unittest.mock import Mock,patch,PropertyMock
 
from .backend import UserRequest
from .backend import Backend,ModelEntity
from ..adapters.driven import (
    MessageLogging_Adapter_proxy,
    MessageRepository_Proxy_Adapter,
    QueryPrompt_Adapter_stub,
    BackendLoading_Adapter_proxy_stub
)
#from ..adapters.drivers import (
#    ModelLoadder_Proxy_Adapter,
#    InputPrompt_adapter,
#    
#)

class TestBackend(unittest.TestCase):
    @classmethod
    @patch.object(MessageRepository_Proxy_Adapter.MessageRepository,'messagesHistory',new_callable=PropertyMock)
    def setUp(cls,repositoryMessages_mock):
        # DRIVENS
        # ! NO HACEMOS UN PATCH A MESSAGE LOGGING 
        cls.log = MessageLogging_Adapter_proxy.MessageLogging()
        cls.repository= repositoryMessages_mock
        cls.query = QueryPrompt_Adapter_stub.QueryPrompt()
        cls.backendMockLoadder = BackendLoading_Adapter_proxy_stub.BackendLoading()
        
        # MOCK CONSUME
        MockMessages = [
            {'role':'system','content':'hello world'}
        ]
        # sets the getter
        repositoryMessages_mock.messagesHistory.return_value = MockMessages
        # sets the setter mock 
        repositoryMessages_mock.messagesHistory = {'role':'alice','content':'hello!'}
        # sets the deletter mock
        del repositoryMessages_mock.messagesHistory
        cls.renderMessageMock = Mock()
        cls.renderMessageMock.return_value = """jcskcnjskncjskncskj
        baaaa user input:
        
        response:
        21
        212
        212
        """
        cls.repository.renderMessage = cls.renderMessageMock 
        # APP
        cls.backend = Backend(
            userQuery=cls.query,
            messagesRepository=cls.repository,
            log=cls.log,
            backendLoader=cls.backendMockLoadder
        )
        
        
    def test_loadModel(self):
        MOCK_BACKEND = ModelEntity(
            modelName='ranni',
            modelPath='D://USER',
            systemQueryExpansion="""
    You are a knowledgeable financial research assistant. 
    Your users are inquiring about an annual report. 
    For the given question, propose up to five related questions to assist them in finding the information they need. 
    Provide concise, single-topic questions (withouth compounding sentences) that cover various aspects of the topic. 
    Ensure each question is complete and directly related to the original inquiry. 
    List each question on a separate line without numbering.
            """,
            systemPresentationResources="""
    respond to the current question {{user_input}}
    using the follow resources {% for resource of resources%} * {{resource}} \n {%endfor%}
            """,
            temperature=0.7,
            top_p=0.5,
            top_k=0.5,
            num_beams=33,
            max_new_tokens=1024,
            repetition_penalty=0.7,
            early_stopping=True,
            load_in_8bit=True, 
        )
        self.assertEqual(
            self.backend.loadModel(specsEntity=MOCK_BACKEND)([1]),
            self.backendMockLoadder.loadBackend(model=MOCK_BACKEND)([1])
        )
    @patch.object(UserRequest,'request',new_callable=PropertyMock)
    def test_ragProcessInput(self,mock_request):
        MOCK_BACKEND = ModelEntity(
            modelName='ranni',
            modelPath='D://USER',
            systemQueryExpansion="""
    You are a knowledgeable financial research assistant. 
    Your users are inquiring about an annual report. 
    For the given question, propose up to five related questions to assist them in finding the information they need. 
    Provide concise, single-topic questions (withouth compounding sentences) that cover various aspects of the topic. 
    Ensure each question is complete and directly related to the original inquiry. 
    List each question on a separate line without numbering.
            """,
            systemPresentationResources="""
    respond to the current question {{user_input}}
    using the follow resources {% for resource of resources%} * {{resource}} \n {%endfor%}
            """,
            temperature=0.7,
            top_p=0.5,
            top_k=0.5,
            num_beams=33,
            max_new_tokens=1024,
            repetition_penalty=0.7,
            early_stopping=True,
            load_in_8bit=True, 
        )
        self.assertEqual(
            self.backend.loadModel(specsEntity=MOCK_BACKEND)([1]),
            self.backendMockLoadder.loadBackend(model=MOCK_BACKEND)([1])
        )
        
        # MOCK CONSUME
        MOCK_USERINPUT = 'what is the meaning of the live ?'
        mock_request.return_value = MOCK_USERINPUT
        process = self.backend.ragProcessInput(input=UserRequest())
        mock_result = self.backend.generator([''])
        self.renderMessageMock.assert_called()
        self.assertEqual(process,
                         mock_result)
        #                 
        #                 )
        
if __name__ =='__main__':
    unittest.main()