import pytest
from src.staircase_climbing import climb_stairs

def test_staircase_base_cases():
    """Test base cases with 0 and 1 steps."""
    assert climb_stairs(0) == 1  # One way to climb 0 steps (do nothing)
    assert climb_stairs(1) == 1  # One way to climb 1 step

def test_staircase_known_values():
    """Test staircase climbing for known number of steps."""
    assert climb_stairs(2) == 2   # Ways: [1,1], [2]
    assert climb_stairs(3) == 3   # Ways: [1,1,1], [1,2], [2,1]
    assert climb_stairs(4) == 5   # Ways: [1,1,1,1], [1,1,2], [1,2,1], [2,1,1], [2,2]
    assert climb_stairs(5) == 8   # Verified Fibonacci sequence

def test_larger_staircases():
    """Test larger staircases to verify expected growth."""
    assert climb_stairs(10) == 89
    assert climb_stairs(15) == 987

def test_negative_steps_raise_error():
    """Ensure negative steps raise a ValueError."""
    with pytest.raises(ValueError, match="Number of steps must be non-negative"):
        climb_stairs(-1)

def test_type_error():
    """Ensure non-integer inputs raise a TypeError."""
    with pytest.raises(TypeError):
        climb_stairs("not an integer")
    with pytest.raises(TypeError):
        climb_stairs(3.14)