import re
from transformers import pipeline
from engine.models.context_model import RequestContext
from engine.semantic_extractor import extract_roles
from engine.parser.text_parsing import parse_text
from engine.intent.classifier import classify_intent
from engine.parser.text_parsing import parse_text
from engine.executor.executor import execute
    
def generate_rcontext(string:str):
    context = RequestContext(string)

    context.string = string.lower()
    context.w_list = re.sub(r"([^\w\s])", r" \1 ", context.string).lower().split()
    context.emotion = pipeline("text-classification", model="monologg/bert-base-cased-goemotions-original")(context.string)
    context.parsed_text = parse_text(context.string)
    context.role_frame = extract_roles(context.parsed_text)
    context.intent = classify_intent(context.role_frame)
    context.execution_result = execute(context)

    return(context)


