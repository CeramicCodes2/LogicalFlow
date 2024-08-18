from dataclasses import dataclass
@dataclass
class ModelEntity:
    modelName:str
    modelPath:str
    systemQueryExpansion:str
    systemPresentationResources:str
    temperature:float = 0.6
    top_p:float = 0.75
    top_k:float = 50
    num_beams:int = 50
    max_new_tokens:int = 2048
    repetition_penalty:float = 1.4
    early_stopping:bool = True
    load_in_8bit:bool = False
    hook_storage:int = 4
    

class GeneratorModel:
    def __init__(self,generator) -> None:
        self.generator = generator

@dataclass
class ConversationMessages:
    messages:list[dict[str,str]]
    jinjaTemplateFormat:str    