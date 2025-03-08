def climb_stairs(n: int) -> int:
    """
    Calculate the number of distinct ways to climb a staircase with n steps,
    where you can take either 1 or 2 steps at a time.

    This is a classic dynamic programming problem solved recursively 
    with memoization to improve time complexity.

    Args:
        n (int): Total number of steps in the staircase. Must be non-negative.

    Returns:
        int: Number of distinct ways to climb the staircase.

    Raises:
        ValueError: If n is negative.

    Examples:
        >>> climb_stairs(2)  # 2 ways: 1+1 or 2
        2
        >>> climb_stairs(3)  # 3 ways: 1+1+1, 1+2, 2+1
        3
    """
    # Validate input
    if n < 0:
        raise ValueError("Number of steps must be non-negative")
    
    # Memoization dictionary to store computed results
    memo = {}
    
    def _climb_recursive(steps: int) -> int:
        # Base cases
        if steps <= 1:
            return 1
        
        # Check if result is already memoized
        if steps in memo:
            return memo[steps]
        
        # Recursive calculation
        # Number of ways is sum of ways for (n-1) and (n-2) steps
        memo[steps] = _climb_recursive(steps - 1) + _climb_recursive(steps - 2)
        
        return memo[steps]
    
    return _climb_recursive(n)