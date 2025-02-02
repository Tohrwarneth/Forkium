import xml.etree.ElementTree as ET
import pandas as pd
import logic.logging as log
from typing import Callable


class XMLParser:
    """
    Parsing XML files and converting them to pandas DataFrame.
    """

    dataframe: pd.DataFrame | None = None
    __listeners: list = list()

    @classmethod
    def parse_xml_to_dataframe(cls, file_path: str):
        """
        Parse an XML file and convert it to a pandas DataFrame.

        Args:
            file_path (str): The path to the XML file to be parsed.
        """
        log.log_event(f"Start parse XML to DataFrame of file: {file_path}")

        try:
            tree: ET.ElementTree = ET.parse(file_path)
            root: ET.Element = tree.getroot()
        except ET.ParseError as e:
            if e.code == 3:
                # If the XML file contains no elements
                root = ET.Element("root")
            else:
                # If another parse error, like a syntax error, was thrown
                log.log_error(f"Error while parsing XML file: {e}")
                cls.dataframe = None
                for listener in cls.__listeners:
                    listener(cls.dataframe)
                return

        columns: list = list()
        rows: list = list()
        for row in root:
            row_data: dict = dict()
            cls.__extract_columns_and_data(row, row_data, columns)
            rows.append(row_data)
        log.log_event(f"{len(columns)} columns and {len(rows)} rows found")

        # Construct the DataFrame
        cls.dataframe = pd.DataFrame(rows, columns=columns)
        log.log_event("Finished parsing XML file to DataFrame")
        for listener in cls.__listeners:
            listener(cls.dataframe)

    @classmethod
    def set_dataframe_none(cls):
        """
        Set the dataframe attribute to None and notify all listeners.
        """
        cls.dataframe = None
        for listener in cls.__listeners:
            listener(cls.dataframe)

    @classmethod
    def __extract_columns_and_data(cls, element: ET.Element, row_data: dict, columns: list):
        """
        Recursively extract columns and data from an XML element.

        Args:
            element (ET.Element): The XML element to extract data from.
            row_data (dict): The dictionary to store the row data.
            columns (list): The list to store the column names.
        """
        for child in element:
            # Iterate as long as a node has children
            if not list(child):
                # Only nodes without child elements will be part of the columns
                col_name: str = child.tag
                if col_name not in columns:
                    columns.append(col_name)
                row_data[col_name] = child.text
            else:
                # If the node contains children, extract them until no child elements are found
                cls.__extract_columns_and_data(child, row_data, columns)

    @classmethod
    def add_listener(cls, listener: Callable):
        """
        Add a listener that will be notified when the dataframe is updated.

        Args:
            listener (Callable): The listener function to be added.
        """
        cls.__listeners.append(listener)
