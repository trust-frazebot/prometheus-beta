import pytest
from src.unique_coordinate_combinations import get_unique_coordinate_combinations

def test_basic_coordinate_combinations():
    """Test basic functionality with simple coordinate pairs."""
    coordinates = [(1, 2), (3, 4), (1, 4), (3, 2)]
    expected = [[1, 2], [1, 4], [3, 2], [3, 4]]
    assert get_unique_coordinate_combinations(coordinates) == expected

def test_duplicate_coordinates():
    """Test handling of duplicate coordinate pairs."""
    coordinates = [(1, 1), (1, 1), (2, 2), (2, 2)]
    expected = [[1, 1], [1, 2], [2, 1], [2, 2]]
    assert get_unique_coordinate_combinations(coordinates) == expected

def test_negative_coordinates():
    """Test handling of negative coordinate values."""
    coordinates = [(-1, 2), (3, -4), (-1, -4)]
    expected = [[-1, -4], [-1, 2], [3, -4], [3, 2]]
    assert get_unique_coordinate_combinations(coordinates) == expected

def test_float_coordinates():
    """Test handling of float coordinate values."""
    coordinates = [(1.5, 2.5), (3.5, 4.5)]
    expected = [[1.5, 2.5], [1.5, 4.5], [3.5, 2.5], [3.5, 4.5]]
    assert get_unique_coordinate_combinations(coordinates) == expected

def test_empty_list():
    """Test behavior with an empty list of coordinates."""
    coordinates = []
    expected = []
    assert get_unique_coordinate_combinations(coordinates) == expected

def test_invalid_input_type():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError, match="Input must be a list of coordinate pairs"):
        get_unique_coordinate_combinations("not a list")

def test_invalid_coordinate_pair():
    """Test error handling for invalid coordinate pairs."""
    with pytest.raises(TypeError, match="Each coordinate must be a pair"):
        get_unique_coordinate_combinations([(1, 2), "invalid"])

def test_non_numeric_coordinates():
    """Test error handling for non-numeric coordinates."""
    with pytest.raises(ValueError, match="Coordinates must be numeric"):
        get_unique_coordinate_combinations([(1, "a"), (2, 3)])