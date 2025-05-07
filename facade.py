import tkinter as tk


class CalculatorFacade:
    def __init__(self, root):
        self.root = root
        self.setup_ui()

    def setup_ui(self):
        from model import CalculatorModel
        from viewmodel import CalculatorViewModel
        from command import CalculatorCommand
        from components import DisplayComponent, ButtonsComponent

        self.model = CalculatorModel()
        self.viewmodel = CalculatorViewModel(self.model)
        self.command = CalculatorCommand(self.viewmodel)

        self.input_text = tk.StringVar()
        self.display_component = DisplayComponent(self.input_text)
        self.buttons_component = ButtonsComponent(self.command)

        self.display_component.create_display(self.root)
        self.buttons_component.create_buttons(self.root)

    def update_display(self, text):
        self.input_text.set(text)