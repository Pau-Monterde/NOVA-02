from queue import Queue

class EngineQueues():
    def __init__(self):
        self.input_queue = Queue()
        self.response_queue = Queue()