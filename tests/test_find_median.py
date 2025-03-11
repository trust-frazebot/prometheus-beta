import pytest
from src.find_median import find_median

def test_median_odd_length_list():
    """Test median for a list with odd number of elements."""
    assert find_median([1, 3, 5]) == 3
    assert find_median([1, 2, 3, 4, 5]) == 3

def test_median_even_length_list():
    """Test median for a list with even number of elements."""
    assert find_median([1, 2, 3, 4]) == 2.5
    assert find_median([2, 4, 6, 8]) == 5

def test_median_single_element():
    """Test median for a list with a single element."""
    assert find_median([42]) == 42

def test_median_with_floats():
    """Test median with floating point numbers."""
    assert find_median([1.5, 2.5, 3.5]) == 2.5
    assert find_median([1.1, 2.2, 3.3, 4.4]) == 2.75

def test_empty_list_raises_error():
    """Test that empty list raises a ValueError."""
    with pytest.raises(ValueError, match="Cannot find median of an empty list"):
        find_median([])

def test_non_list_input_raises_error():
    """Test that non-list input raises a TypeError."""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_median("not a list")
    with pytest.raises(TypeError, match="Input must be a list"):
        find_median(123)

def test_non_numeric_list_raises_error():
    """Test that list with non-numeric elements raises a TypeError."""
    with pytest.raises(TypeError, match="All list elements must be numeric"):
        find_median([1, 2, 'a', 4])
    with pytest.raises(TypeError, match="All list elements must be numeric"):
        find_median([1, 2, None, 4])