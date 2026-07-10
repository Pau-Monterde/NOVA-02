class IntentRule:
    def __init__(self, name:str, actions:list[str], required_roles:list[str], keywords:list[str], execution = None):
        self.name = name
        self.actions = actions
        self.required_roles = required_roles
        self.keywords = keywords
        self.execution = execution
        
class Intent:
    def __init__(self, rule:IntentRule, score:float):
        self.rule = rule
        self.score = score


