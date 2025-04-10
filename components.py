import tkinter as tk
from tkinter import font

class DisplayComponent:
    def create_display(self, root, input_text):
        display_frame = tk.Frame(root, bg="#f0f0f0")
        display_frame.pack(expand=True, fill="both", padx=10, pady=10)

        display_font = font.Font(size=24)
        display = tk.Entry(
            display_frame,
            textvariable=input_text,
            font=display_font,
            justify="right",
            bd=0,
            bg="#ffffff",
            fg="#000000",
            insertwidth=0,
        )
        display.pack(expand=True, fill="both", ipady=10)

class ButtonsComponent:
    def create_buttons(self, root, button_click_callback):
        buttons_frame = tk.Frame(root, bg="#f0f0f0")
        buttons_frame.pack(expand=True, fill="both", padx=10, pady=10)

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
                command=lambda t=text: button_click_callback(t),
            )
            button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

        for i in range(4):
            buttons_frame.grid_rowconfigure(i, weight=1)
            buttons_frame.grid_columnconfigure(i, weight=1)
