import pytest
from src.number_sorting import sort_nums, optimal_sort

def test_sort_nums_basic_sorting():
    """Test basic sorting functionality."""
    input_list = [5, 2, 9, 1, 7]
    result = sort_nums(input_list.copy())
    assert result == [1, 2, 5, 7, 9]

def test_optimal_sort_basic_sorting():
    """Test optimal sorting functionality."""
    input_list = [5, 2, 9, 1, 7]
    result = optimal_sort(input_list.copy())
    assert result == [1, 2, 5, 7, 9]

def test_both_sorting_methods_same_result():
    """Verify both sorting methods produce identical results."""
    test_cases = [
        [5, 2, 9, 1, 7],
        [100, 3, 2, 1],
        [],
        [1],
        [3, 3, 3, 3],
        [-1, -5, 10, 0]
    ]
    
    for case in test_cases:
        sort_nums_result = sort_nums(case.copy())
        optimal_sort_result = optimal_sort(case.copy())
        assert sort_nums_result == optimal_sort_result

def test_empty_list_handling():
    """Test sorting with an empty list."""
    assert sort_nums([]) == []
    assert optimal_sort([]) == []

def test_large_list_sorting():
    """Test sorting a larger list."""
    import random
    
    # Create a large random list
    large_list = [random.randint(-1000, 1000) for _ in range(1000)]
    
    # Verify that manual sort and optimal sort produce same result
    assert sort_nums(large_list.copy()) == optimal_sort(large_list.copy())