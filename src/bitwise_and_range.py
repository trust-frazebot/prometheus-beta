def bitwise_and_range(m: int, n: int) -> int:
    """
    Calculate the bitwise AND of all numbers in the range [m, n].
    
    Args:
        m (int): The lower bound of the range (inclusive)
        n (int): The upper bound of the range (inclusive)
    
    Returns:
        int: The bitwise AND of all numbers in the range
    
    Raises:
        ValueError: If m or n is negative or m > n
    
    Examples:
        >>> bitwise_and_range(5, 7)
        4
        >>> bitwise_and_range(0, 3)
        0
    """
    # Validate input
    if m < 0 or n < 0:
        raise ValueError("Both m and n must be non-negative integers")
    
    if m > n:
        raise ValueError("m must be less than or equal to n")
    
    # If range is zero, return the single number
    if m == n:
        return m
    
    # Find the most significant bit position where m and n differ
    shift = 0
    while m != n:
        m >>= 1
        n >>= 1
        shift += 1
    
    # Left shift the common prefix back
    return m << shift