import re
from transformers import pipeline
import spacy, chunk, token
from engine.models.semantic.models import RoleFrame
from engine.semantic.extractor import extract_roles
from engine.parser.text_parsing import parse_text
from engine.intent.classifier import classify_intent
from engine.models.intent.models import Intent
from engine.executor.executor import execute
from engine.models.executor.models import ExecutionResult

from engine.parser.text_parsing import parse_text


class RequestContext():
    def __init__(self, string:str):

        self.string:str = string.lower()
        self.w_list:list[str] = re.sub(r"([^\w\s])", r" \1 ", self.string).lower().split()

        # Nivel de estado de animo
        self.emotion = pipeline("text-classification", model="monologg/bert-base-cased-goemotions-original")(self.string)

        # Texto parseado 
        self.parsed_text = parse_text(string)

        # Entidades separadas
        self.role_frame:RoleFrame = extract_roles(parse_text(self.string))

        # Intención
        self.intent:Intent = classify_intent(self.role_frame)

        # Ejecución
        self.execution_result:ExecutionResult

    def execution(self):
        execute(self.intent)
        

     
            
            



