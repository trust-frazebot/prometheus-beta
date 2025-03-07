import pytest
from src.tree_sort import tree_sort

def test_tree_sort_basic():
    """Test sorting a basic list of integers"""
    input_list = [5, 2, 9, 1, 7, 6]
    assert tree_sort(input_list) == [1, 2, 5, 6, 7, 9]

def test_tree_sort_empty_list():
    """Test sorting an empty list"""
    assert tree_sort([]) == []

def test_tree_sort_single_element():
    """Test sorting a list with a single element"""
    assert tree_sort([42]) == [42]

def test_tree_sort_already_sorted():
    """Test sorting a list that is already sorted"""
    input_list = [1, 2, 3, 4, 5]
    assert tree_sort(input_list) == [1, 2, 3, 4, 5]

def test_tree_sort_reverse_sorted():
    """Test sorting a list in reverse order"""
    input_list = [5, 4, 3, 2, 1]
    assert tree_sort(input_list) == [1, 2, 3, 4, 5]

def test_tree_sort_with_duplicates():
    """Test sorting a list with duplicate elements"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    assert tree_sort(input_list) == [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]

def test_tree_sort_with_floats():
    """Test sorting a list of floating-point numbers"""
    input_list = [3.14, 2.71, 1.41, 0.58]
    assert tree_sort(input_list) == [0.58, 1.41, 2.71, 3.14]

def test_tree_sort_invalid_input_type():
    """Test that a TypeError is raised for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        tree_sort("not a list")

def test_tree_sort_uncomparable_elements():
    """Test that a ValueError is raised for uncomparable elements"""
    with pytest.raises(ValueError, match="List contains elements that cannot be compared"):
        tree_sort([1, 2, "3", 4])

def test_tree_sort_preserves_original_list():
    """Test that the original list is not modified"""
    input_list = [5, 2, 9, 1, 7, 6]
    original_copy = input_list.copy()
    tree_sort(input_list)
    assert input_list == original_copy