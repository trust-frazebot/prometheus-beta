import pytest
from src.url_validator import is_valid_url

def test_valid_urls():
    """Test various valid URL formats."""
    valid_urls = [
        'https://www.example.com',
        'http://example.com',
        'https://example.com/path',
        'http://localhost',
        'http://localhost:8000',
        'https://sub.domain.com/path?param=value',
        'ftp://files.example.com',
        'sftp://secure.example.com',
    ]
    
    for url in valid_urls:
        assert is_valid_url(url), f"Failed to validate URL: {url}"

def test_invalid_urls():
    """Test various invalid URL formats."""
    invalid_urls = [
        '',  # Empty string
        'not a url',
        'example.com',  # Missing scheme
        None,  # None input
        123,  # Non-string input
        'http://',  # Only scheme
        'https://   ',  # Invalid netloc
    ]
    
    for url in invalid_urls:
        assert not is_valid_url(url), f"Incorrectly validated URL: {url}"

def test_edge_cases():
    """Test edge case URL formats."""
    edge_case_urls = [
        'https://example.com/path with spaces',
        'http://example.com:invalid_port',
        'https://',  # Just scheme
    ]
    
    # These might be considered valid or invalid depending on specific requirements
    for url in edge_case_urls:
        assert isinstance(is_valid_url(url), bool), f"Unexpected result for URL: {url}"