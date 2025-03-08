import pytest
from src.find_longest_substring import find_longest_substring

def test_find_longest_substring_basic_cases():
    """Test basic functionality of finding longest unique substring."""
    assert find_longest_substring("abcabcbb") == "abc"
    assert find_longest_substring("bbbbb") == "b"
    assert find_longest_substring("pwwkew") == "wke"

def test_find_longest_substring_edge_cases():
    """Test edge cases like empty string and single character."""
    assert find_longest_substring("") == ""
    assert find_longest_substring("a") == "a"
    assert find_longest_substring("aab") == "ab"

def test_find_longest_substring_complex_cases():
    """Test more complex scenarios with unique substrings."""
    assert find_longest_substring("dvdf") == "vdf"
    assert find_longest_substring("tmmzuxt") == "mzuxt"

def test_find_longest_substring_all_unique():
    """Test when entire string has unique characters."""
    assert find_longest_substring("abcdefg") == "abcdefg"

def test_find_longest_substring_repeated_chars():
    """Test scenarios with multiple repeated characters."""
    assert find_longest_substring("abcdefgabcdefg") == "abcdefg"
    assert find_longest_substring("abcabcdbb") == "abcd"

def test_find_longest_substring_unicode():
    """Test with unicode characters."""
    result = find_longest_substring("αβγαβδ")
    assert len(result) == 4  # Longest unique substring length
    assert len(set(result)) == 4  # Ensure unique characters

def test_find_longest_substring_special_characters():
    """Test with special characters and spaces."""
    result = find_longest_substring("  a b  ")
    # Allow either 3 or 4 characters 
    assert len(result) in [3, 4]  
    assert len(set(result)) == len(result)  # Ensure all characters are unique