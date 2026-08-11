from engine.models.semantic_models import RoleFrame
from engine.models.intent_models import Intent, IntentRule, ContextIntent
from engine.models.parser_models import ParsedText
from engine.intent.intent_rules import *
from engine.executor.skills.file_sender import send_file
from engine.executor.skills.app_opening import open_app
from engine.executor.skills.clock import show_current_time
from engine.intent.evaluator import score_rule
from engine.models.exceptions.context_exceptions import IntentNotFoundException
from engine.models.speech_act import SpeechAct

def act_list(speech_act:SpeechAct):
    if speech_act == SpeechAct.EXECUTION.value:
        return EXECUTION_RULES
    elif speech_act == SpeechAct.INFORMATION.value:
        return INFORMATION_RULES
    elif speech_act == SpeechAct.EXPLANATION.value:
        return EXPLANATION_RULES
    elif speech_act == SpeechAct.CONVERSATION.value:
        return CONVERSATION_RULES
    elif speech_act == SpeechAct.CONFIRMATION.value:
        return CONFIRMATION_RULES
    elif speech_act == SpeechAct.CLARIFICATION.value:
        return CLARIFICATION_RULES
    elif speech_act == SpeechAct.CORRECTION.value:
        return CORRECTION_RULES
    elif speech_act == SpeechAct.FEEDBACK.value:
        return FEEDBACK_RULES
    elif speech_act == SpeechAct.UNKNOWN.value:
        return UNKNOWN_RULES
    
def classify_intent(frame:RoleFrame, p_text:ParsedText, speech_act:SpeechAct, context_intents:list[ContextIntent] | None = None):
    print(speech_act)
    
    intent_list = act_list(speech_act)

    scored_intents = {}
    best_intent = None
    best_score = 0

    if context_intents:
        print("Avaluando por context intent")
        for rule in context_intents:
            score = score_rule(rule, frame, p_text)

            if rule.min_score:
                if score >= rule.min_score:
                    scored_intents[rule] = score

            elif score >= 10:
                scored_intents[rule] = score

    for rule in intent_list:
        score = score_rule(rule, frame, p_text)

        if rule.min_score:
            if score >= rule.min_score:
                scored_intents[rule] = score

        elif score >= 10:
            scored_intents[rule] = score

    for rule, score in scored_intents.items():
        if score > best_score:
            best_score = score
            best_intent = rule
    
    if not best_intent:
        raise IntentNotFoundException()

    return Intent(best_intent, best_score)

           
    