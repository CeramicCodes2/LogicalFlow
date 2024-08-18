from dataclasses import dataclass,asdict
@dataclass
class Message:
    content:str
    rol:str
    def toDict(self):
        return asdict(self)
    
@dataclass
class UserRequest:
    request:str = ''
    significantLinks:str = ''
    significantResources:str = ''
    def toDict(self):
        return Message(self.request,'user')
    