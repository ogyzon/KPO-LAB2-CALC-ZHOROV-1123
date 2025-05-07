import math


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
        return ""

    def evaluate(self):
        try:
            # Заменяем тригонометрические функции на вызовы math
            expr = self._expression
            expr = expr.replace('sin', 'math.sin')
            expr = expr.replace('cos', 'math.cos')
            expr = expr.replace('tan', 'math.tan')

            result = str(eval(expr))
            self._expression = result
            return result
        except Exception:
            self._expression = ""
            return "Ошибка"