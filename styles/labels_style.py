from tkinter import ttk


class TestFieldLabel(ttk.Style):
    
    def __init__(self):
        super().__init__()
        self.configure("TextLabel.TLabel", font="Verdana 12", foreground="Black", background="White")


class SelectFieldLabel(ttk.Style):

    def __init__(self):
        super().__init__()
        self.configure("SelectLabel.TLabel", font="Verdana 12", foreground="Black", background="White")


class CounterFieldLabel(ttk.Style):

    def __init__(self):
        super().__init__()
        self.configure("CounterLabel.TLabel", font="Verdana 12", foreground="Black", background="White")


class BigLabel(ttk.Style):

    def __init__(self):
        super().__init__()
        self.configure("BigLabel.TLabel", font="Verdana 14", background="White")
