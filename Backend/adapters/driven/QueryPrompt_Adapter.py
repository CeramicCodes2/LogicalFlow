from Repository.app.schemas.PromptRequest import PromptRequest
from ...ports.drivens.for_queryPrompt import ForQueryPrompt

class QueryPrompt(ForQueryPrompt):
    def getData(self, request: str|list[str]) -> PromptRequest:
        return PromptRequest(queryRequest=[],top=4)
        #return super().getData(request)
