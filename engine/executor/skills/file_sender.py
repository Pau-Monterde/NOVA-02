from tkinter.messagebox import showinfo
from engine.models.semantic_models import RoleEntity, RoleType
from engine.models.context_model import RequestContext
from engine.models.executor_models import ExecutionResult
from engine.models.intent_models import IntentRule

def send_file(context:RequestContext):
    roles_list = context.role_frame.roles

    for role_ent in roles_list:
        if role_ent.role == RoleType.RECIPIENT:
            recipient = role_ent.value

    showinfo(message=f"Enviando archivo a {recipient}")
    return ExecutionResult(True)

  
    