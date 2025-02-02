import unittest
import os
import logic.logging as log


class TestLogging(unittest.TestCase):
    """
    Test suite for the logging system.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up the test environment.
        """
        cls.log_file = "log.txt"

    def setUp(self):
        """
        Reset the log entries before each test.
        """
        log.log_entries = list()
        log.error_entries = list()

    def tearDown(self):
        """
        Clean up the log files after each test in case a test is failing.
        """
        if os.path.exists(self.log_file):
            os.remove(self.log_file)

    def test_log_event(self):
        """
        Test logging a single event.
        """
        log.log_event("Test Event")
        self.assertIn("Test Event", log.log_entries[-1])

    def test_log_multiple_events(self):
        """
        Test logging multiple events.
        """
        for i in range(0, 5):
            log.log_event(f"Event {i}")
            self.assertIn(f"Event {i}", log.log_entries[-1])

    def test_log_error(self):
        """
        Test logging a single error.
        """
        log.log_error("Test Error")
        self.assertIn("Test Error", log.log_entries[-1])
        self.assertIn("Test Error", log.error_entries[-1])

    def test_log_multiple_errors(self):
        """
        Test logging multiple errors.
        """
        for i in range(0, 5):
            log.log_error(f"Error {i}")
            self.assertIn(f"Error {i}", log.log_entries[-1])
            self.assertIn(f"Error {i}", log.error_entries[-1])

    def test_get_latest_error(self):
        """
        Test get latest error.
        """
        for i in range(0, 5):
            log.log_error(f"Error {i}")

        self.assertEqual(f"Error 4", log.get_latest_error())

    def test_get_latest_error_empty(self):
        """
        Test get latest error while none was logged.
        """

        self.assertEqual("", log.get_latest_error())

    def test_log_listener(self):
        """
        Test adding a log listener and check the observed entries.
        """
        listened_entries = list()
        log.add_log_listener(lambda entry: listened_entries.append(entry))

        for i in range(0, 5):
            log.log_event(f"Event {i}")

        self.assertEqual(log.log_entries, listened_entries)

    def test_save_filled_log(self):
        """
        Test saving a log file with multiple log entries.
        """
        for i in range(0, 5):
            log.log_event(f"Event {i}")

        log.save_log(self.log_file)
        self.assertTrue(os.path.exists(self.log_file))

        with open(self.log_file, 'r') as file:
            saved_logs = file.read().strip().split("\n")

        self.assertEqual(log.log_entries[:-1], saved_logs)

    def test_save_empty_log(self):
        """
        Test saving an empty log file.
        """
        log.save_log(self.log_file)
        self.assertTrue(os.path.exists(self.log_file))

        with open(self.log_file, 'r') as file:
            saved_logs = file.read().strip().split("\n")

        self.assertEqual([''], saved_logs)


if __name__ == '__main__':
    unittest.main()
