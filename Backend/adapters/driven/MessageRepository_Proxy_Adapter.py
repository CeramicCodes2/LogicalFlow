from Backend.app.schemas.ModelEntity import ConversationMessages
from ...ports.drivens.for_messageFormatting import ForMessageRepository

MOCK_DATA = ConversationMessages(
    messages=[{
        "role":"system","content":"Hello world!"
    }]
)
class MessageRepository(ForMessageRepository):
    def __init__(self) -> None:
        super().__init__()
        self._messagesHistory = ConversationMessages(messages=[dict()],jinjaTemplateFormat='')
    @property
    def messagesHistory(self,message:dict[str,str]):
        return self._messagesHistory
    @messagesHistory.setter
    def messagesHistory(self,arg:dict[str,str]):
        self._messagesHistory.messages.append(arg)
    @messagesHistory.deleter
    def messagesHistory(self):
        self._messagesHistory = ConversationMessages(messages=[dict()],jinjaTemplateFormat='')
    def formatMessagesList(self, messages: ConversationMessages):
        ...