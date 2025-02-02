# Forkium XML-Parser

## Installation Guide

### Prerequisites

Before you begin, ensure you have Python 3.11 or higher installed on your machine. You can download Python from the
following link:

- [Download Python](https://www.python.org/downloads/)

Make sure to download and install the latest version of Python for your operating system.

### Installation Steps

Follow these steps to install and run the project:

1. **Check Python Version**

   First, check if you have Python 3.11 or higher installed on your machine. Open a terminal or command prompt and run
   the following command:

   ```bash
   python --version
   ```

   The output should be `Python 3.11.x` or higher. If you see a lower version or get an error, download and install
   Python 3.11 or higher from the link above.

2. **Clone the Repository**

   Clone the repository to your local machine using `git` or download the project as a ZIP file and extract it.

   ```bash
   git clone https://github.com/Tohrwarneth/Forkium.git
   cd Forkium
   ```

3. **Create a Virtual Environment**

   Create a virtual environment to manage the dependencies. Use the following command:

   ```bash
   python -m venv venv
   ```

   Activate the virtual environment:

    - On Windows:

      ```bash
      .\venv\Scripts\activate
      ```

    - On macOS and Linux:

      ```bash
      source venv/bin/activate
      ```

4. **Install the Dependencies**

   Install the required dependencies using `pip` and the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Project**

   Now you can run the project:
   ```bash
   python main.py
   ```

### Additional Information

If you need any further assistance or encounter any issues, feel free to reach out to me.

## Test Documentation

The testing was split between automated Unit Tests and manually GUI and System Tests.

### Automated Unit Tests

The logic part of the application was tested by pythons unittest package.
You can find them in the `tests` folder.

1. **Activate the Virtual Environment**

   To run the unit tests activate the Virtual Environment:

    - On Windows:

        ```bash
        .\venv\Scripts\activate
        ```

    - On macOS and Linux:

      ```bash
      source venv/bin/activate
      ```
2. **Run the Unit Tests**

   Execute following command to run all test files within the tests folder:
   ```bash
   python -m unittest discover -s tests
   ```

### Manually GUI and System Tests

The GUI and Integration Tests are done manually. Here fore test cases was written to run through a checklist of steps
and expected outcome. In fact most of the GUI tests also covered the system tests.

#### Test Cases

##### Successfully parsing with full even XML file

Parsing XML data with even amount of child nodes and every column to a new Excel file

| Step                 | Description                                                                                    | Expected Result                                                                                                                                                                                                                                          |
|----------------------|------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Select XML File      | Click the Button 'Select File'. Select an XML file with an even amount of child nodes.         | A Message should appear next to the button stating the XML file is loaded. Logs showing next to other statements the number of columns and rows. Column Preview updated and displays the columns of the xml file all selected.                           |
| Export As Excel File | Click the Button 'Export as Excel Table'. Type the name of the file in the dialog and confirm. | A Message should appear next to the button stating the XML file is successfully exported. Logs showing next to other statements the number of exported columns and rows as well as the creation of a new file. The button to export the data is enabled. |
| Check Excel Content  | Open the Excel file.                                                                           | Excel opens the sheet with the name of the exported XML file. Every column and row from the XML file are present. The columns width are adjusted to the content size.                                                                                    |

##### Successfully parsing without prettier

Parsing XML data with even amount of child nodes and every column to a new Excel file without prettier

| Step                 | Description                                                                                    | Expected Result                                                                                                                                                                                                                                          |
|----------------------|------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Select XML File      | Click the Button 'Select File'. Select an XML file with an even amount of child nodes.         | A Message should appear next to the button stating the XML file is loaded. Logs showing next to other statements the number of columns and rows. Column Preview updated and displays the columns of the xml file all selected.                           |
| Deselect prettier    | Click the Checkbox 'Adjust column width to content'.                                           | Checkbox is unchecked.                                                                                                                                                                                                                                   |
| Export As Excel File | Click the Button 'Export as Excel Table'. Type the name of the file in the dialog and confirm. | A Message should appear next to the button stating the XML file is successfully exported. Logs showing next to other statements the number of exported columns and rows as well as the creation of a new file. The button to export the data is enabled. |
| Check Excel Content  | Open the Excel file.                                                                           | Excel opens the sheet with the name of the exported XML file. Every column and row from the XML file are present. The columns width is not adjusted to the content size.                                                                                 |

##### Successfully parsing with full uneven XML file

Parsing XML data with uneven amount of child nodes and every column to a new Excel file

| Step                 | Description                                                                                          | Expected Result                                                                                                                                                                                                                                          |
|----------------------|------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Select XML File      | Click the Button 'Select File'. Select an XML file with an different depth of amount of child nodes. | A Message should appear next to the button stating the XML file is loaded. Logs showing next to other statements the number of columns and rows. Column Preview updated and displays the columns of the xml file all selected.                           |
| Export As Excel File | Click the Button 'Export as Excel Table'. Type the name of the file in the dialog and confirm.       | A Message should appear next to the button stating the XML file is successfully exported. Logs showing next to other statements the number of exported columns and rows as well as the creation of a new file. The button to export the data is enabled. |
| Check Excel Content  | Open the Excel file.                                                                                 | Excel opens the sheet with the name of the exported XML file. Every column and row from the XML file are present. The columns width is adjusted to the content size.                                                                                     |

##### Successfully parsing with not every column

Parsing XML data with child nodes and not every column to a new Excel file

| Step                 | Description                                                                                    | Expected Result                                                                                                                                                                                                                                          |
|----------------------|------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Select XML File      | Click the Button 'Select File'. Select an XML file with child nodes.                           | A Message should appear next to the button stating the XML file is loaded. Logs showing next to other statements the number of columns and rows. Column Preview updated and displays the columns of the xml file all selected.                           |
| Deselect Columns     | Deselect some of the columns in the column preview.                                            | The Checkboxes of the deselected columns are unchecked. Logs stating there deselection.                                                                                                                                                                  |
| Select Column        | Reselect one of the columns in the column preview.                                             | The Checkboxes of the reselected column is checked. Logs stating the selection.                                                                                                                                                                          |
| Export As Excel File | Click the Button 'Export as Excel Table'. Type the name of the file in the dialog and confirm. | A Message should appear next to the button stating the XML file is successfully exported. Logs showing next to other statements the number of exported columns and rows as well as the creation of a new file. The button to export the data is enabled. |
| Check Excel Content  | Open the Excel file.                                                                           | Excel opens the sheet with the name of the exported XML file. Only the selected columns and every row from the XML file are present. The columns width is adjusted to the content size.                                                                  |

##### Successfully parsing with no column

Parsing XML data with child nodes and no column to a new Excel file

| Step                 | Description                                                                                    | Expected Result                                                                                                                                                                                                                                          |
|----------------------|------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Select XML File      | Click the Button 'Select File'. Select an XML file with child nodes.                           | A Message should appear next to the button stating the XML file is loaded. Logs showing next to other statements the number of columns and rows. Column Preview updated and displays the columns of the xml file all selected.                           |
| Deselect Columns     | Deselect all of the columns in the column preview.                                             | The Checkboxes of the deselected columns are unchecked. Logs stating there deselection.                                                                                                                                                                  |
| Export As Excel File | Click the Button 'Export as Excel Table'. Type the name of the file in the dialog and confirm. | A Message should appear next to the button stating the XML file is successfully exported. Logs showing next to other statements the number of exported columns and rows as well as the creation of a new file. The button to export the data is enabled. |
| Check Excel Content  | Open the Excel file.                                                                           | Excel opens the sheet with the name of the exported XML file. The sheet dont contains any data.                                                                                                                                                          |

##### Successfully parsing with empty XML

Parsing XML data with no nodes to a new Excel file

| Step                 | Description                                                                                    | Expected Result                                                                                                                                                                                                                                          |
|----------------------|------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Select XML File      | Click the Button 'Select File'. Select an XML file with no nodes.                              | A Message should appear next to the button stating the XML file is loaded. Logs showing next to other statements the number of columns and rows. Column Preview updated and displays no columns.                                                         |
| Export As Excel File | Click the Button 'Export as Excel Table'. Type the name of the file in the dialog and confirm. | A Message should appear next to the button stating the XML file is successfully exported. Logs showing next to other statements the number of exported columns and rows as well as the creation of a new file. The button to export the data is enabled. |
| Check Excel Content  | Open the Excel file.                                                                           | Excel opens the sheet with the name of the exported XML file. The sheet dont contains any data.                                                                                                                                                          |

##### Successfully parsing to an existing Excel file

Parsing XML data with child nodes to an existing Excel file

| Step                 | Description                                                                                                      | Expected Result                                                                                                                                                                                                                                           |
|----------------------|------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Select XML File      | Click the Button 'Select File'. Select an XML file with child nodes.                                             | A Message should appear next to the button stating the XML file is loaded. Logs showing next to other statements the number of columns and rows. Column Preview updated and displays the columns of the xml file all selected.                            |
| Export As Excel File | Click the Button 'Export as Excel Table'. Type or select the name of an existing file in the dialog and confirm. | A Message should appear next to the button stating the XML file is successfully exported. Logs showing next to other statements the number of exported columns and rows as well as the creation of a new sheet. The button to export the data is enabled. |
| Check Excel Content  | Open the Excel file.                                                                                             | The Excel workbook contains several sheets with the name of the exported XML file followed by an index. The sheet with the highest index contains every column and row from the XML file. The columns width is adjusted to the content size.              |

##### Failing parsing with an XML containing syntax errors

Failing parsing XML data with syntax errors

| Step            | Description                                                            | Expected Result                                                                                                                                                                                                                                                                    |
|-----------------|------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Select XML File | Click the Button 'Select File'. Select an XML file with syntax errors. | A Message should appear next to the button stating the XML file contains syntax errors. Logs showing next to other statements the message of a syntax error and in which line and column it appears. Column Preview displays no columns.The button to export the data is disabled. |

##### Failing parsing with an XML containing syntax errors

Failing exporting XML data to an opened Excel file

| Step                 | Description                                                                                    | Expected Result                                                                                                                                                                                                                          |
|----------------------|------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Select XML File      | Click the Button 'Select File'. Select an XML file with syntax errors.                         | A Message should appear next to the button stating the XML file contains syntax errors. Logs showing next to other statements the message of a syntax error and in which line and column it appears. Column Preview displays no columns. |
| Open Excel File      | Open an existing Excel file.                                                                   | Excel locks the file.                                                                                                                                                                                                                    |
| Export As Excel File | Click the Button 'Export as Excel Table'. Type the name of the file in the dialog and confirm. | A Message should appear next to the button stating the Excel file is open by another app. Logs showing a similar error message.                                                                                                          |

##### Save Logs to new file

Save the generated logs to a new file.

| Step                 | Description                                                                       | Expected Result                                  |
|----------------------|-----------------------------------------------------------------------------------|--------------------------------------------------|
| Generate Log Entries | Generate log entries through using the app.                                       | Log entries are displayed.                       |
| Save Logs            | Open an existing Excel file. Type the name of the file in the dialog and confirm. | Text file is created.                            |
| Check Text File      | Open text file.                                                                   | All log entries are listed in the correct order. |

##### Save Logs to an existing file

Save the generated logs to an existing file.

| Step                 | Description                                                                                      | Expected Result                                                                                |
|----------------------|--------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| Generate Log Entries | Generate log entries through using the app.                                                      | Log entries are displayed.                                                                     |
| Save Logs            | Open an existing Excel file. Type/select the name of an existing file in the dialog and confirm. | An overwrite dialog opens.                                                                     |
| Confirm Overwrite    | Confirm the overwrite dialog.                                                                    | Text file is overwritten.                                                                      |
| Check Text File      | Open text file.                                                                                  | All log entries are listed in the correct order. Only the entries which was previous generated |

##### Don't overwrite an existing log file

Don't overwrite an existing log file.

| Step                 | Description                                                                                      | Expected Result                                         |
|----------------------|--------------------------------------------------------------------------------------------------|---------------------------------------------------------|
| Generate Log Entries | Generate log entries through using the app.                                                      | Log entries are displayed.                              |
| Save Logs            | Open an existing Excel file. Type/select the name of an existing file in the dialog and confirm. | An overwrite dialog opens.                              |
| Confirm Overwrite    | Dismiss the overwrite dialog.                                                                    | Text file is not overwritten.                           |
| Check Text File      | Open text file.                                                                                  | Only the entries of the previous file content is listed |

##### Changing Column Preview

Select different XML files to update the column preview.

| Step                 | Description                                                                                    | Expected Result                                                   |
|----------------------|------------------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| Fill Preview         | Click the Button 'Select File'. Select an XML file with child notes.                           | Column Preview displays the columns of the XML file and selected. |
| Export As Excel File | Click the Button 'Export as Excel Table'. Type the name of the file in the dialog and confirm. | Column Preview is displaying the columns of the XML file          |
| Clear Preview        | Click the Button 'Select File'. Select an XML file with no notes.                              | Column Preview displays no columns.                               |
| Refill Preview       | Click the Button 'Select File'. Select an XML file with child notes.                           | Column Preview displays the columns of the XML file and selected. |
| Clear Preview Again  | Click the Button 'Select File'. Select an XML file with syntax errors.                         | Column Preview displays no columns.                               |
