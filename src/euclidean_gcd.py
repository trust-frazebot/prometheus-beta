def euclidean_gcd(a: int, b: int) -> int:
    """
    Compute the Greatest Common Divisor (GCD) of two integers using the Euclidean algorithm.
    
    The Euclidean algorithm is based on the principle that the greatest common divisor 
    of two numbers does not change if the smaller number is subtracted from the larger number.
    
    Args:
        a (int): First non-negative integer
        b (int): Second non-negative integer
    
    Returns:
        int: The greatest common divisor of a and b
    
    Raises:
        ValueError: If either input is negative
        TypeError: If inputs are not integers
    """
    # Type checking
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Inputs must be integers")
    
    # Handle negative input
    if a < 0 or b < 0:
        raise ValueError("Inputs must be non-negative integers")
    
    # Handle zero cases
    if a == 0:
        return b
    if b == 0:
        return a
    
    # Euclidean algorithm implementation
    while b != 0:
        a, b = b, a % b
    
    return a