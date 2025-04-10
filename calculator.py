import tkinter as tk
from tkinter import font

class Calculator:
    def __init__(self, root, display_component, buttons_component):
        self.root = root
        self.root.title("Калькулятор Жоров Макаров 1123")
        self.root.geometry("400x600")
        self.root.minsize(300, 500)
        self.root.configure(bg="#f0f0f0")

        # Переменная для хранения текущего выражения
        self.expression = ""
        self.input_text = tk.StringVar()

        # Создание интерфейса
        display_component.create_display(self.root, self.input_text)
        buttons_component.create_buttons(self.root, self.on_button_click)

    def on_button_click(self, char):
        if char == "C":
            self.expression = ""
            self.input_text.set("")
        elif char == "=":
            try:
                result = str(eval(self.expression))
                self.input_text.set(result)
                self.expression = result
            except Exception:
                self.input_text.set("Ошибка")
                self.expression = ""
        else:
            self.expression += str(char)
            self.input_text.set(self.expression)
