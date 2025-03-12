import pytest
from src.burrows_wheeler_transform import burrows_wheeler_transform, inverse_burrows_wheeler_transform

def test_burrows_wheeler_transform_basic():
    """Test basic functionality of BWT"""
    assert burrows_wheeler_transform("banana") == "annb$aa"
    assert burrows_wheeler_transform("hello") == "ello$h"

def test_burrows_wheeler_transform_single_char():
    """Test BWT with a single character"""
    assert burrows_wheeler_transform("a") == "a$"

def test_burrows_wheeler_transform_empty_input():
    """Test that empty input raises a ValueError"""
    with pytest.raises(ValueError, match="Input string cannot be empty"):
        burrows_wheeler_transform("")

def test_burrows_wheeler_transform_non_string():
    """Test that non-string input raises a TypeError"""
    with pytest.raises(TypeError, match="Input must be a string"):
        burrows_wheeler_transform(123)

def test_inverse_burrows_wheeler_transform_basic():
    """Test basic functionality of inverse BWT"""
    assert inverse_burrows_wheeler_transform("annb$aa") == "banana"
    assert inverse_burrows_wheeler_transform("ello$h") == "hello"

def test_inverse_burrows_wheeler_transform_single_char():
    """Test inverse BWT with a single character"""
    assert inverse_burrows_wheeler_transform("a$") == "a"

def test_inverse_burrows_wheeler_transform_empty_input():
    """Test that empty input raises a ValueError"""
    with pytest.raises(ValueError, match="Input must be a valid BWT string"):
        inverse_burrows_wheeler_transform("")

def test_inverse_burrows_wheeler_transform_no_terminator():
    """Test that input without terminator raises a ValueError"""
    with pytest.raises(ValueError, match="Input must be a valid BWT string"):
        inverse_burrows_wheeler_transform("abc")

def test_inverse_burrows_wheeler_transform_non_string():
    """Test that non-string input raises a TypeError"""
    with pytest.raises(TypeError, match="Input must be a string"):
        inverse_burrows_wheeler_transform(123)

def test_bwt_roundtrip():
    """Test that BWT and inverse BWT recover the original string"""
    test_strings = [
        "banana", 
        "hello", 
        "Mississippi", 
        "algorithm", 
        "transformation",
        "a"
    ]
    
    for s in test_strings:
        bwt = burrows_wheeler_transform(s)
        recovered = inverse_burrows_wheeler_transform(bwt)
        assert recovered == s, f"Failed roundtrip for string: {s}"