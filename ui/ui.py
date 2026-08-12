import webview
from jinja2 import Environment, FileSystemLoader
from ui.api import Api


env = Environment(
    loader=FileSystemLoader("ui/templates")
)

api = Api()

template = env.get_template("index.html")

def user_interface():
    window = webview.create_window(
        title = "NOVA-02",
        html = template.render(),
        js_api = api,
        width = 1200,
        height = 700
    )

    def test():
        window.evaluate_js(
            "receive_event('Hola desde Python')"
        )

    webview.start(test)

    return window
