import tkinter as tk
from factory import CalculatorFactory

if __name__ == "__main__":
    root = tk.Tk()
    factory = CalculatorFactory()
    calculator = factory.create_calculator(root)
    root.mainloop()
