import re
from transformers import pipeline
from engine.models.context_model import RequestContext, ContextStatus
from engine.models.exceptions.context_exceptions import LinguisticAnalyzerFatalException, ContextNotCreatedException
from engine.semantic_extractor import extract_roles
from engine.parser.text_parsing import parse_text
from engine.intent.classifier import classify_intent
from engine.parser.text_parsing import parse_text
    
def generate_rcontext(prompt:str):
        context_status = ContextStatus()
        #w_list = re.sub(r"([^\w\s])", r" \1 ", string).lower().split()
        try:
                parsed_text, context_status.parser_exceptions = parse_text(prompt)
        except LinguisticAnalyzerFatalException as e:
                context_status.fatal_exception = e
                context_status.success = False
                raise ContextNotCreatedException(context_status.fatal_exception)


        # role_frame = extract_roles(parsed_text)
        # try: 
        #         intent = classify_intent(role_frame)
        # except IntentNotFoundException as infe:
        #         context_status.fatal_error = infe
        #         print("Sorry, i didn't understood what do you want me to do")

        return RequestContext(prompt_str=prompt, parsed_text=parsed_text, status=context_status)


        


