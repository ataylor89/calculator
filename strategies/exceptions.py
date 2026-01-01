class InvalidExpression(Exception):
    def __init__(self, expression, message='The expression is invalid'):
        super().__init__(message)

class InvalidStrategy(Exception):
    def __init__(self, expression, message='Strategy not supported'):
        super().__init__(message)
