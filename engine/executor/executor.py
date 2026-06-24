from engine.models.context_model import RequestContext
from engine.models.context_model import ExecutionResult
from engine.models.executor_models import ExecutionResult
from engine.models.exceptions.IntentNotFound import IntentNotFoundException

def execute(context:RequestContext):
    print("HOla munod")
    context.intent.rule.execution(context)
    execution_result:ExecutionResult = ExecutionResult(True)
    return execution_result

