class InvalidExpression(Exception):
    def __init__(self, message='The expression is invalid'):
        super().__init__(message)

class InvalidStrategy(Exception):
    def __init__(self, message='Strategy not supported'):
        super().__init__(message)
