import tkinter as tk
import locale
from gui.welcome import WelcomeFrame
from gui.file_selection import FileSelectionFrame
from gui.previewframe import PreviewFrame
from gui.logging import LoggingFrame


class MainGUI(tk.Tk):
    """
    The main GUI application class that initializes the various frames for the XML to Excel parser.
    """

    welcome_frame: WelcomeFrame
    file_frame: FileSelectionFrame
    preview_frame: PreviewFrame
    logging_frame: LoggingFrame

    __translations: dict

    def __init__(self):
        """
        Initialize the MainGUI application.

        Sets the title of the window based on the current locale and configures the layout.
        Loads the appropriate language translations and initializes the GUI.
        """
        super().__init__()

        # Determine the current locale
        current_locale = locale.getlocale()
        if current_locale[0].__contains__("de_"):
            # If the current locale is German, use German translations
            import resources.lang.de as lang
        else:
            # Otherwise, use English translations
            import resources.lang.en as lang

        self.__translations = lang.translations

        # Set the window title
        self.title(self.__translations["title"])

        # Configure the layout of the main window
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

        self.welcome_frame = WelcomeFrame(self, self.__translations, row=0, column=0, columnspan=2, padx=10, pady=10)
        self.file_frame = FileSelectionFrame(self, self.__translations, row=1, column=0, padx=20, pady=20)
        self.preview_frame = PreviewFrame(self, self.__translations, row=1, column=1, rowspan=2, padx=20, pady=20)
        self.file_frame.set_selected_columns_variables(self.preview_frame.check_vars)
        self.logging_frame = LoggingFrame(self, self.__translations, row=2, column=0, columnspan=1, padx=20, pady=20)
