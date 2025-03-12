import pytest
from src.unique_substrings import extract_unique_substrings

def test_basic_unique_substrings():
    """Test basic substring extraction."""
    result = extract_unique_substrings("abc")
    assert set(result) == set(["a", "b", "c", "ab", "bc", "abc"])

def test_empty_string():
    """Test extraction from an empty string."""
    assert extract_unique_substrings("") == []

def test_single_character():
    """Test extraction from a single character string."""
    result = extract_unique_substrings("a")
    assert result == ["a"]

def test_repeated_characters():
    """Test extraction with repeated characters."""
    result = extract_unique_substrings("aaa")
    assert set(result) == set(["a", "aa", "aaa"])

def test_invalid_input_type():
    """Test raising TypeError for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        extract_unique_substrings(123)

def test_complex_string():
    """Test extraction from a more complex string."""
    result = extract_unique_substrings("hello")
    expected = set(["h", "e", "l", "o", "he", "el", "ll", "lo", 
                    "hel", "ell", "llo", "hello"])
    assert set(result) == expected

def test_sorted_output():
    """Verify that the output is sorted."""
    result = extract_unique_substrings("cab")
    assert result == ["a", "ab", "b", "c", "ca", "cab"]