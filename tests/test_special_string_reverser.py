import pytest
from src.special_string_reverser import special_string_reverser

def test_basic_reversal():
    """Test basic string reversal."""
    assert special_string_reverser("hello") == "olleh"

def test_palindrome_preservation():
    """Test that palindromes remain unchanged."""
    assert special_string_reverser("racecar") == "racecar"
    assert special_string_reverser("level123level") == "level123level"

def test_integer_reversal():
    """Test that integers are reversed separately."""
    assert special_string_reverser("123") == "321"
    assert special_string_reverser("a123b") == "a321b"

def test_mixed_string():
    """Test a mix of different types of substrings."""
    assert special_string_reverser("hello123world") == "olleh321dlrow"
    assert special_string_reverser("racecar123world") == "racecar321dlrow"

def test_special_characters():
    """Test strings with special characters."""
    assert special_string_reverser("hello, world!") == "olleh, dlrow!"
    assert special_string_reverser("123, abc!") == "321, cba!"

def test_edge_cases():
    """Test edge cases."""
    assert special_string_reverser("") == ""
    assert special_string_reverser(" ") == " "

def test_error_handling():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        special_string_reverser(123)
    with pytest.raises(TypeError):
        special_string_reverser(None)

def test_complex_scenarios():
    """Test more complex string scenarios."""
    assert special_string_reverser("a1b2c3") == "a1b2c3"[::-1]
    assert special_string_reverser("radar123world") == "radar321dlrow"
    assert special_string_reverser("hello123racecar") == "olleh321racecar"