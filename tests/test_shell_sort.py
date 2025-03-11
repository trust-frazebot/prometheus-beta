import pytest
from src.shell_sort import shell_sort

def test_shell_sort_basic():
    """Test basic sorting of a random list of integers"""
    arr = [64, 34, 25, 12, 22, 11, 90]
    assert shell_sort(arr) == [11, 12, 22, 25, 34, 64, 90]

def test_shell_sort_empty_list():
    """Test sorting an empty list"""
    arr = []
    assert shell_sort(arr) == []

def test_shell_sort_single_element():
    """Test sorting a list with a single element"""
    arr = [42]
    assert shell_sort(arr) == [42]

def test_shell_sort_already_sorted():
    """Test sorting a list that is already sorted"""
    arr = [1, 2, 3, 4, 5]
    assert shell_sort(arr) == [1, 2, 3, 4, 5]

def test_shell_sort_reverse_sorted():
    """Test sorting a list in reverse order"""
    arr = [5, 4, 3, 2, 1]
    assert shell_sort(arr) == [1, 2, 3, 4, 5]

def test_shell_sort_duplicates():
    """Test sorting a list with duplicate elements"""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert shell_sort(arr) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

def test_shell_sort_floating_point():
    """Test sorting a list of floating-point numbers"""
    arr = [3.14, 2.71, 1.41, 0.58, 2.23]
    assert shell_sort(arr) == [0.58, 1.41, 2.23, 2.71, 3.14]

def test_shell_sort_invalid_input():
    """Test that a TypeError is raised for non-list input"""
    with pytest.raises(TypeError):
        shell_sort("not a list")

def test_shell_sort_comparable_objects():
    """Test sorting with comparable custom objects"""
    class Person:
        def __init__(self, age):
            self.age = age
        
        def __lt__(self, other):
            return self.age < other.age
    
    people = [Person(25), Person(30), Person(20), Person(35)]
    sorted_people = shell_sort(people)
    assert [p.age for p in sorted_people] == [20, 25, 30, 35]