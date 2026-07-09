from engine.models.semantic_models import RoleFrame
from engine.models.intent_models import Intent, IntentRule
from engine.models.parser_models import ParsedText
from engine.executor.skills.file_sender import send_file
from engine.executor.skills.app_opening import open_app
from engine.intent.evaluator import score_rule
from engine.models.exceptions.context_exceptions import IntentNotFoundException

INTENT_RULES = [
    IntentRule(
        name="OPEN_APP",
        actions=["open"],
        required_roles=["TARGET"],
        execution = open_app
    ),

    IntentRule(
        name="SEND_FILE",
        actions=["send"],
        required_roles=["TARGET", "RECIPIENT"],
        execution = send_file
    )
]

def classify_intent(frame:RoleFrame, p_text:ParsedText):
    best_intent = None
    best_score = 0

    for rule in INTENT_RULES:
        score = score_rule(rule, frame, p_text)

        if score > best_score:
            best_score = score
            best_intent = rule
    
    if not best_intent:
        raise IntentNotFoundException()

    return Intent(best_intent, best_score)

           
    