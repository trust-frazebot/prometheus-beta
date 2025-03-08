import pytest
from src.rotate_and_reverse import rotate_and_reverse

def test_basic_rotation_and_reversal():
    """Test basic rotation and reversal functionality"""
    assert rotate_and_reverse("hello", 2) == "loleh"

def test_no_rotation():
    """Test when rotations is zero"""
    assert rotate_and_reverse("hello", 0) == "olleh"

def test_full_string_rotation():
    """Test rotation equal to string length"""
    assert rotate_and_reverse("hello", 5) == "olleh"

def test_rotation_greater_than_length():
    """Test rotation greater than string length"""
    assert rotate_and_reverse("hello", 7) == "loleh"

def test_empty_string():
    """Test empty string input"""
    assert rotate_and_reverse("", 3) == ""

def test_single_character():
    """Test single character string"""
    assert rotate_and_reverse("a", 10) == "a"

def test_invalid_string_type():
    """Test non-string input for string argument"""
    with pytest.raises(TypeError, match="Input 'string' must be a string"):
        rotate_and_reverse(123, 2)

def test_invalid_rotations_type():
    """Test non-integer input for rotations argument"""
    with pytest.raises(TypeError, match="Input 'rotations' must be an integer"):
        rotate_and_reverse("hello", "2")

def test_negative_rotations():
    """Test negative number of rotations"""
    with pytest.raises(ValueError, match="Number of rotations cannot be negative"):
        rotate_and_reverse("hello", -1)