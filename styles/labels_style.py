from tkinter import ttk

"""This module has class that are the styles for the labels."""


class TextFieldLabel(ttk.Style):
    """Class for the style of a label of a text field."""
    
    def __init__(self):
        """Initialize the class."""
        super().__init__()
        self.configure(
            "TextLabel.TLabel",
            font=("Arial", 12),
            foreground="Black",
            background="#99CCFF"
        )


class SelectFieldLabel(ttk.Style):
    """Class for the style of a label of a select field."""

    def __init__(self):
        """Initialize the class."""
        super().__init__()
        self.configure(
            "SelectLabel.TLabel",
            font=("Arial", 12),
            foreground="Black",
            background="#99CCFF"
        )


class CounterFieldLabel(ttk.Style):
    """Class for the style of a label for a gas cylinder counter."""

    def __init__(self):
        """Initialize the class."""
        super().__init__()
        self.configure(
            "CounterLabel.TLabel",
            font=("Arial", 12),
            foreground="Black",
            background="#99CCFF"
        )


class BigLabel(ttk.Style):
    """Class for the style of a large label."""

    def __init__(self):
        """Initialize the class."""
        super().__init__()
        self.configure(
            "BigLabel.TLabel",
            font=("Arial", 14),
            background="#99CCFF"
        )


class WarningMessage(ttk.Style):
    """Class for the style of a label of a warning message."""

    def __init__(self):
        """Initialize the class."""
        super().__init__()
        self.configure(
            "WarningLabel.TLabel",
            font=("Arial", 14),
            foreground="Red",
            background="#99CCFF"
        )
