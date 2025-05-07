from model import CalculatorModel


class CalculatorViewModel:
    def __init__(self, model):
        self.model = model
        self.input_text = ""
        self.update_display_callback = None

    def on_button_click(self, char):
        if char == "C":
            self.input_text = self.model.clear()  # Исправлено: теперь возвращает пустую строку
        elif char == "=":
            result = self.model.evaluate()
            self.input_text = result
        else:
            self.model.expression += str(char)
            self.input_text = self.model.expression

        if self.update_display_callback:
            self.update_display_callback(self.input_text)