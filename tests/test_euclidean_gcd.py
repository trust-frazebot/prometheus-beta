import pytest
from src.euclidean_gcd import euclidean_gcd

def test_gcd_basic_cases():
    """Test basic GCD calculations"""
    assert euclidean_gcd(48, 18) == 6
    assert euclidean_gcd(54, 24) == 6
    assert euclidean_gcd(17, 23) == 1
    assert euclidean_gcd(0, 5) == 5
    assert euclidean_gcd(5, 0) == 5

def test_gcd_same_number():
    """Test GCD when both numbers are the same"""
    assert euclidean_gcd(7, 7) == 7
    assert euclidean_gcd(100, 100) == 100

def test_gcd_one_is_multiple():
    """Test GCD when one number is a multiple of the other"""
    assert euclidean_gcd(12, 3) == 3
    assert euclidean_gcd(3, 12) == 3

def test_gcd_zero_cases():
    """Test GCD with zero inputs"""
    assert euclidean_gcd(0, 0) == 0

def test_gcd_large_numbers():
    """Test GCD with larger numbers"""
    assert euclidean_gcd(1071, 462) == 21

def test_invalid_input_type():
    """Test error handling for non-integer inputs"""
    with pytest.raises(TypeError):
        euclidean_gcd(10.5, 20)
    with pytest.raises(TypeError):
        euclidean_gcd("10", 20)
    with pytest.raises(TypeError):
        euclidean_gcd([10], 20)

def test_negative_input():
    """Test error handling for negative inputs"""
    with pytest.raises(ValueError):
        euclidean_gcd(-10, 20)
    with pytest.raises(ValueError):
        euclidean_gcd(10, -20)
    with pytest.raises(ValueError):
        euclidean_gcd(-10, -20)