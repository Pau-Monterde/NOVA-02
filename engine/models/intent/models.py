class IntentRule:
    def __init__(self, name:str, actions:list[str], required_roles:list[str]):
        self.name = name
        self.actions = actions
        self.required_roles = required_roles

INTENT_RULES = [
    IntentRule(
        name="SEND_FILE",
        actions=["send"],
        required_roles=["TARGET", "RECIPIENT"]
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
    def __init__(self, name:str, score:float):
        self.name = name
        self.score = score