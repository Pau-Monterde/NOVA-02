class IntentNotFoundException(Exception):
    def __init__(self):
        super().__init__("Cannot detect an intent")