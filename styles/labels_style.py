from tkinter import ttk


class TextFieldLabel(ttk.Style):
    
    def __init__(self):
        super().__init__()
        self.configure(
            "TextLabel.TLabel",
            font=("Verdana", 12),
            foreground="Black",
            background="#99CCFF"
        )

class SelectFieldLabel(ttk.Style):

    def __init__(self):
        super().__init__()
        self.configure(
            "SelectLabel.TLabel",
            font=("Verdana", 12),
            foreground="Black",
            background="#99CCFF"
        )


class CounterFieldLabel(ttk.Style):

    def __init__(self):
        super().__init__()
        self.configure(
            "CounterLabel.TLabel",
            font=("Verdana", 12),
            foreground="Black",
            background="#99CCFF"
        )


class BigLabel(ttk.Style):

    def __init__(self):
        super().__init__()
        self.configure(
            "BigLabel.TLabel",
            font=("Verdana", 14),
            background="#99CCFF"
        )