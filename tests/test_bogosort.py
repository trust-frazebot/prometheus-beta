import pytest
import random
from src.bogosort import bogosort, is_sorted

def test_bogosort_empty_list():
    """Test sorting an empty list"""
    assert bogosort([]) == []

def test_bogosort_single_element():
    """Test sorting a list with a single element"""
    assert bogosort([5]) == [5]

def test_bogosort_already_sorted():
    """Test sorting a list that is already sorted"""
    sorted_list = [1, 2, 3, 4, 5]
    assert bogosort(sorted_list) == sorted_list

def test_bogosort_unsorted_integers():
    """Test sorting a list of unsorted integers"""
    unsorted = [5, 2, 8, 1, 9]
    result = bogosort(unsorted)
    assert is_sorted(result)
    assert set(result) == set(unsorted)

def test_bogosort_with_duplicates():
    """Test sorting a list with duplicate elements"""
    unsorted = [3, 1, 4, 1, 5, 9, 2, 6]
    result = bogosort(unsorted)
    assert is_sorted(result)
    assert set(result) == set(unsorted)

def test_bogosort_invalid_input():
    """Test that TypeError is raised for non-list inputs"""
    with pytest.raises(TypeError):
        bogosort("not a list")
    with pytest.raises(TypeError):
        bogosort(123)

def test_is_sorted_function():
    """Test the is_sorted helper function"""
    assert is_sorted([]) == True
    assert is_sorted([1]) == True
    assert is_sorted([1, 2, 3]) == True
    assert is_sorted([3, 2, 1]) == False
    assert is_sorted([1, 1, 2, 3]) == True  # Handles duplicates