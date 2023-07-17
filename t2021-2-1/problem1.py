class Calculator:
    a: float
    b: float
    operation: str

    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation

    def calculate(self):
        if self.operation == 'Addition':
            return self.a + self.b
        if self.operation == 'Subtraction':
            return self.a - self.b
        if self.operation == 'Multiplication':
            return self.a * self.b
        if self.operation == 'Division':
            return self.a / self.b
