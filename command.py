from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self, char):
        pass


class CalculatorCommand(Command):
    def __init__(self, viewmodel):
        self.viewmodel = viewmodel

    def execute(self, char):
        self.viewmodel.on_button_click(char)