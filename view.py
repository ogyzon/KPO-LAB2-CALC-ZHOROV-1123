import tkinter as tk
from facade import CalculatorFacade


class Calculators:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор MVVM Жоров Макаров 1123")
        self.root.geometry("400x600")
        self.root.minsize(300, 500)
        self.root.configure(bg="#f0f0f0")

        # Initialize facade
        self.facade = CalculatorFacade(root)
        self.facade.viewmodel.update_display_callback = self.update_display

    def update_display(self, text):
        self.facade.update_display(text)