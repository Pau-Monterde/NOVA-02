from llm_manager import detect_speech_act
from engine.intent.intent_rules import *

def speech_act_selection(phrase:str):
    speech_act = detect_speech_act(phrase)
    print(speech_act)
    if speech_act == "EXECUTION":
        return EXECUTION_RULES
    elif speech_act == "INFORMATION":
        return INFORMATION_RULES
    elif speech_act == "EXPLANATION":
        return EXPLANATION_RULES
    elif speech_act == "CONVERSATION":
        return CONVERSATION_RULES
    elif speech_act == "CONFIRMATION":
        return CONFIRMATION_RULES
    elif speech_act == "CLARIFICATION":
        return CLARIFICATION_RULES
    elif speech_act == "CORRECTION":
        return CORRECTION_RULES
    elif speech_act == "FEEDBACK":
        return FEEDBACK_RULES
    elif speech_act == "UNKNOWN":
        return UNKNOWN_RULES
    