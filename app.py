import tkinter as tk
from view import Calculators
from config import validate_resources


if __name__ == "__main__":
    try:
        validate_resources()
        root = tk.Tk()
        app = Calculators(root)
        root.mainloop()
    except FileNotFoundError as e:
        print(f"Ошибка запуска: {e}")
        input("Нажмите Enter для выхода...")