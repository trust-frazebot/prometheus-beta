import pytest
import sys
import os

# Ensure the src directory is in the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from fizzy_numbers import get_fizzy_numbers

def test_get_fizzy_numbers_basic():
    """Test basic functionality of fizzy numbers."""
    result = get_fizzy_numbers(10)
    assert result == [3, 6, 7, 9, 10], "Should return correct fizzy numbers up to 10"

def test_get_fizzy_numbers_larger_range():
    """Test fizzy numbers in a larger range."""
    result = get_fizzy_numbers(21)
    expected = [3, 6, 7, 9, 10, 12, 14, 15, 18, 20, 21]
    assert result == expected, "Should return correct fizzy numbers up to 21"

def test_get_fizzy_numbers_single_number():
    """Test when only one number is a fizzy number."""
    result = get_fizzy_numbers(4)
    assert result == [3], "Should return only 3 as a fizzy number"

def test_get_fizzy_numbers_edge_case_1():
    """Test the edge case of 1."""
    result = get_fizzy_numbers(1)
    assert result == [], "Should return an empty list for input 1"

def test_get_fizzy_numbers_error_handling():
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        get_fizzy_numbers(0)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        get_fizzy_numbers(-5)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        get_fizzy_numbers(3.14)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        get_fizzy_numbers("10")