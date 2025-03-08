import pytest
from src.sum_of_multiples import sum_of_multiples

def test_basic_multiple():
    """Test basic multiple summing."""
    assert sum_of_multiples(10, [3, 5]) == 23  # 3 + 5 + 6 + 9

def test_single_multiple():
    """Test with a single multiple."""
    assert sum_of_multiples(10, [3]) == 18  # 3 + 6 + 9

def test_empty_multiples():
    """Test with empty multiples list."""
    assert sum_of_multiples(10, []) == 0

def test_large_limit():
    """Test with a larger limit."""
    assert sum_of_multiples(100, [3, 5]) == 2318

def test_unique_multiples():
    """Ensure only unique multiples are summed."""
    assert sum_of_multiples(10, [3, 6]) == 18  # 3 + 6 + 9 (avoid double-counting)

def test_zero_limit_raises_error():
    """Test that zero limit raises ValueError."""
    with pytest.raises(ValueError, match="Limit must be a positive integer."):
        sum_of_multiples(0, [3, 5])

def test_negative_limit_raises_error():
    """Test that negative limit raises ValueError."""
    with pytest.raises(ValueError, match="Limit must be a positive integer."):
        sum_of_multiples(-10, [3, 5])

def test_zero_multiple_raises_error():
    """Test that zero in multiples raises ValueError."""
    with pytest.raises(ValueError, match="All multiples must be positive integers."):
        sum_of_multiples(10, [3, 0, 5])

def test_negative_multiple_raises_error():
    """Test that negative multiple raises ValueError."""
    with pytest.raises(ValueError, match="All multiples must be positive integers."):
        sum_of_multiples(10, [3, -5, 7])

def test_single_multiple_at_limit():
    """Test multiple near the limit."""
    assert sum_of_multiples(9, [3]) == 9  # 3 + 6 

def test_various_multiples():
    """Test summing various multiples."""
    assert sum_of_multiples(20, [3, 5, 7]) == 99  # 3+6+9+5+10+15+7+14