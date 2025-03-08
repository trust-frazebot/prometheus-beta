import pytest
from src.first_non_repeating_character import first_non_repeating_character

def test_first_non_repeating_character():
    # Test basic cases with non-repeating characters
    assert first_non_repeating_character("leetcode") == "l"
    assert first_non_repeating_character("loveleetcode") == "v"
    
    # Test cases with no non-repeating characters
    assert first_non_repeating_character("aabb") is None
    assert first_non_repeating_character("aaaaaa") is None
    
    # Test empty string
    assert first_non_repeating_character("") is None
    
    # Test single character strings
    assert first_non_repeating_character("a") == "a"
    
    # Test error cases
    with pytest.raises(ValueError, match="Input must contain only lowercase letters"):
        first_non_repeating_character("Hello")
    
    with pytest.raises(ValueError, match="Input must contain only lowercase letters"):
        first_non_repeating_character("123")
    
    with pytest.raises(ValueError, match="Input must contain only lowercase letters"):
        first_non_repeating_character("a1b")