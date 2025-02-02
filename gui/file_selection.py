import errno
import tkinter as tk
from tkinter import filedialog
import openpyxl
import pandas as pd
from logic.xml_dataframe import XMLParser

import resources.style as style
import logic.logging as log
import os


class FileSelectionFrame(tk.Frame):
    """
    Frame for file selection and export operations.
    """

    xml_file_button: tk.Button
    xml_file_label: tk.Label
    output_file_button: tk.Button
    output_file_label: tk.Label
    output_prettier_checkbox: tk.Checkbutton

    __check_vars: dict | None
    __xml_path: str
    __output_path: str
    __translations: dict
    __use_output_prettier: tk.BooleanVar

    def __init__(self, root: tk.Frame | tk.Tk, translations: dict, row: int = 1, column: int = 0, padx: int = 20,
                 pady: int = 20):
        """
        Initialize the FileSelectionFrame.

        Args:
            root (Frame | Tk): Frame parent. A Tkinter frame or the root Tkinter window.
            translations (dict): A dictionary of translations for UI text.
            row (int): The row position of the frame in the grid.
            column (int): The column position of the frame in the grid.
            padx (int): The horizontal padding around the frame.
            pady (int): The vertical padding around the frame.
        """
        super().__init__(root)
        self.__check_vars = None
        self.__xml_path = ""
        self.__output_path = ""
        self.__translations = translations
        row_padding = 20
        column_padding = 30

        self.grid(row=row, column=column, sticky=tk.EW, padx=padx, pady=pady)

        # File Input
        self.xml_file_button: tk.Button = tk.Button(self, font=style.button_font, fg=style.button_fg,
                                                    bg=style.button_bg,
                                                    text=translations["file.select.button"],
                                                    command=self.select_xml_file)
        self.xml_file_button.grid(row=0, column=0, sticky=tk.EW, ipadx=style.button_x_padding,
                                  ipady=style.button_y_padding,
                                  pady=(0, row_padding))

        self.xml_file_label = tk.Label(self, font=style.hint_font, text=translations["file.select.none"])
        self.xml_file_label.grid(row=0, column=1, sticky=tk.NW, ipady=style.button_y_padding, padx=column_padding)

        # File Output
        self.output_file_button = tk.Button(self, font=style.button_font, fg=style.button_fg,
                                            bg=style.button_bg,
                                            state=tk.DISABLED, text=translations["file.output.button"],
                                            command=self.select_output_file)
        self.output_file_button.grid(row=1, column=0, sticky=tk.EW, ipadx=style.button_x_padding,
                                     ipady=style.button_y_padding)

        self.__use_output_prettier = tk.BooleanVar(value=True)
        self.output_prettier_checkbox = tk.Checkbutton(self, text=translations["file.output.prettier"],
                                                       variable=self.__use_output_prettier)
        self.output_prettier_checkbox.grid(row=2, column=0, sticky=tk.W)
        self.__use_output_prettier.trace_add("write", lambda *args, var=self.__use_output_prettier: log.log_event(
            f"{'Select' if var.get() else 'Deselect'} export prettier"))

        self.output_file_label = tk.Label(self, font=style.hint_font, text=translations["file.output.none"])
        self.output_file_label.grid(row=1, column=1, sticky=tk.NW, ipady=style.button_y_padding, padx=column_padding)

    def select_xml_file(self):
        """
        Open a file dialog to select an input XML file.
        Parse the selected XML file and update the UI accordingly.
        """
        log.log_event("Selecting an input XML file")

        filetypes: list = [(self.__translations["file.select.xml"], "*.xml")]
        title: str = self.__translations["file.select.title"]
        self.__xml_path = filedialog.askopenfilename(filetypes=filetypes, title=title)

        if self.__xml_path:
            # An XML file was selected
            self.xml_file_label.config(text=str.format(self.__translations["file.select.success"], self.__xml_path),
                                       font=style.default_font)
            log.log_event(f"{self.__xml_path} selected")
            XMLParser.parse_xml_to_dataframe(self.__xml_path)

            if XMLParser.dataframe is None:
                # If a parse exception other than an empty file was thrown
                self.output_file_button.config(state=tk.DISABLED)
                if log.get_latest_error().__contains__("syntax"):
                    self.xml_file_label.config(
                        text=str.format(self.__translations["file.select.error.syntax"], self.__xml_path),
                        font=style.error_font)
                else:
                    self.xml_file_label.config(
                        text=str.format(self.__translations["file.select.error"], self.__xml_path),
                        font=style.error_font)
            else:
                # XML data can now be exported
                self.output_file_button.config(state=tk.NORMAL)
        else:
            # No file was selected
            self.xml_file_label.config(text=self.__translations["file.select.none"], font=style.hint_font)
            self.output_file_button.config(state=tk.DISABLED)
            XMLParser.set_dataframe_none()
            log.log_event("Selection canceled")

    def select_output_file(self):
        """
        Open a file dialog to select an output XLSX file.
        Save the parsed XML data to the selected XLSX file.
        """
        log.log_event("Selecting an output XLSX file")
        filetypes = [(self.__translations["file.output.xlsx"], "*.xlsx")]
        title = self.__translations["file.output.title"]
        self.__output_path = filedialog.asksaveasfilename(filetypes=filetypes, title=title, confirmoverwrite=False)
        if self.__output_path:
            # An output path was selected
            if not self.__output_path.endswith(".xlsx"):
                # If the file name has no extension called xlsx
                self.__output_path += ".xlsx"

            self.output_file_label.config(text=str.format(self.__translations["file.output.success"],
                                                          self.__output_path), font=style.default_font)
            log.log_event(f"{self.__output_path} selected")
            self.__save_output_file()
        else:
            # No file was selected
            self.output_file_label.config(text=self.__translations["file.output.none"], font=style.hint_font)
            log.log_event("Selection canceled")

    def __save_output_file(self):
        """
        Save the parsed XML data to the selected XLSX file.
        Optionally apply prettier for better readability.
        """
        log.log_event("Exporting XML data to XLSX file")

        if not self.__check_vars:
            # If check_vars is not set externally
            selected_dataframe: pd.DataFrame = XMLParser.dataframe
        else:
            # If check_vars is set externally
            selected_columns = [col for col, var in self.__check_vars.items() if var.get()]
            selected_dataframe = XMLParser.dataframe[selected_columns]

        log.log_event(f"Exporting {len(selected_dataframe.columns)} columns and {len(selected_dataframe)} rows")
        sheet_name = os.path.splitext(os.path.basename(self.__xml_path))[0]

        if os.path.exists(self.__output_path):
            # If the Excel file already exists
            log.log_event("Add a new sheet to an existing workbook")
            try:
                with pd.ExcelWriter(self.__output_path, engine="openpyxl", mode="a") as writer:
                    workbook = writer.book
                    i = 1
                    base_sheet_name = sheet_name
                    while sheet_name in workbook.sheetnames:
                        # Find the next unused index if sheet name already exists
                        sheet_name = f"{base_sheet_name}_{i}"
                        i += 1
                    selected_dataframe.to_excel(writer, index=False, sheet_name=sheet_name)
            except IOError as e:
                if e.errno == errno.EACCES:
                    # An access error is thrown
                    log.log_error(
                        f"Error while opening the file '{self.__output_path}'. The file is opened by another app and cannot be edited")
                    self.output_file_label.config(
                        text=str.format(self.__translations["file.output.error.open"], self.__output_path),
                        font=style.error_font)
                else:
                    # Another IO error is thrown
                    log.log_error(f"Error while saving the file '{self.__output_path}': {e}")
                    self.output_file_label.config(
                        text=str.format(self.__translations["file.output.error.io"], self.__output_path),
                        font=style.error_font)
                return
        else:
            log.log_event("Create a new workbook")
            try:
                selected_dataframe.to_excel(self.__output_path, index=False, sheet_name=sheet_name)
            except IOError as e:
                # Another IO error is thrown
                log.log_error(f"Error while saving the file '{self.__output_path}': {e}")
                self.output_file_label.config(
                    text=str.format(self.__translations["file.output.error.io"], self.__output_path),
                    font=style.error_font)
                return

        if self.__use_output_prettier:
            # If the Excel sheet should be edited to look nicer
            # Currently only autosize of the columns
            wb = openpyxl.load_workbook(self.__output_path)
            sheet = wb[sheet_name]
            for col in sheet.columns:
                sheet.column_dimensions[col[0].column_letter].auto_size = True
            wb.save(self.__output_path)

        log.log_event(f"XML data exported to {self.__output_path}")

    def set_selected_columns_variables(self, check_vars: dict):
        """
        Set the variables of the selected columns for export based on the provided check variables.

        Args:
            check_vars (dict): A dictionary where keys are column names and values are BooleanVar objects indicating whether the column is selected.
        """
        self.__check_vars = check_vars
