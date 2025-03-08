def rotate_and_reverse(string: str, rotations: int) -> str:
    """
    Rotate a string a specified number of times and then reverse it.
    
    Args:
        string (str): The input string to rotate and reverse
        rotations (int): Number of times to rotate the string
    
    Returns:
        str: The rotated and reversed string
    
    Raises:
        TypeError: If inputs are not of the correct type
        ValueError: If rotations is negative
    """
    # Validate input types
    if not isinstance(string, str):
        raise TypeError("Input 'string' must be a string")
    
    if not isinstance(rotations, int):
        raise TypeError("Input 'rotations' must be an integer")
    
    # Handle negative rotations
    if rotations < 0:
        raise ValueError("Number of rotations cannot be negative")
    
    # Handle empty string or zero rotations
    if not string or rotations == 0:
        return string[::-1]
    
    # Normalize rotations to be within string length
    effective_rotations = rotations % len(string)
    
    # Perform rotation and reversal
    rotated_string = string[effective_rotations:] + string[:effective_rotations]
    return rotated_string[::-1]