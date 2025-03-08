import pytest
from src.longest_increasing_subsequence import longest_increasing_subsequence_length

def test_typical_increasing_sequence():
    assert longest_increasing_subsequence_length([1,3,5,4,7]) == 3

def test_no_increasing_sequence():
    assert longest_increasing_subsequence_length([7,6,5,4,3]) == 1

def test_all_equal_numbers():
    assert longest_increasing_subsequence_length([2,2,2,2]) == 1

def test_empty_array():
    assert longest_increasing_subsequence_length([]) == 0

def test_single_element():
    assert longest_increasing_subsequence_length([42]) == 1

def test_multiple_increasing_subsequences():
    assert longest_increasing_subsequence_length([1,2,3,1,2,3,4]) == 4

def test_mixed_sequence():
    assert longest_increasing_subsequence_length([1,3,5,7,2,3,4,5]) == 4

def test_negative_numbers():
    assert longest_increasing_subsequence_length([-3,-2,-1,0,1]) == 5

def test_large_array():
    large_test_array = list(range(1000)) + list(range(500, 1500))
    assert longest_increasing_subsequence_length(large_test_array) == 1000