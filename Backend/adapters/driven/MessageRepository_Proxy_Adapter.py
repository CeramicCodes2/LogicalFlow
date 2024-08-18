from Backend.app.schemas.ModelEntity import ConversationMessages
from ...ports.drivens.for_messageFormatting import ForMessageRepository
from jinja2 import Template
MOCK_DATA = ConversationMessages(
    messages=[{
        "role":"system","content":"Hello world!"
    }],jinjaTemplateFormat=''
)
class MessageRepository(ForMessageRepository):
    def __init__(self) -> None:
        super().__init__()
        self._template = ''
        self._messagesHistory = ConversationMessages(messages=[dict()],jinjaTemplateFormat='')
    @property
    def template(self):
        return self._messagesHistory.jinjaTemplateFormat
    @template.setter
    def template(self,template:str):
        self._messagesHistory.jinjaTemplateFormat = template
    @template.deleter
    def template(self):
        self._messagesHistory.jinjaTemplateFormat = ''
    @property
    def messagesHistory(self,message:dict[str,str]):
        return self._messagesHistory
    @messagesHistory.setter
    def messagesHistory(self,arg:dict[str,str]):
        self._messagesHistory.messages.append(arg)
    @messagesHistory.deleter
    def messagesHistory(self):
        self._messagesHistory = [dict()]
    def formatMessagesList(self, messages: ConversationMessages) -> str:
        template = Template(self.template)
        return template.render(messages)