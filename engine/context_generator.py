import re
from engine.models.context_model import RequestContext, ContextStatus
from engine.models.exceptions.context_exceptions import LinguisticAnalyzerFatalException, ContextNotCreatedException, IntentNotFoundException, AnyRoleAssignmentException
from engine.semantic_extractor import roles_extraction
from engine.parser.text_parsing import parse_text
from engine.intent.classifier import classify_intent
from engine.parser.text_parsing import parse_text
from engine.models.speech_act import SpeechAct
from engine.speech_act_classifier import classify_speech_act
    
def generate_rcontext(prompt:str):
        context_status = ContextStatus(True)
        #w_list = re.sub(r"([^\w\s])", r" \1 ", string).lower().split()
        try:
                parsed_text, context_status.parser_exceptions = parse_text(prompt)
        except LinguisticAnalyzerFatalException as e:
                context_status.fatal_exception = e
                raise ContextNotCreatedException(context_status.fatal_exception)
        
        speech_act = classify_speech_act(parse_text)

        role_frame, semantic_exceptions_list = roles_extraction(parsed_text)
        if semantic_exceptions_list: context_status.semantic_exceptions = semantic_exceptions_list

        try: 
                intent = classify_intent(role_frame, parsed_text)
        except IntentNotFoundException as infe:
                intent = None
                context_status.fatal_exception = infe
                raise ContextNotCreatedException(context_status.fatal_exception)
        
        return RequestContext(prompt, context_status, parsed_text, role_frame, intent)


        


