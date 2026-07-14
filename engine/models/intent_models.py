class IntentRule:
    def __init__(self, name:str, actions:list[str], required_roles:list[str], keywords:list[str], min_score:float = 60,execution = None):
        self.name = name
        self.actions = actions
        self.required_roles = required_roles
        self.keywords = keywords
        self.min_score = min_score
        self.execution = execution
        
class Intent:
    def __init__(self, rule:IntentRule, score:float):
        self.rule = rule
        self.score = score


