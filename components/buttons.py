import os
import sys
import tkinter as tk
from tkinter import font
from config import FontConfig, ButtonConfig, BUTTON_LAYOUT, AppConfig, ThemeConfig
from .sound import SoundPlayer

if sys.platform == "win32":
    import ctypes

    def load_custom_font(font_path):
        full_path = os.path.abspath(font_path)
        ctypes.windll.gdi32.AddFontResourceExW(full_path, 0x10, 0)


class ButtonsComponent:
    def __init__(self, command):
        self.command = command
        self.sound_player = SoundPlayer()

    def create_buttons(self, root):
        buttons_frame = tk.Frame(root, bg=ThemeConfig.BACKGROUND)
        buttons_frame.pack(expand=True, fill="both", padx=10, pady=10)

        load_custom_font(FontConfig.FONT_PATH)

        try:
            button_font = font.Font(family=FontConfig.FONT_NAME, size=FontConfig.BUTTON_SIZE)
        except tk.TclError:
            print("⚠️ Не удалось загрузить SF Pro Text. Используется стандартный шрифт.")
            button_font = font.Font(size=FontConfig.BUTTON_SIZE)

        for button in BUTTON_LAYOUT:
            if len(button) == 5:
                text, row, col, rowspan, colspan = button
                btn = tk.Button(
                    buttons_frame,
                    text=text,
                    font=button_font,
                    bg=ButtonConfig.BACKGROUND,
                    fg=ButtonConfig.FOREGROUND,
                    bd=ButtonConfig.BORDER_WIDTH,
                    command=lambda t=text: self._on_button_click(t)
                )
                btn.grid(row=row, column=col, rowspan=rowspan, columnspan=colspan,
                         sticky="nsew", padx=ButtonConfig.PADDING_X, pady=ButtonConfig.PADDING_Y)
            else:
                text, row, col = button
                btn = tk.Button(
                    buttons_frame,
                    text=text,
                    font=button_font,
                    bg=ButtonConfig.BACKGROUND,
                    fg=ButtonConfig.FOREGROUND,
                    bd=ButtonConfig.BORDER_WIDTH,
                    command=lambda t=text: self._on_button_click(t)
                )
                btn.grid(row=row, column=col, sticky="nsew",
                         padx=ButtonConfig.PADDING_X, pady=ButtonConfig.PADDING_Y)

        for i in range(6):
            buttons_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            buttons_frame.grid_columnconfigure(i, weight=1)

    def _on_button_click(self, button_text):
        self.sound_player.play_click()
        self.command.execute(button_text)