import pytest
from src.sum_squares import sum_of_squares

def test_sum_of_squares_basic():
    """Test sum of squares with basic numeric list."""
    assert sum_of_squares([1, 2, 3]) == 14  # 1^2 + 2^2 + 3^2 = 1 + 4 + 9 = 14

def test_sum_of_squares_empty():
    """Test sum of squares with an empty list."""
    assert sum_of_squares([]) == 0

def test_sum_of_squares_negative():
    """Test sum of squares with negative numbers."""
    assert sum_of_squares([-1, -2, -3]) == 14  # Same as positive numbers due to squaring

def test_sum_of_squares_mixed_types():
    """Test sum of squares with mixed numeric types."""
    assert sum_of_squares([1, 2.5, 3]) == 14.25  # 1^2 + 2.5^2 + 3^2 = 1 + 6.25 + 9 = 14.25

def test_sum_of_squares_invalid_input():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError, match="Input must be a list"):
        sum_of_squares(123)

def test_sum_of_squares_non_numeric():
    """Test error handling for lists with non-numeric elements."""
    with pytest.raises(TypeError, match="All elements must be numeric"):
        sum_of_squares([1, 2, 'three'])

def test_sum_of_squares_none():
    """Test error handling for None input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        sum_of_squares(None)