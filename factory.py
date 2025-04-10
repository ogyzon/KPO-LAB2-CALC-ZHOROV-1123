from calculator import Calculator
from components import DisplayComponent, ButtonsComponent

class CalculatorFactory:
    def create_calculator(self, root):
        display_component = DisplayComponent()
        buttons_component = ButtonsComponent()
        return Calculator(root, display_component, buttons_component)
