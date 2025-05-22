import tkinter as tk
from tkinter import messagebox
from facade import CalculatorFacade
from PIL import Image, ImageTk


class Calculators:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор Жоров Макаров Сотвалдиев 1123")
        self.root.geometry("400x600")
        self.root.minsize(300, 500)
        self.root.configure(bg="#f0f0f0")
        self.root.iconbitmap("resources/icons/calculator_icon.ico")

        self.create_menu()

        # Initialize facade
        self.facade = CalculatorFacade(root)
        self.facade.viewmodel.update_display_callback = self.update_display

    def update_display(self, text):
        self.facade.update_display(text)

    def create_menu(self):
        menubar = tk.Menu(self.root)
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="Об авторе", command=self.show_about)
        menubar.add_cascade(label="Справка", menu=help_menu)
        self.root.config(menu=menubar)

    def show_about(self):
        messagebox.showinfo(
            "Об авторе",
            "Разработали студенты группы 10701123:\nМакаров А.С.\nЖоров Е.А.\nСотвалдиев А.С."
        )