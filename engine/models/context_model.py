from typing import Any
from engine.models.semantic_models import RoleFrame
from engine.models.parser_models import ParsedText
from engine.models.intent_models import Intent
from engine.models.parser_models import ParserExceptions
from engine.models.semantic_models import SemanticExceptions
from engine.models.bus_model import EventBus

class ContextStatus():
    def __init__(self, success:bool = True, fatal_exception:Exception | None = None, parser_exceptions:ParserExceptions | None = None, semantic_exceptions:SemanticExceptions | None = None):
        self.success = success
        self.fatal_exception = fatal_exception
        self.parser_exceptions = parser_exceptions
        self.semantic_exceptions = semantic_exceptions


class RequestContext():

    def __init__(self, prompt_str:str, status:ContextStatus, parsed_text:ParsedText, role_frame:RoleFrame | None = None, intent:Intent | None = None, context_intents:list | None = None):

        self.prompt_str = prompt_str

        # Texto parseado 
        self.parsed_text = parsed_text

        # Entidades separadas
        self.role_frame = role_frame 

        # Intención
        self.intent = intent 

        # Respuesta del intent
        self.response_raw:str

        # Respuesta definitiva procesada por el llm
        self.response:str

        self.context_intents = context_intents

        # Ejecución
        self.status = status

        # Buzón de eventos
        self.event_bus = EventBus()
    

        
         
    
    

        
        

     
            
            



