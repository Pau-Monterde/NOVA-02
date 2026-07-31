class IntentRule:
    def __init__(self, name:str, actions:list[str], required_roles:list[str] | None = None, keywords:list[str] | None = None, min_score:float = 60, context_intents:list | None = None, execution = None):
        self.name = name
        self.actions = actions
        self.required_roles = required_roles
        self.keywords = keywords
        self.min_score = min_score
        self.context_intents = context_intents
        self.execution = execution

class ContextIntent(IntentRule):
    def __init__(self, name:str, actions:list[str], required_roles:list[str] | None = None, keywords:list[str] | None = None, min_score:float = 60, context_intents:list | None = None, execution = None):
        super().__init__(name, actions, required_roles, keywords, min_score, execution)
        
class Intent:
    def __init__(self, rule:IntentRule, score:float):
        self.rule = rule
        self.score = score




