from engine.models.intent.models import Intent, INTENT_RULES
from engine.models.executor.models import ExecutionResult

def execute(intent:Intent):
    return ExecutionResult(True)