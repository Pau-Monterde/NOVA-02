from engine.models.intent_models import IntentRule
from engine.models.semantic_models import RoleFrame

def score_rule(rule:IntentRule, frame:RoleFrame):
    score = 0

    action = frame.get_role("ACTION")

    if action and action.value in rule.actions:
        score += 50

    roles_present = {
        role.role
        for role in frame.roles
    }

    for required in rule.required_roles:
        if required in roles_present:
            score += 25

    return score