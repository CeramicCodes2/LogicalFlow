from dataclasses import dataclass
@dataclass
class PromptRequest:
    queryRequest:str|list[str]
    top:int
