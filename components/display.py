import os
import sys
import tkinter as tk
from tkinter import font

if sys.platform == "win32":
    import ctypes

    def load_custom_font(font_path):
        full_path = os.path.abspath(font_path)
        ctypes.windll.gdi32.AddFontResourceExW(full_path, 0x10, 0)

class DisplayComponent:
    def __init__(self, input_text):
        self.input_text = input_text

    def create_display(self, root):
        display_frame = tk.Frame(root, bg="#f0f0f0")
        display_frame.pack(expand=True, fill="both", padx=10, pady=10)

        # Загружаем шрифт
        font_path = "resources/fonts/SFProText-Regular.ttf"
        load_custom_font(font_path)

        try:
            display_font = font.Font(family="SF Pro Text", size=24)
        except tk.TclError:
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
