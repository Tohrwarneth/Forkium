import tkinter as tk
import resources.style as style
import logic.logging as log
from logic.xml_dataframe import XMLParser
import pandas as pd

class PreviewFrame(tk.Frame):
    """
    Frame for previewing and selecting columns from the parsed XML data.
    """

    check_vars: dict
    preview_label: tk.Label
    check_frame: tk.Frame

    def __init__(self, root: tk.Frame | tk.Tk, translations: dict, row: int = 1, column: int = 0, rowspan: int = 3,
                 padx: int = 20, pady: int = 20):
        """
        Initialize the PreviewFrame.

        Args:
            root (Frame | Tk): Frame parent. A Tkinter frame or the root Tkinter window.
            translations (dict): A dictionary of translations for UI text.
            row (int): The row position of the frame in the grid.
            column (int): The column position of the frame in the grid.
            rowspan (int): The number of rows the frame spans in the grid.
            padx (int): The horizontal padding around the frame.
            pady (int): The vertical padding around the frame.
        """
        super().__init__(root)
        self.grid(row=row, column=column, rowspan=rowspan, sticky=tk.NW, padx=padx, pady=pady)

        self.check_vars = dict()

        self.preview_label = tk.Label(self, font=style.default_font, text=translations["preview"])
        self.preview_label.grid(row=0, column=0, sticky=tk.NW)

        # Frame for checkboxes
        self.check_frame = tk.Frame(self, width=100)
        self.check_frame.grid(row=0, column=1, pady=10, sticky=tk.EW)

        # Listen for changes in the XML data
        XMLParser.add_listener(self.update_checkboxes)

    def update_checkboxes(self, dataframe: pd.DataFrame):
        """
        Update the checkboxes based on the columns of the provided dataframe.

        Args:
            dataframe (pd.DataFrame): The dataframe containing the parsed XML data.
        """
        for widget in self.check_frame.winfo_children():
            widget.destroy()
        self.check_vars.clear()

        if dataframe is not None:
            # If the construction of the dataframe was successful
            for col in dataframe.columns:
                var = tk.BooleanVar(value=True)
                # Logs changes to the check state
                var.trace_add("write", lambda *args, col=col, var=var: log.log_event(
                    f"Column '{col}' {'selected' if var.get() else 'unselected'}"))
                chk = tk.Checkbutton(self.check_frame, text=col, variable=var)
                chk.pack(anchor="w")
                self.check_vars[col] = var
