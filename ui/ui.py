import webview
from webview import Window
from ui.api import Api
from engine.models.queues_model import EngineQueues
import json

def listen_responses(window:Window, engine_queues:EngineQueues):
    while(True):
        response = engine_queues.response_queue.get()
        window.evaluate_js(f"write_response({json.dumps(response)})")

def user_interface(api:Api, engine_queues:EngineQueues):
    window = webview.create_window(
        title = "NOVA-02",
        url = "ui/templates/index.html",
        js_api = api,
        width = 1200,
        height = 700,
    )

    print(window.events)

    webview.start(func = listen_responses, args = (window, engine_queues), http_server=True)

    return window
