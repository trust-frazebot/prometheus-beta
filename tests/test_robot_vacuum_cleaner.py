import pytest
from src.robot_vacuum_cleaner import cleanRoom

def test_basic_room_cleaning():
    """Test cleaning a simple room with no obstacles"""
    grid = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    # Test from different starting positions and directions
    assert cleanRoom(grid, 1, 1, 0) == 8  # Minimum steps to clean all cells
    assert cleanRoom(grid, 0, 0, 1) == 8  # Different start position
    assert cleanRoom(grid, 2, 2, 3) == 8  # Different start position and direction

def test_room_with_obstacles():
    """Test cleaning a room with obstacles"""
    grid = [
        [0, 0, 0],
        [1, 1, 0],
        [0, 0, 0]
    ]
    # Obstacles should not be counted in steps
    assert cleanRoom(grid, 0, 0, 0) == 6  # Fewer steps due to obstacles

def test_single_cell_room():
    """Test cleaning a single-cell room"""
    grid = [[0]]
    assert cleanRoom(grid, 0, 0, 0) == 0  # Already at final state

def test_error_handling():
    """Test error cases"""
    # Empty grid
    with pytest.raises(ValueError, match="Grid cannot be empty"):
        cleanRoom([], 0, 0, 0)
    
    # Out of bounds starting position
    grid = [[0, 0], [0, 0]]
    with pytest.raises(ValueError, match="Starting position is out of grid bounds"):
        cleanRoom(grid, 2, 0, 0)
    
    # Invalid direction
    with pytest.raises(ValueError, match="Invalid direction"):
        cleanRoom(grid, 0, 0, 4)

def test_obstacle_starting_position():
    """Test starting on an obstacle"""
    grid = [
        [0, 0, 0],
        [1, 1, 1],
        [0, 0, 0]
    ]
    # Starting on an obstacle should return 0 steps
    assert cleanRoom(grid, 1, 0, 0) == 0
    assert cleanRoom(grid, 1, 1, 0) == 0
    assert cleanRoom(grid, 1, 2, 0) == 0

def test_complex_room_layout():
    """Test a more complex room layout"""
    grid = [
        [0, 0, 1, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 1],
        [1, 0, 0, 0]
    ]
    # Verify step counting with various obstacles
    result = cleanRoom(grid, 0, 0, 1)
    assert result > 0  # Should require some steps
    assert result < 16  # Total cell count