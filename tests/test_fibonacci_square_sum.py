import pytest
import math
from src.fibonacci_square_sum import generate_fibonacci_square_sum_sequence, is_perfect_square

def test_is_perfect_square():
    # Test perfect squares
    assert is_perfect_square(0) == True
    assert is_perfect_square(1) == True
    assert is_perfect_square(4) == True
    assert is_perfect_square(9) == True
    assert is_perfect_square(16) == True
    
    # Test non-perfect squares
    assert is_perfect_square(2) == False
    assert is_perfect_square(3) == False
    assert is_perfect_square(7) == False
    assert is_perfect_square(15) == False

def test_generate_sequence_basic():
    # Test basic sequence generation
    sequence = generate_fibonacci_square_sum_sequence(5)
    assert len(sequence) == 5
    
    # Verify that consecutive pair sums are perfect squares
    for i in range(len(sequence) - 2):
        assert is_perfect_square(sequence[i] + sequence[i+1]), \
            f"Sum of {sequence[i]} and {sequence[i+1]} is not a perfect square"

def test_generate_sequence_length():
    # Test different sequence lengths
    for length in [2, 3, 5, 10]:
        sequence = generate_fibonacci_square_sum_sequence(length)
        assert len(sequence) == length

def test_invalid_inputs():
    # Test invalid input types
    with pytest.raises(TypeError):
        generate_fibonacci_square_sum_sequence("3")
    with pytest.raises(TypeError):
        generate_fibonacci_square_sum_sequence(3.5)
    
    # Test invalid sequence lengths
    with pytest.raises(ValueError):
        generate_fibonacci_square_sum_sequence(0)
    with pytest.raises(ValueError):
        generate_fibonacci_square_sum_sequence(1)

def test_sequence_properties():
    # More detailed checks of sequence properties
    sequence = generate_fibonacci_square_sum_sequence(7)
    
    # Check that consecutive pairs have square sums
    for i in range(len(sequence) - 2):
        pair_sum = sequence[i] + sequence[i+1]
        sqrt_sum = int(math.sqrt(pair_sum))
        assert sqrt_sum * sqrt_sum == pair_sum, \
            f"Sum of {sequence[i]} and {sequence[i+1]} ({pair_sum}) is not a perfect square"