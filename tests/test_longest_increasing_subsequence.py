import pytest
from src.longest_increasing_subsequence import find_longest_increasing_subsequence

def test_empty_array():
    """Test behavior with an empty array"""
    length, subsequence = find_longest_increasing_subsequence([])
    assert length == 0
    assert subsequence == []

def test_single_element():
    """Test array with a single element"""
    length, subsequence = find_longest_increasing_subsequence([5])
    assert length == 1
    assert subsequence == [5]

def test_basic_increasing_sequence():
    """Test a simple increasing sequence"""
    length, subsequence = find_longest_increasing_subsequence([10, 22, 33, 44, 55])
    assert length == 5
    assert subsequence == [10, 22, 33, 44, 55]

def test_non_consecutive_increasing_sequence():
    """Test a sequence where the longest subsequence is not consecutive"""
    length, subsequence = find_longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18])
    assert length == 4
    assert subsequence == [2, 5, 7, 101]

def test_repeated_elements():
    """Test a sequence with repeated elements"""
    length, subsequence = find_longest_increasing_subsequence([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15])
    assert length == 6
    assert subsequence == [0, 2, 6, 9, 13, 15]

def test_descending_sequence():
    """Test a completely descending sequence"""
    length, subsequence = find_longest_increasing_subsequence([5, 4, 3, 2, 1])
    assert length == 1
    assert len(subsequence) == 1
    assert subsequence[0] in [5, 4, 3, 2, 1]

def test_mixed_sequence():
    """Test a mixed sequence with multiple increasing subsequences"""
    length, subsequence = find_longest_increasing_subsequence([1, 11, 2, 10, 4, 5, 2, 1])
    assert length == 3
    assert subsequence in [[1, 2, 10], [1, 4, 5], [2, 4, 5]]

def test_large_input():
    """Test a larger input to ensure performance"""
    large_input = list(range(1000))
    length, subsequence = find_longest_increasing_subsequence(large_input)
    assert length == 1000
    assert subsequence == large_input