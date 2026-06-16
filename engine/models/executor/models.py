class ExecutionResult():
    def __init__(self, success:bool, data = None, error = None):
        self.success = success
        self.data = data
        self.error = error