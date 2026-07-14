import json
import os
from tkinter.messagebox import showinfo
from engine.models.context_model import RequestContext


def open_app(context: RequestContext):
    try:
        target_app = context.role_frame.get_role("TARGET").value
    except Exception as e:
        pass
    print(target_app)
    showinfo(message=f"Abriendo {target_app}")

    with open("./data/applications.json", "r", encoding="utf-8") as file:
        apps = json.load(file)
        
    app_path = apps[target_app]["path"]
    print(app_path)
    run_status = os.startfile(app_path)

    print("App abierta")
    