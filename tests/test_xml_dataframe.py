import unittest
import numpy as np
from logic.xml_dataframe import XMLParser
import os


class TestXMLParser(unittest.TestCase):
    """
    Test suite for the XMLParser class.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up the test environment.
        """
        #  Create XML file with equal child notes
        cls.xml_data = """<?xml version="1.0"?>
        <root>
            <item>
                <name>Item1</name>
                <value>10</value>
            </item>
            <item>
                <name>Item2</name>
                <value>20</value>
            </item>
        </root>"""
        cls.xml_file_even = 'even_test.xml'
        with open(cls.xml_file_even, 'w') as file:
            file.write(cls.xml_data)

        #  Create XML file with a different number of child notes
        cls.xml_data = """<?xml version="1.0"?>
        <root>
            <item>
                <name>Item1</name>
                <value>10</value>
                <properties>
                    <state>NEW</state>
                </properties>
            </item>
            <item>
                <name>Item2</name>
                <value>20</value>
            </item>
        </root>"""
        cls.xml_file_uneven = 'uneven_test.xml'
        with open(cls.xml_file_uneven, 'w') as file:
            file.write(cls.xml_data)

        #  Create XML file no content
        cls.xml_data = str()
        cls.xml_file_empty = 'empty_test.xml'
        with open(cls.xml_file_empty, 'w') as file:
            file.write(cls.xml_data)

        #  Create XML with a syntax error
        cls.xml_data = "Syntax Error"
        cls.xml_file_syntax = 'syntax_test.xml'
        with open(cls.xml_file_syntax, 'w') as file:
            file.write(cls.xml_data)

        #  Create a working non XML file
        cls.xml_data = """<?xml version="1.0"?>
        <root>
            <item>
                <name>Item1</name>
                <value>10</value>
            </item>
            <item>
                <name>Item2</name>
                <value>20</value>
            </item>
        </root>"""
        cls.non_xml_file = 'non_xml_test.txt'
        with open(cls.non_xml_file, 'w') as file:
            file.write(cls.xml_data)

    @classmethod
    def tearDownClass(cls):
        """
        Clean up the test environment.
        """
        if os.path.exists(cls.xml_file_even):
            os.remove(cls.xml_file_even)

        if os.path.exists(cls.xml_file_uneven):
            os.remove(cls.xml_file_uneven)

        if os.path.exists(cls.xml_file_empty):
            os.remove(cls.xml_file_empty)

        if os.path.exists(cls.xml_file_syntax):
            os.remove(cls.xml_file_syntax)

        if os.path.exists(cls.non_xml_file):
            os.remove(cls.non_xml_file)

    def test_parse_xml_even(self):
        """
        Test parsing an XML file with even structure.
        """
        XMLParser.parse_xml_to_dataframe(self.xml_file_even)
        dataframe = XMLParser.dataframe

        expected_columns = ['name', 'value']
        expected_data = {'name': ['Item1', 'Item2'], 'value': ['10', '20']}

        self.assertEqual(expected_columns, list(dataframe.columns))
        self.assertEqual(expected_data, dataframe.to_dict(orient='list'))

    def test_parse_xml_uneven(self):
        """
        Test parsing an XML file with uneven structure.
        """
        XMLParser.parse_xml_to_dataframe(self.xml_file_uneven)
        dataframe = XMLParser.dataframe

        expected_columns = ['name', 'value', 'state']
        expected_data = {'name': ['Item1', 'Item2'], 'value': ['10', '20'], 'state': ['NEW', np.nan]}

        self.assertEqual(expected_columns, list(dataframe.columns))
        self.assertEqual(expected_data, dataframe.to_dict(orient='list'))

    def test_parse_xml_empty(self):
        """
        Test parsing an empty XML file.
        """
        XMLParser.parse_xml_to_dataframe(self.xml_file_empty)
        dataframe = XMLParser.dataframe

        expected_columns = list()
        expected_data = dict()

        self.assertEqual(expected_columns, list(dataframe.columns))
        self.assertEqual(expected_data, dataframe.to_dict(orient='list'))

    def test_parse_xml_syntax_error(self):
        """
        Test parsing an XML file with syntax error.
        """
        XMLParser.parse_xml_to_dataframe(self.xml_file_syntax)
        dataframe = XMLParser.dataframe
        self.assertIsNone(dataframe)

    def test_parse_non_xml_file(self):
        """
        Test parsing a non XML file with even structure.
        """
        XMLParser.parse_xml_to_dataframe(self.non_xml_file)
        dataframe = XMLParser.dataframe

        expected_columns = ['name', 'value']
        expected_data = {'name': ['Item1', 'Item2'], 'value': ['10', '20']}

        self.assertEqual(expected_columns, list(dataframe.columns))
        self.assertEqual(expected_data, dataframe.to_dict(orient='list'))


if __name__ == '__main__':
    unittest.main()
