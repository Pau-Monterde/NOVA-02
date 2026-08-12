import webview
from jinja2 import Environment, FileSystemLoader
from ui.api import Api

def user_interface(api):

    env = Environment(loader=FileSystemLoader("ui/templates"))

    template = env.get_template("index.html")


    window = webview.create_window(
        title = "NOVA-02",
        html = template.render(),
        js_api = api,
        width = 1200,
        height = 700
    )

    webview.start()

    return window
