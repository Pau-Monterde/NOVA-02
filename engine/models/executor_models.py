from engine.models.parser_models import ParserExceptions

class ExecutionResult():
    def __init__(self, success:bool, fatal_error:Exception | None = None, parser_exceptions:ParserExceptions | None = None, ):
        self.success = success

    