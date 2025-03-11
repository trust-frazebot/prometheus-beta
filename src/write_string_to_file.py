def write_string_to_file(content: str, file_path: str) -> None:
    """
    Write a string to a specified file.

    Args:
        content (str): The string to write to the file.
        file_path (str): The path to the file where the content will be written.

    Raises:
        TypeError: If content is not a string or file_path is not a string.
        ValueError: If content is empty or file_path is an empty string.
        PermissionError: If the file cannot be written due to permission issues.
        IOError: If there are any other IO-related errors during file writing.
    """
    # Validate input types
    if not isinstance(content, str):
        raise TypeError("Content must be a string")
    if not isinstance(file_path, str):
        raise TypeError("File path must be a string")
    
    # Validate input values
    if not content:
        raise ValueError("Content cannot be an empty string")
    if not file_path:
        raise ValueError("File path cannot be an empty string")
    
    # Write the content to the file
    try:
        with open(file_path, 'w') as file:
            file.write(content)
    except PermissionError:
        raise PermissionError(f"Permission denied: Cannot write to {file_path}")
    except IOError as e:
        raise IOError(f"Error writing to file {file_path}: {str(e)}")