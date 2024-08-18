from Repository.app.schemas.PromptRequest import PromptRequest
from ...ports.drivens.for_queryPrompt import ForQueryPrompt
MOCK_DATA = ['HELLO'*4]
class QueryPrompt(ForQueryPrompt):
    def getData(self, request: str|list[str]) -> PromptRequest:
        return PromptRequest(queryRequest=MOCK_DATA,top=4)
        #return super().getData(request)
