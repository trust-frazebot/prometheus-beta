import pytest
from src.palindrome_substring_counter import count_palindromic_substrings

def test_basic_palindrome_counts():
    """Test basic palindrome substring counting"""
    assert count_palindromic_substrings("abc") == 3
    assert count_palindromic_substrings("aaa") == 6
    assert count_palindromic_substrings("racecar") == 10

def test_empty_and_single_char_inputs():
    """Test edge cases with empty and single character inputs"""
    assert count_palindromic_substrings("") == 0
    assert count_palindromic_substrings("a") == 1
    assert count_palindromic_substrings("  ") == 0

def test_complex_palindromes():
    """Test more complex palindrome scenarios"""
    assert count_palindromic_substrings("A man a plan a canal: Panama") == 12
    assert count_palindromic_substrings("race a car") == 7

def test_non_palindrome_string():
    """Test string with no palindrome substrings"""
    assert count_palindromic_substrings("abcdef") == 6

def test_mixed_case_palindromes():
    """Test palindromes with mixed case"""
    assert count_palindromic_substrings("AbBa") == 5

def test_special_characters():
    """Test strings with special characters"""
    assert count_palindromic_substrings("a!b@c#b$a") == 3