from engine.models.intent.models import Intent, IntentRule, INTENT_RULES
from engine.models.executor.models import ExecutionResult
from engine.models.exceptions.IntentNotFound import IntentNotFoundException

def execute(intent:Intent):
    try: 
        success, data, error = intent.rule.execution()
        return ExecutionResult(success, data, error)
    except Exception as e:
        print("Ha habido un error")
