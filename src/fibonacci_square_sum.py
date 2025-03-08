import math

def is_perfect_square(num):
    """
    Check if a number is a perfect square.
    
    Args:
        num (int): Number to check for perfect square property.
    
    Returns:
        bool: True if the number is a perfect square, False otherwise.
    """
    root = int(math.sqrt(num))
    return root * root == num

def generate_fibonacci_square_sum_sequence(n):
    """
    Generate a Fibonacci-like sequence where the sum of consecutive pairs 
    is always a perfect square.
    
    Args:
        n (int): Number of elements to generate in the sequence.
    
    Returns:
        list: A list of n numbers where consecutive pair sums are perfect squares.
    
    Raises:
        ValueError: If n is less than 2.
    """
    # Validate input
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 2:
        raise ValueError("Sequence length must be at least 2")
    
    # Initialize the sequence
    sequence = [1, 1]
    
    # Generate the sequence
    while len(sequence) < n:
        # Get the last two numbers
        a, b = sequence[-2], sequence[-1]
        
        # Try potential next numbers
        for next_num in range(b + 1, b * 2 + 1):
            # Check if the sum of the last two numbers forms a perfect square
            if is_perfect_square(a + b):
                sequence.append(next_num)
                break
    
    return sequence[:n]