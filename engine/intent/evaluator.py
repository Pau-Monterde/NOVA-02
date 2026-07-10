from engine.models.intent_models import IntentRule
from engine.models.semantic_models import RoleFrame, RoleEntity
from engine.models.parser_models import ParsedText
from engine.models.exceptions.context_exceptions import ActionNotFoundException, KeywordsNotFoundException, RequiredRolesNotFoundException

def action_scoring(rule:IntentRule, frame:RoleFrame, p_text:ParsedText, score:int):
    initial_score = score
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
            #score -= 20
            pass

    if initial_score == score:
        raise ActionNotFoundException()
    
    return score

def required_roles_scoring(rule:IntentRule, frame:RoleFrame, score:int):
    initial_score = score

    for role in rule.required_roles:
        if frame.get_role(role):
            score += 15
    
    if initial_score == score:
        raise RequiredRolesNotFoundException()
    
    return score

def keyword_scoring(rule:IntentRule, p_text:ParsedText, score:int):
    initial_score = score

    for token in p_text.linguistic_analisys.pos:
        if token.lemma in rule.keywords:
            if score < 0:
                score = 0
            score += 10

    if initial_score == score:
        raise KeywordsNotFoundException()
    
    return score

def score_rule(rule:IntentRule, frame:RoleFrame, p_text:ParsedText):
    rule_scoring_exceptions:list[Exception] = []
    score = 0

    try: 
        score = required_roles_scoring(rule, frame, score)
    except RequiredRolesNotFoundException as e:
        rule_scoring_exceptions.append(e)
        score -= 10

    try: 
        score = keyword_scoring(rule, p_text, score)
    except KeywordsNotFoundException as e:
        rule_scoring_exceptions.append(e)
        score -= 10

    if score <= 0:
        return score
    
    try:
        score = action_scoring(rule, frame, p_text, score)
    except ActionNotFoundException as e:
        rule_scoring_exceptions.append(e)

    return score