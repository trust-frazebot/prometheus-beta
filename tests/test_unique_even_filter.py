import pytest
from src.unique_even_filter import filter_unique_even_numbers

def test_filter_unique_even_numbers_basic():
    """Test basic functionality of filtering unique even numbers."""
    input_list = [1, 2, 3, 4, 2, 5, 6, 4, 7, 8]
    expected = [2, 4, 6, 8]
    assert filter_unique_even_numbers(input_list) == expected

def test_filter_unique_even_numbers_empty_list():
    """Test filtering an empty list."""
    assert filter_unique_even_numbers([]) == []

def test_filter_unique_even_numbers_no_evens():
    """Test a list with no even numbers."""
    input_list = [1, 3, 5, 7]
    assert filter_unique_even_numbers(input_list) == []

def test_filter_unique_even_numbers_only_evens():
    """Test a list with only even numbers."""
    input_list = [2, 4, 6, 2, 4, 6]
    expected = [2, 4, 6]
    assert filter_unique_even_numbers(input_list) == expected

def test_filter_unique_even_numbers_mixed_types():
    """Test handling of mixed positive and negative even numbers."""
    input_list = [-2, 1, -2, 3, 4, -4, 5, 6]
    expected = [-2, 4, -4, 6]
    assert filter_unique_even_numbers(input_list) == expected

def test_filter_unique_even_numbers_order_preservation():
    """Test that the original order of first appearance is preserved."""
    input_list = [10, 5, 2, 3, 10, 2, 4, 5, 6]
    expected = [10, 2, 4, 6]
    assert filter_unique_even_numbers(input_list) == expected