import os
import sys
import tkinter as tk
from tkinter import font

if sys.platform == "win32":
    import ctypes

    def load_custom_font(font_path):
        # Абсолютный путь
        full_path = os.path.abspath(font_path)
        # FR_PRIVATE = 0x10 — шрифт только в памяти, не добавляется в системный список
        ctypes.windll.gdi32.AddFontResourceExW(full_path, 0x10, 0)


class ButtonsComponent:
    def __init__(self, command):
        self.command = command

    def create_buttons(self, root):
        buttons_frame = tk.Frame(root, bg="#f0f0f0")
        buttons_frame.pack(expand=True, fill="both", padx=10, pady=10)

        buttons = [
            ("sin", 0, 0), ("cos", 0, 1), ("tan", 0, 2), ("C", 0, 3),
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), ("(", 4, 1), (")", 4, 2), ("+", 4, 3),
            ("=", 5, 0, 1, 4)
        ]

        font_path = "resources/fonts/SFProText-Regular.ttf"
        load_custom_font(font_path)

        # Название семейства — должно точно совпадать с именем в файле
        try:
            button_font = font.Font(family="SF Pro Text", size=14)
        except tk.TclError:
            print("⚠️ Не удалось загрузить SF Pro Text. Используется стандартный шрифт.")
            button_font = font.Font(size=14)

        for button in buttons:
            if len(button) == 5:
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

        for i in range(6):
            buttons_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            buttons_frame.grid_columnconfigure(i, weight=1)
