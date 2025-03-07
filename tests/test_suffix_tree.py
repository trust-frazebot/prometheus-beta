import pytest
from src.suffix_tree import SuffixTree

def test_suffix_tree_initialization():
    """Test basic initialization of Suffix Tree."""
    text = "banana"
    tree = SuffixTree(text)
    assert tree.text == "banana$"
    # Remove root attribute check as it's no longer part of the implementation

def test_basic_search():
    """Test basic pattern search functionality."""
    text = "hello world"
    tree = SuffixTree(text)
    
    # Test existing patterns
    assert tree.search("hello") == True
    assert tree.search("world") == True
    assert tree.search("lo wo") == True
    
    # Test non-existing patterns
    assert tree.search("python") == False
    assert tree.search("xyz") == False

def test_search_empty_pattern():
    """Test searching with an empty pattern."""
    text = "banana"
    tree = SuffixTree(text)
    
    assert tree.search("") == False

def test_case_sensitivity():
    """Test that search is case-sensitive."""
    text = "Hello World"
    tree = SuffixTree(text)
    
    assert tree.search("hello") == False
    assert tree.search("Hello") == True

def test_find_all_occurrences():
    """Test finding all occurrences of a pattern."""
    text = "banana banana"
    tree = SuffixTree(text)
    
    # Verify finds multiple occurrences
    occurrences = tree.find_all_occurrences("banana")
    assert len(occurrences) > 1
    
    # Test single occurrence pattern
    occurrences = tree.find_all_occurrences("ana")
    assert len(occurrences) > 0
    
    # Test non-existing pattern
    occurrences = tree.find_all_occurrences("xyz")
    assert len(occurrences) == 0

def test_edge_cases():
    """Test various edge cases."""
    # Empty string
    tree = SuffixTree("")
    assert tree.search("anything") == False
    
    # Single character
    tree = SuffixTree("a")
    assert tree.search("a") == True
    assert tree.search("b") == False

def test_long_pattern_search():
    """Test searching with very long patterns."""
    text = "a" * 1000
    tree = SuffixTree(text)
    
    assert tree.search("a" * 500) == True
    assert tree.search("a" * 1001) == False