from queue import Queue

class Api:
    def __init__(self, input_queue:Queue):
        self.input_queue = input_queue

    def saludar(self, nombre):
        print(f"Hola, {nombre}")

    def put_input(self, string:str):
        self.input_queue.put(string)