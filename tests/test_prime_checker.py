import pytest
from src.prime_checker import is_prime

def test_prime_numbers():
    """Test that known prime numbers are correctly identified."""
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    for num in prime_numbers:
        assert is_prime(num) is True, f"{num} should be prime"

def test_non_prime_numbers():
    """Test that known non-prime numbers are correctly identified."""
    non_prime_numbers = [0, 1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20]
    for num in non_prime_numbers:
        assert is_prime(num) is False, f"{num} should not be prime"

def test_large_prime():
    """Test a larger prime number."""
    assert is_prime(97) is True
    assert is_prime(101) is True

def test_large_non_prime():
    """Test a larger non-prime number."""
    assert is_prime(100) is False
    assert is_prime(999) is False

def test_invalid_inputs():
    """Test that invalid inputs raise appropriate errors."""
    with pytest.raises(ValueError, match="Input must be an integer"):
        is_prime(3.14)
    
    with pytest.raises(ValueError, match="Input must be an integer"):
        is_prime("not a number")
    
    with pytest.raises(ValueError, match="Input must be an integer"):
        is_prime(None)