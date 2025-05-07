import tkinter as tk
from tkinter import font


class ButtonsComponent:
    def __init__(self, command):
        self.command = command

    def create_buttons(self, root):
        buttons_frame = tk.Frame(root, bg="#f0f0f0")
        buttons_frame.pack(expand=True, fill="both", padx=10, pady=10)

        # Обновленный массив кнопок с тригонометрическими функциями
        buttons = [
            ("sin", 0, 0), ("cos", 0, 1), ("tan", 0, 2), ("C", 0, 3),
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), ("(", 4, 1), (")", 4, 2), ("+", 4, 3),
            ("=", 5, 0, 1, 4)  # Большая кнопка "=" на всю ширину
        ]

        button_font = font.Font(size=14)  # Уменьшили шрифт для большего количества кнопок

        for button in buttons:
            if len(button) == 5:  # Для кнопки "=" с особыми параметрами
                text, row, col, rowspan, colspan = button
                btn = tk.Button(
                    buttons_frame,
                    text=text,
                    font=button_font,
                    bg="#e0e0e0",
                    fg="#000000",
                    bd=0,
                    command=lambda t=text: self.command.execute(t)
                )
                btn.grid(row=row, column=col, rowspan=rowspan, columnspan=colspan,
                         sticky="nsew", padx=5, pady=5)
            else:
                text, row, col = button
                btn = tk.Button(
                    buttons_frame,
                    text=text,
                    font=button_font,
                    bg="#e0e0e0",
                    fg="#000000",
                    bd=0,
                    command=lambda t=text: self.command.execute(t)
                )
                btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

        # Настройка веса строк и столбцов
        for i in range(6):  # Теперь у нас 6 строк
            buttons_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            buttons_frame.grid_columnconfigure(i, weight=1)