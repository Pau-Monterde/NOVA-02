class ContextNotCreatedException(Exception):
    def __init__(self, fatal_exception:Exception):
        super().__init__(f"NOVA-02 can't create context --> {fatal_exception}")

class POSNotFoundInDocException(Exception):
    def __init__(self):
        super().__init__("There aren't POS tokens in doc")

class NERNotFoundInDocException(Exception):
    def __init__(self):
        super().__init__("There aren't NER entities in doc")

class LinguisticAnalyzerFatalException(Exception):
    def __init__(self, exception_causer:Exception):
        super().__init__(f"A fatal exception makes NOVA-02 unable to process your request --> {exception_causer}")

class NotRootVerbInContextException(Exception):
    def __init__(self):
        super().__init__("There isn't a root verb in context")

class NotDirectObjInContextException(Exception):
    def __init__(self):
        super().__init__("There isn't a direct object in context")

class NotIndObjsInContextException(Exception):
    def __init__(self):
        super().__init__("There isn't a direct object in context")

class IntentNotFoundException(Exception):
    def __init__(self):
        super().__init__("Cannot detect an intent")

class AnyRoleAssignmentException(Exception):
    def __init__(self):
        super().__init__("Cannot assign roles")

class RequiredRolesNotFoundException(Exception):
    def __init__(self):
        super().__init__("There aren't required roles in context")

class KeywordsNotFoundException(Exception):
    def __init__(self):
        super().__init__("There aren't keywords in context")

class ActionNotFoundException(Exception):
    def __init__(self):
        super().__init__("There isn't an action in context")