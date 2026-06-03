import re
from transformers import pipeline
import spacy, chunk, token
from engine.models.text_parser.parsed_text import ParsedText
from engine.intent.intent_manager import detect_intent
from engine.models.intent_models import Intent
from engine.parser.text_parsing import parse_text


class Prompt():
    def __init__(self, string:str):

        self.string:str = string.lower()
        self.w_list:list[str] = re.sub(r"([^\w\s])", r" \1 ", self.string).lower().split()

        # Nivel de estado de animo
        self.emotion = pipeline("text-classification", model="monologg/bert-base-cased-goemotions-original")(self.string)

        # Intención
        self.intent:Intent | None = detect_intent(self.w_list)

        # Entidades separadas
        self.parsed_text:ParsedText = parse_text(string)
        

     
            
            



