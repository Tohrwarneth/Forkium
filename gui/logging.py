import tkinter as tk
from tkinter import ttk, filedialog
import resources.style as style
import logic.logging as log


class LoggingFrame(tk.Frame):
    """
    Frame for displaying and saving log messages.
    """

    log_label: tk.Label
    log_text: tk.Text
    scrollbar_v: tk.Scrollbar
    scrollbar_h: tk.Scrollbar
    save_button: tk.Button

    __translations: dict

    def __init__(self, root: tk.Frame | tk.Tk, translations: dict, row: int = 1, column: int = 0, columnspan: int = 2,
                 padx: int = 20, pady: int = 20):
        """
        Initialize the LoggingFrame.

        Args:
            root (Frame | Tk): Frame parent. A Tkinter frame or the root Tkinter window.
            translations (dict): A dictionary of translations for UI text.
            row (int): The row position of the frame in the grid.
            column (int): The column position of the frame in the grid.
            columnspan (int): The number of columns the frame spans in the grid.
            padx (int): The horizontal padding around the frame.
            pady (int): The vertical padding around the frame.
        """
        super().__init__(root)
        self.grid(row=row, column=column, columnspan=columnspan, sticky=tk.NSEW, padx=padx, pady=pady)

        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)

        self.__translations = translations

        # log label
        self.log_label = tk.Label(self, font=style.default_font, text=translations["log.title"])
        self.log_label.grid(row=0, column=0, sticky=tk.W)

        # log text area
        self.log_text = tk.Text(self, wrap=tk.NONE, state=tk.DISABLED)
        self.log_text.grid(row=1, column=0, sticky=tk.NSEW)

        # Vertical and horizontal scrollbars for the log text area
        self.scrollbar_v = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.log_text.yview)
        self.scrollbar_v.grid(row=1, column=1, sticky=tk.NS)

        self.scrollbar_h = ttk.Scrollbar(self, orient=tk.HORIZONTAL, command=self.log_text.xview)
        self.scrollbar_h.grid(row=2, column=0, sticky=tk.EW)
        self.log_text.config(yscrollcommand=self.scrollbar_v.set, xscrollcommand=self.scrollbar_h.set)

        # Save log button
        self.save_button = tk.Button(self, font=style.button_font, fg=style.button_fg, bg=style.button_bg,
                                     text=translations["log.save"], command=self.save_log)
        self.save_button.grid(row=0, column=0, sticky=tk.E, ipadx=style.button_x_padding,
                              ipady=style.button_y_padding)

        # Add a log listener to update the log frame
        log.add_log_listener(self.update_log_frame)

    def update_log_frame(self, event: str):
        """
        Update the log text area with a new log event.

        Args:
            event (str): The log event to be added to the log text area.
        """
        self.log_text.config(state=tk.NORMAL)
        self.log_text.insert(tk.END, f"{event}\n")
        self.log_text.config(state=tk.DISABLED)
        self.log_text.see(tk.END)

    def save_log(self):
        """
        Save the log messages to a text file.

        Opens a file dialog to select the location for saving the log file.
        """
        log.log_event("Saving logs to a text file")

        title = self.__translations["log.save.title"]
        filetypes = [(self.__translations["log.save.file"], "*.txt")]
        file_path = filedialog.asksaveasfilename(title=title, filetypes=filetypes)

        if file_path:
            # If a file is selected
            if not file_path.endswith(".txt"):
                # If the file name has no extension called txt
                file_path += ".txt"
            log.log_event(f"Save as {file_path}")
            log.save_log(save_path=file_path)
        else:
            # If the selection was canceled
            log.log_event(f"Saving canceled")
