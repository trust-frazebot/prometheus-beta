import pytest
from src.matrix_search import search_matrix

def test_matrix_search_basic():
    """Test basic matrix search functionality"""
    matrix = [
        [1, 3, 5],
        [7, 9, 11],
        [13, 15, 17]
    ]
    assert search_matrix(matrix, 9) == True
    assert search_matrix(matrix, 8) == False

def test_matrix_search_edge_cases():
    """Test edge cases"""
    # Empty matrix
    assert search_matrix([], 5) == False
    
    # Matrix with empty rows
    assert search_matrix([[], [], []], 5) == False
    
    # Single element matrix
    matrix_single = [[5]]
    assert search_matrix(matrix_single, 5) == True
    assert search_matrix(matrix_single, 6) == False

def test_matrix_search_various_inputs():
    """Test matrix search with different matrix configurations"""
    # Rectangular matrix
    matrix_rect = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    assert search_matrix(matrix_rect, 4) == True
    assert search_matrix(matrix_rect, 7) == False
    
    # Large matrix
    matrix_large = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    assert search_matrix(matrix_large, 12) == True
    assert search_matrix(matrix_large, 17) == False