from engine.models.semantic_models import RoleFrame
from engine.models.intent_models import Intent, IntentRule
from engine.executor.skills.file_sender import send_file
from engine.intent.evaluator import score_rule

INTENT_RULES = [
    IntentRule(
        name="SEND_FILE",
        actions=["send"],
        required_roles=["TARGET", "RECIPIENT"],
        execution = send_file
    ),

    IntentRule(
        name="PLAY_MEDIA",
        actions=["play"],
        required_roles=["TARGET"]
    ),

    IntentRule(
        name="OPEN_APP",
        actions=["open"],
        required_roles=["TARGET"]
    )
]

def classify_intent(frame:RoleFrame):
    best_intent = None
    best_score = 0

    for rule in INTENT_RULES:
        score = score_rule(rule, frame)

        if score > best_score:
            best_score = score
            best_intent = rule

    return Intent(best_intent, best_score)

           
    