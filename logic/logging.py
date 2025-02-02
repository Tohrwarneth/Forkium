from datetime import datetime
from typing import Callable

# List of log entries
log_entries: list = list()
# List of error entries
error_entries: list = list()
# List of log listeners (callback functions)
log_listeners: list = list()


def log_event(event: str):
    """
    Log an event with a timestamp and notify all registered listeners.

    Args:
        event (str): The event message to be logged.
    """
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    log_entry = f"{timestamp} {event}"
    log_entries.append(log_entry)
    for listener in log_listeners:
        listener(log_entry)


def log_error(event: str):
    """
    Log an error event and add it to the error entries.

    Args:
        event (str): The error message to be logged.
    """
    log_event(event)
    error_entries.append(event)


def save_log(save_path: str):
    """
    Save the log entries to a specified file and log the save event.

    Args:
        save_path (str): The path of the file where the log entries will be saved.
    """
    if save_path:
        with open(save_path, 'w') as log_file:
            log_file.write("\n".join(log_entries))
        log_event(f"Log saved: {save_path}")


def add_log_listener(listener: Callable):
    """
    Add a listener function that will be notified when a log event occurs.

    Args:
        listener (Callable): A callback function that will be called with the log entry.
    """
    log_listeners.append(listener)


def get_latest_error() -> str:
    """
    Get the most recent error entry.

    Returns:
        str: The most recent error entry or empty string if none was logged.
    """
    if len(error_entries) > 0:
        return error_entries[-1]
    else:
        return str()
