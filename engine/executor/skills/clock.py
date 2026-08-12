import time
from engine.models.context_model import RequestContext

def show_current_time(context: RequestContext):
    current_time = time.strftime("%H:%M")
    context.response_raw = f"The current time is: {current_time}"
    return context