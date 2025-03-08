import pytest
from src.ip_address_validator import validate_single_digit_ip

def test_valid_ip_addresses():
    """Test valid single-digit IP addresses"""
    valid_cases = [
        "1.2.3.4",
        "0.0.0.0",
        "9.9.9.9"
    ]
    for ip in valid_cases:
        assert validate_single_digit_ip(ip) is True, f"{ip} should be valid"

def test_invalid_ip_addresses():
    """Test invalid IP addresses"""
    invalid_cases = [
        # Wrong number of octets
        "1.2.3",  # Too few
        "1.2.3.4.5",  # Too many
        
        # Non-digit octets
        "a.1.2.3",  # Non-numeric
        "1.2.3.b",  # Non-numeric
        
        # Multi-digit octets
        "10.1.2.3",  # Two-digit octet
        "1.22.3.4",  # Two-digit octet
        
        # Out of single-digit range
        "-1.2.3.4",  # Negative
        "1.2.3.10",  # > 9
        
        # Non-string input
        123,
        None,
        [],
        
        # Empty string
        "",
        
        # Spaces
        " 1.2.3.4 ",
        "1. 2.3.4"
    ]
    for ip in invalid_cases:
        assert validate_single_digit_ip(ip) is False, f"{ip} should be invalid"

def test_edge_cases():
    """Test edge case scenarios"""
    # Boundary cases
    assert validate_single_digit_ip("0.0.0.0") is True
    assert validate_single_digit_ip("9.9.9.9") is True