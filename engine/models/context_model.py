from typing import Any
from engine.models.semantic_models import RoleFrame
from engine.models.parser_models import ParsedText
from engine.models.intent_models import Intent
from engine.models.executor_models import ExecutionResult

from engine.parser.text_parsing import parse_text


class RequestContext():

    def __init__(self, string:str):

        self.string:str = string
        self.w_list:list[str] = []

        # Nivel de estado de animo
        self.emotion:list[dict[str, Any]] = []

        # Texto parseado 
        self.parsed_text:ParsedText | None = None

        # Entidades separadas
        self.role_frame:RoleFrame | None = None 

        # Intención
        self.intent:Intent | None = None 

        # Ejecución
        self.execution_result:ExecutionResult | None = None
    

        
         
    
    

        
        

     
            
            



