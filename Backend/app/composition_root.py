from .backend import Backend
from ..adapters.driven import (
    MessageLogging_Adapter_proxy,
    MessageRepository_Proxy_Adapter,
    QueryPrompt_Adapter_stub,
    BackendLoading_Adapter_proxy_stub
)
from ..adapters.drivers import (
    ModelLoadder_Proxy_Adapter,
    InputPrompt_adapter,
    
)
def compositionMock():
    # DRIVENS
    log = MessageLogging_Adapter_proxy.MessageLogging()
    repository= MessageRepository_Proxy_Adapter.MessageRepository()
    query = QueryPrompt_Adapter_stub.QueryPrompt()
    backendLoader = BackendLoading_Adapter_proxy_stub.BackendLoading()
    # APP 
    backend = Backend(
        userQuery=query,
        messagesRepository=repository,
        log=log,
        backendLoader=backendLoader
    )
    # DRIVERS
    backendLoadder = ModelLoadder_Proxy_Adapter.BackendLoadder(backend)
    inputPrompt = InputPrompt_adapter.InputPrompt(backend)
    return backendLoadder,inputPrompt
def composition_root():
    # DRIVENS
    log = MessageLogging_Adapter_proxy.MessageLogging()
    repository= MessageRepository_Proxy_Adapter.MessageRepository()
    query = QueryPrompt_Adapter_stub.QueryPrompt()
    backendLoader = BackendLoading_Adapter_proxy_stub.BackendLoading()
    # APP 
    backend = Backend(
        userQuery=query,
        messagesRepository=repository,
        log=log,
        backendLoader=backendLoader
    )
    # DRIVERS
    backendLoadder = ModelLoadder_Proxy_Adapter.BackendLoadder(backend)
    inputPrompt = InputPrompt_adapter.InputPrompt(backend)
    return backendLoadder,inputPrompt

backendLoadder,inputPrompt = compositionMock()


