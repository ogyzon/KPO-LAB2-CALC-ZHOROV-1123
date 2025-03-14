import tkinter as tk
from tkinter import font

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор Жоров Макаров 1123")
        self.root.geometry("400x600")  # Начальный размер окна
        self.root.minsize(300, 500)    # Минимальный размер окна
        self.root.configure(bg="#f0f0f0")

        # Переменная для хранения текущего выражения
        self.expression = ""
        self.input_text = tk.StringVar()

        # Создание основного интерфейса
        self.create_display()
        self.create_buttons()

    def create_display(self):
        # Поле для отображения введенных чисел и результата
        display_frame = tk.Frame(self.root, bg="#f0f0f0")
        display_frame.pack(expand=True, fill="both", padx=10, pady=10)

        display_font = font.Font(size=24)
        display = tk.Entry(
            display_frame,
            textvariable=self.input_text,
            font=display_font,
            justify="right",
            bd=0,
            bg="#ffffff",
            fg="#000000",
            insertwidth=0,
        )
        display.pack(expand=True, fill="both", ipady=10)

    def create_buttons(self):
        # Фрейм для кнопок
        buttons_frame = tk.Frame(self.root, bg="#f0f0f0")
        buttons_frame.pack(expand=True, fill="both", padx=10, pady=10)

        # Кнопки
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), ("C", 4, 1), ("=", 4, 2), ("+", 4, 3),
        ]

        button_font = font.Font(size=18)
        for (text, row, col) in buttons:
            button = tk.Button(
                buttons_frame,
                text=text,
                font=button_font,
                bg="#e0e0e0",
                fg="#000000",
                bd=0,
                command=lambda t=text: self.on_button_click(t),
            )
            button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

        # Настройка адаптивности кнопок
        for i in range(4):
            buttons_frame.grid_rowconfigure(i, weight=1)
            buttons_frame.grid_columnconfigure(i, weight=1)

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

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()