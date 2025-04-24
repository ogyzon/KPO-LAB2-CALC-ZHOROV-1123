import tkinter as tk
from viewmodel import CalculatorViewModel
from model import CalculatorModel
from components import DisplayComponent, ButtonsComponent

class Calculators:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор MVVM Жоров Макаров 1123")
        self.root.geometry("400x600")
        self.root.minsize(300, 500)
        self.root.configure(bg="#f0f0f0")
        
        # Initialize MVVM components
        self.model = CalculatorModel()
        self.viewmodel = CalculatorViewModel(self.model)
        self.viewmodel.update_display_callback = self.update_display
        
        # UI Components
        self.input_text = tk.StringVar()
        self.display_component = DisplayComponent(self.input_text)
        self.buttons_component = ButtonsComponent(self.viewmodel.on_button_click)
        
        # Create UI
        self.display_component.create_display(root)
        self.buttons_component.create_buttons(root)
    
    def update_display(self, text):
        self.input_text.set(text)