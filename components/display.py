import os
import sys
import tkinter as tk
from tkinter import font
from config import FontConfig, DisplayConfig, AppConfig, ThemeConfig

if sys.platform == "win32":
    import ctypes

    def load_custom_font(font_path):
        full_path = os.path.abspath(font_path)
        ctypes.windll.gdi32.AddFontResourceExW(full_path, 0x10, 0)


class DisplayComponent:
    def __init__(self, input_text):
        self.input_text = input_text

    def create_display(self, root):
        from config import ThemeConfig

        display_frame = tk.Frame(root, bg=ThemeConfig.BACKGROUND)

        display_frame.pack(expand=True, fill="both", padx=10, pady=10)

        # Загружаем шрифт
        load_custom_font(FontConfig.FONT_PATH)

        try:
            display_font = font.Font(family=FontConfig.FONT_NAME, size=FontConfig.DISPLAY_SIZE)
        except tk.TclError:
            display_font = font.Font(size=FontConfig.DISPLAY_SIZE)

        display = tk.Entry(
            display_frame,
            textvariable=self.input_text,
            font=display_font,
            justify=DisplayConfig.JUSTIFY,
            bd=DisplayConfig.BORDER_WIDTH,
            bg=DisplayConfig.BACKGROUND,
            fg=DisplayConfig.FOREGROUND,
            insertwidth=0,
        )
        display.pack(expand=True, fill="both", ipady=10)