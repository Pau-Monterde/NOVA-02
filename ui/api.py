from queue import Queue
from engine.models.queues_model import EngineQueues
from webview import Window

class Api:
    def __init__(self, engine_queues:EngineQueues):
        self.engine_queues = engine_queues

    def put_input(self, string:str):
        self.engine_queues.input_queue.put(string)