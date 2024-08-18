from Backend.app.schemas.UserRequest import UserRequest
from ...ports.drivers.for_inputPrompit import ForInputPrompt

class InputPrompt(ForInputPrompt):
    def __init__(self,backend) -> None:
        self.backend = backend
        
    def processInput(self, input: UserRequest):
        return self.backend.processInput(input)
    
