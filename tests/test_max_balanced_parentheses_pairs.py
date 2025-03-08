import pytest
from src.max_balanced_parentheses_pairs import max_balanced_parentheses_pairs

def test_basic_balanced_pairs():
    """Test basic scenarios with balanced pairs."""
    assert max_balanced_parentheses_pairs("()()") == 2
    assert max_balanced_parentheses_pairs("(())") == 2
    assert max_balanced_parentheses_pairs("((()))") == 3

def test_unbalanced_input():
    """Test scenarios with unbalanced parentheses."""
    assert max_balanced_parentheses_pairs("(()") == 1
    assert max_balanced_parentheses_pairs("())") == 1
    assert max_balanced_parentheses_pairs(")()(") == 1

def test_mixed_characters():
    """Test scenarios with mixed characters."""
    assert max_balanced_parentheses_pairs("(a)b()") == 2
    assert max_balanced_parentheses_pairs("abc()()def") == 2

def test_edge_cases():
    """Test edge cases."""
    assert max_balanced_parentheses_pairs("") == 0
    assert max_balanced_parentheses_pairs("(((())))") == 4
    assert max_balanced_parentheses_pairs("))))((((") == 0

def test_type_handling():
    """Test type handling."""
    with pytest.raises(TypeError):
        max_balanced_parentheses_pairs(None)
    with pytest.raises(TypeError):
        max_balanced_parentheses_pairs(123)