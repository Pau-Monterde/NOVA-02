from engine.models.context_model import RequestContext, ContextStatus
from engine.models.exceptions.context_exceptions import IntentNotFoundException

def execute(context:RequestContext):
    print(context.intent.rule.name)
    context.intent.rule.execution(context)
    return 

