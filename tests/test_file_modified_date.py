import os
import pytest
from datetime import datetime
import time
from src.file_modified_date import get_file_last_modified_date

def test_get_file_last_modified_date_normal():
    # Create a temporary file
    test_file_path = 'tests/test_temp_file.txt'
    with open(test_file_path, 'w') as f:
        f.write('Test content')
    
    # Get the last modified date
    modified_date = get_file_last_modified_date(test_file_path)
    
    # Verify it's a datetime and recent
    assert isinstance(modified_date, datetime)
    assert datetime.now().timestamp() - modified_date.timestamp() < 10  # within 10 seconds
    
    # Clean up
    os.remove(test_file_path)

def test_get_file_last_modified_date_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        get_file_last_modified_date('non_existent_file.txt')

def test_get_file_last_modified_date_invalid_input():
    with pytest.raises(TypeError):
        get_file_last_modified_date(123)  # non-string input

def test_get_file_last_modified_date_directory():
    with pytest.raises(ValueError):
        get_file_last_modified_date('tests')  # directory instead of file

def test_get_file_last_modified_date_after_modification():
    # Create a temporary file
    test_file_path = 'tests/test_modified_file.txt'
    with open(test_file_path, 'w') as f:
        f.write('Initial content')
    
    # Wait a bit to ensure timestamp changes
    time.sleep(1)
    
    # Modify the file
    with open(test_file_path, 'w') as f:
        f.write('Modified content')
    
    # Get the last modified date
    modified_date = get_file_last_modified_date(test_file_path)
    
    # Verify it's a datetime and very recent
    assert isinstance(modified_date, datetime)
    assert datetime.now().timestamp() - modified_date.timestamp() < 10  # within 10 seconds
    
    # Clean up
    os.remove(test_file_path)