import tkinter as tk
from tkinter import messagebox
from config import AppConfig, IconConfig, ThemeConfig
from facade import CalculatorFacade

class Calculators:
    def __init__(self, root):
        self.root = root
        self.root.title(AppConfig.TITLE)
        self.root.geometry(AppConfig.GEOMETRY)
        self.root.minsize(AppConfig.MIN_WIDTH, AppConfig.MIN_HEIGHT)
        self.root.configure(bg=ThemeConfig.BACKGROUND)
        self.root.iconbitmap(IconConfig.ICON_PATH)

        self.create_menu()
        self.facade = CalculatorFacade(root)
        self.facade.viewmodel.update_display_callback = self.update_display

        self.create_theme_toggle()

    def update_display(self, text):
        self.facade.update_display(text)

    def create_menu(self):
        menubar = tk.Menu(self.root)
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="Об авторе", command=self.show_about)
        menubar.add_cascade(label="Справка", menu=help_menu)
        self.root.config(menu=menubar)

    def show_about(self):
        messagebox.showinfo("Об авторе", AppConfig.ABOUT_INFO)

    def create_theme_toggle(self):
        self.theme_button = tk.Button(
            self.root, text="Черный фон", command=self.toggle_theme,
            bg=ThemeConfig.THEMES[ThemeConfig.MODE]["BUTTON_BG"],
            fg=ThemeConfig.THEMES[ThemeConfig.MODE]["FOREGROUND"]
        )
        self.theme_button.pack(pady=10)

    def toggle_theme(self):
        new_mode = "dark" if ThemeConfig.MODE == "light" else "light"
        ThemeConfig.update_theme(new_mode)

        self.root.configure(bg=ThemeConfig.BACKGROUND)
        self.theme_button.config(bg=ThemeConfig.BUTTON_BG, fg=ThemeConfig.FOREGROUND)
