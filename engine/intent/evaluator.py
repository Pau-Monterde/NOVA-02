from engine.models.intent_models import IntentRule
from engine.models.semantic_models import RoleFrame, RoleEntity
from engine.models.parser_models import ParsedText

def score_rule(rule:IntentRule, frame:RoleFrame, p_text:ParsedText):
    score = 0
    
    action:RoleEntity = frame.get_role("ACTION")

    if action and action.value in rule.actions:
        score += 50
    
    else: 
        not_roled_actions_found = 0
        for token in p_text.linguistic_analisys.pos:
            if token.lemma in rule.actions:
                not_roled_actions_found += 1
                score += 25

        if not_roled_actions_found == 0:
            score -= 50

    return score