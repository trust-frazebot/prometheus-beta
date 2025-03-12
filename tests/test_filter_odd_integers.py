import pytest
from src.filter_odd_integers import filter_and_sort_odd_integers

def test_filter_and_sort_odd_integers_mixed_list():
    """Test filtering and sorting odd integers from a mixed list."""
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert filter_and_sort_odd_integers(input_list) == [1, 3, 5, 7, 9]

def test_filter_and_sort_odd_integers_only_even():
    """Test list with only even numbers."""
    input_list = [2, 4, 6, 8]
    assert filter_and_sort_odd_integers(input_list) == []

def test_filter_and_sort_odd_integers_empty_list():
    """Test empty input list."""
    input_list = []
    assert filter_and_sort_odd_integers(input_list) == []

def test_filter_and_sort_odd_integers_only_odd():
    """Test list with only odd numbers."""
    input_list = [9, 7, 5, 3, 1]
    assert filter_and_sort_odd_integers(input_list) == [1, 3, 5, 7, 9]

def test_filter_and_sort_odd_integers_negative_numbers():
    """Test list with negative numbers."""
    input_list = [-1, -2, -3, -4, -5, 0, 1, 2, 3, 4, 5]
    assert filter_and_sort_odd_integers(input_list) == [-5, -3, -1, 1, 3, 5]

def test_filter_and_sort_odd_integers_large_numbers():
    """Test list with large numbers."""
    input_list = [10001, 10002, 10003, 10004, 10005]
    assert filter_and_sort_odd_integers(input_list) == [10001, 10003, 10005]