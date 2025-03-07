import pytest
from src.longest_common_prefix import find_longest_common_prefix

def test_common_prefix_basic():
    assert find_longest_common_prefix(["flower", "flow", "flight"]) == "fl"

def test_common_prefix_single_string():
    assert find_longest_common_prefix(["hello"]) == "hello"

def test_common_prefix_empty_list():
    assert find_longest_common_prefix([]) == ""

def test_common_prefix_no_common_prefix():
    assert find_longest_common_prefix(["dog", "racecar", "car"]) == ""

def test_common_prefix_full_match():
    assert find_longest_common_prefix(["apple", "apple", "apple"]) == "apple"

def test_common_prefix_case_sensitive():
    assert find_longest_common_prefix(["Apple", "apple"]) == ""

def test_invalid_input_not_list():
    with pytest.raises(TypeError, match="Input must be a list of strings"):
        find_longest_common_prefix("not a list")

def test_invalid_input_non_string_elements():
    with pytest.raises(ValueError, match="All elements must be strings"):
        find_longest_common_prefix(["string", 123, "another"])

def test_common_prefix_unicode():
    assert find_longest_common_prefix(["café", "cafè", "cafeteria"]) == "caf"

def test_common_prefix_empty_strings():
    assert find_longest_common_prefix(["", "", ""]) == ""

def test_common_prefix_partial_empty():
    assert find_longest_common_prefix(["hello", "", "help"]) == ""