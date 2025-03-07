import re
from urllib.parse import urlparse

def is_valid_url(url: str) -> bool:
    """
    Check if the given string is a valid URL.

    Args:
        url (str): The URL string to validate.

    Returns:
        bool: True if the URL is valid, False otherwise.

    Examples:
        >>> is_valid_url('https://www.example.com')
        True
        >>> is_valid_url('http://localhost:8000')
        True
        >>> is_valid_url('ftp://files.example.com')
        True
        >>> is_valid_url('not a url')
        False
    """
    # Check if the input is a string and not empty
    if not isinstance(url, str) or not url:
        return False
    
    try:
        # Use urlparse to check basic URL structure
        result = urlparse(url)
        
        # Check if scheme and netloc are present
        return all([result.scheme, result.netloc])
    except Exception:
        return False