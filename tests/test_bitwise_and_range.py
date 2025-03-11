import pytest
from src.bitwise_and_range import bitwise_and_range

def test_bitwise_and_range_same_number():
    """Test when lower and upper bounds are the same"""
    assert bitwise_and_range(5, 5) == 5

def test_bitwise_and_range_consecutive_numbers():
    """Test bitwise AND with consecutive numbers"""
    assert bitwise_and_range(5, 7) == 4

def test_bitwise_and_range_zero_to_three():
    """Test bitwise AND from zero to three"""
    assert bitwise_and_range(0, 3) == 0

def test_bitwise_and_range_larger_range():
    """Test bitwise AND with a larger range"""
    assert bitwise_and_range(10, 15) == 8

def test_bitwise_and_range_single_number():
    """Test with a single number"""
    assert bitwise_and_range(10, 10) == 10

def test_bitwise_and_negative_input():
    """Test that negative inputs raise a ValueError"""
    with pytest.raises(ValueError):
        bitwise_and_range(-1, 5)
    with pytest.raises(ValueError):
        bitwise_and_range(5, -1)

def test_bitwise_and_invalid_range():
    """Test that invalid range (m > n) raises a ValueError"""
    with pytest.raises(ValueError):
        bitwise_and_range(7, 5)

def test_bitwise_and_range_zero():
    """Test bitwise AND range with zero"""
    assert bitwise_and_range(0, 0) == 0