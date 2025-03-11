import os
import pytest
from src.write_string_to_file import write_string_to_file

def test_write_string_to_file_success(tmp_path):
    """Test successful file writing"""
    test_file = tmp_path / "test_file.txt"
    test_content = "Hello, world!"
    
    write_string_to_file(test_content, str(test_file))
    
    with open(test_file, 'r') as file:
        assert file.read() == test_content

def test_write_string_to_file_overwrite(tmp_path):
    """Test overwriting an existing file"""
    test_file = tmp_path / "test_file.txt"
    
    # Write first content
    write_string_to_file("First content", str(test_file))
    
    # Overwrite with new content
    new_content = "New content"
    write_string_to_file(new_content, str(test_file))
    
    with open(test_file, 'r') as file:
        assert file.read() == new_content

def test_write_string_to_file_invalid_input_types():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError, match="Content must be a string"):
        write_string_to_file(123, "file.txt")
    
    with pytest.raises(TypeError, match="File path must be a string"):
        write_string_to_file("content", 123)

def test_write_string_to_file_empty_inputs():
    """Test error handling for empty inputs"""
    with pytest.raises(ValueError, match="Content cannot be an empty string"):
        write_string_to_file("", "file.txt")
    
    with pytest.raises(ValueError, match="File path cannot be an empty string"):
        write_string_to_file("content", "")

def test_write_string_to_file_non_existent_directory(tmp_path):
    """Test writing to a file in a non-existent directory"""
    non_existent_dir = tmp_path / "non_existent_dir"
    test_file = non_existent_dir / "test_file.txt"
    
    # This should raise an IOError due to directory not existing
    with pytest.raises(IOError):
        write_string_to_file("content", str(test_file))