class CalculatorModel:
    def __init__(self):
        self._expression = ""
    
    @property
    def expression(self):
        return self._expression
    
    @expression.setter
    def expression(self, value):
        self._expression = value
    
    def clear(self):
        self._expression = ""
    
    def evaluate(self):
        try:
            result = str(eval(self._expression))
            self._expression = result
            return result
        except Exception:
            self._expression = ""
            return "Ошибка"