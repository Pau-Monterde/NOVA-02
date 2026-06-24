class ExecutionResult():
    def __init__(self, success:bool, error:Exception | None = None):
        self.success = success
        self.error = error
    