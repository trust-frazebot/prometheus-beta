import pytest
from src.alternating_title_case import alternating_title_case

def test_basic_alternating_case():
    # Test basic functionality
    assert alternating_title_case("hello world python") == "Hello world Python"
    assert alternating_title_case("this is a test") == "This is A test"

def test_empty_string():
    # Test empty string
    assert alternating_title_case("") == ""

def test_single_word():
    # Test single word
    assert alternating_title_case("hello") == "Hello"

def test_multiple_words():
    # Test multiple words with longer input
    assert alternating_title_case("the quick brown fox jumps") == "The quick Brown fox Jumps"

def test_error_handling():
    # Test error handling for non-string input
    with pytest.raises(TypeError, match="Input must be a string"):
        alternating_title_case(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        alternating_title_case(None)

def test_whitespace_handling():
    # Test handling of extra whitespace
    assert alternating_title_case("  hello   world  ") == "Hello world"

def test_mixed_case_input():
    # Test input with mixed case
    assert alternating_title_case("HeLLo WoRLd PYthOn") == "Hello world Python"