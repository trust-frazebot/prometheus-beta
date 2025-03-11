import os
from datetime import datetime

def get_file_last_modified_date(file_path):
    """
    Get the last modified date of a file.

    Args:
        file_path (str): Path to the file.

    Returns:
        datetime: Last modified datetime of the file.

    Raises:
        FileNotFoundError: If the file does not exist.
        PermissionError: If there's no permission to access the file.
        OSError: For other OS-related errors when accessing the file.
    """
    # Validate input
    if not isinstance(file_path, str):
        raise TypeError("File path must be a string")

    # Check if file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    # Check if it's a file (not a directory)
    if not os.path.isfile(file_path):
        raise ValueError(f"Path is not a file: {file_path}")

    try:
        # Get last modified timestamp and convert to datetime
        modified_timestamp = os.path.getmtime(file_path)
        return datetime.fromtimestamp(modified_timestamp)
    except PermissionError:
        raise PermissionError(f"Permission denied accessing file: {file_path}")
    except OSError as e:
        raise OSError(f"Error accessing file: {file_path}, {str(e)}")