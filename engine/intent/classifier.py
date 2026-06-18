from engine.models.semantic.models import RoleFrame
from engine.models.intent.models import IntentRule, INTENT_RULES, Intent
from engine.intent.evaluator import score_rule

def classify_intent(frame:RoleFrame):
    best_intent = None
    best_score = 0

    for rule in INTENT_RULES:
        score = score_rule(rule, frame)

        if score > best_score:
            best_score = score
            best_intent = rule

    return Intent(best_intent, best_score)

           
    