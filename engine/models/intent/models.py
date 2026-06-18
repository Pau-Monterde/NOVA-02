from engine.executor.skills.file_sender import send_file

class IntentRule:
    def __init__(self, name:str, actions:list[str], required_roles:list[str], execution = None):
        self.name = name
        self.actions = actions
        self.required_roles = required_roles
        self.execution = execution

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

class Intent:
    def __init__(self, rule:IntentRule, score:float):
        self.rule = rule
        self.score = score

