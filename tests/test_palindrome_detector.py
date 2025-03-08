import pytest
from src.palindrome_detector import contains_palindrome_word

def test_contains_palindrome_word():
    # Test cases with palindrome words
    assert contains_palindrome_word("racecar is a palindrome") == True
    assert contains_palindrome_word("hello level world") == True
    assert contains_palindrome_word("123 level 456") == True
    
    # Test cases without palindrome words
    assert contains_palindrome_word("python is awesome") == False
    assert contains_palindrome_word("hello world") == False
    
    # Edge cases
    assert contains_palindrome_word("") == False
    assert contains_palindrome_word("a") == True
    assert contains_palindrome_word("ab") == False
    
    # Mixed cases with special characters and numbers
    assert contains_palindrome_word("hello! racecar, world") == True
    assert contains_palindrome_word("123 abc 456") == False
    
    # Case insensitivity
    assert contains_palindrome_word("Racecar is cool") == True
    
    # Longer palindrome words
    assert contains_palindrome_word("this is a madam in the house") == True
    assert contains_palindrome_word("radar is an excellent word") == True