from engine.models.context_model import RequestContext

def open_app(context: RequestContext):
    print(f"Abriendo {context.role_frame.get_role}")
    print("App abierta")
    