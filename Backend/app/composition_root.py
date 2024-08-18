from .backend import Backend
from ..adapters.driven import *
from ..adapters.drivers import *
def compositionMock():
    # DRIVENS
    log = MessageLogging_Adapter_proxy.MessageLogging()
    repository= MessageRepository_Proxy_Adapter.MessageRepository()
    query = QueryPrompt_Adapter_stub.QueryPrompt()
    
    # APP 
    backend = Backend(
        userQuery=query,
        messagesRepository=repository,
        log=log
    )
    # DRIVERS
    backendLoadder = Backend_Loadder_Proxy_Adapter.BackendLoadder(backend)
    inputPrompt = InputPrompt_adapter.InputPrompt(backend)
    return backendLoadder,inputPrompt

backendLoadder,inputPrompt = compositionMock()


