import pytest
from src.max_subarray_sum import kadanes_max_subarray_sum

def test_positive_numbers():
    """Test with an array of positive numbers."""
    assert kadanes_max_subarray_sum([1, 2, 3, 4]) == 10

def test_mixed_numbers():
    """Test with mixed positive and negative numbers."""
    assert kadanes_max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

def test_all_negative_numbers():
    """Test with all negative numbers."""
    assert kadanes_max_subarray_sum([-1, -2, -3, -4]) == -1

def test_single_element():
    """Test with a single element."""
    assert kadanes_max_subarray_sum([5]) == 5

def test_zero_element():
    """Test with zero elements."""
    assert kadanes_max_subarray_sum([0]) == 0

def test_input_type_error():
    """Test that TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list of integers"):
        kadanes_max_subarray_sum("not a list")

def test_empty_list_error():
    """Test that ValueError is raised for empty list."""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        kadanes_max_subarray_sum([])