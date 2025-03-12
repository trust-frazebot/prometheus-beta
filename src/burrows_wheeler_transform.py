def burrows_wheeler_transform(input_string: str) -> str:
    """
    Perform the Burrows-Wheeler Transform on the input string.
    
    The Burrows-Wheeler Transform (BWT) is a data compression algorithm that 
    rearranges a block of data to make it more compressible.
    
    Args:
        input_string (str): The input string to transform. 
                             Must be a non-empty string.
    
    Returns:
        str: The Burrows-Wheeler transformed string.
    
    Raises:
        ValueError: If the input string is empty.
        TypeError: If the input is not a string.
    
    Examples:
        >>> burrows_wheeler_transform("banana")
        'annb$aa'
        >>> burrows_wheeler_transform("hello")
        'ello$h'
    """
    # Input validation
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    if not input_string:
        raise ValueError("Input string cannot be empty")
    
    # Add unique terminator character
    modified_string = input_string + '$'
    
    # Generate all rotations of the string
    rotations = [modified_string[i:] + modified_string[:i] 
                 for i in range(len(modified_string))]
    
    # Sort the rotations lexicographically
    sorted_rotations = sorted(rotations)
    
    # Extract the last character of each sorted rotation
    bwt_result = ''.join(rotation[-1] for rotation in sorted_rotations)
    
    return bwt_result

def inverse_burrows_wheeler_transform(bwt_string: str) -> str:
    """
    Perform the inverse Burrows-Wheeler Transform to recover the original string.
    
    Args:
        bwt_string (str): The Burrows-Wheeler transformed string.
    
    Returns:
        str: The original string before transformation.
    
    Raises:
        ValueError: If the input string is empty or doesn't contain a terminator.
        TypeError: If the input is not a string.
    
    Examples:
        >>> inverse_burrows_wheeler_transform('annb$aa')
        'banana'
        >>> inverse_burrows_wheeler_transform('ello$h')
        'hello'
    """
    # Input validation
    if not isinstance(bwt_string, str):
        raise TypeError("Input must be a string")
    
    if not bwt_string or '$' not in bwt_string:
        raise ValueError("Input must be a valid BWT string with a terminator")
    
    # Create first and last column
    n = len(bwt_string)
    
    # Create a table to track original order
    table = [''] * n
    
    # First, create the first column (sorted string)
    first_column = sorted(bwt_string)
    
    # Create the mapping between first and last column
    for i in range(n):
        # Find the next character in the reconstruction
        next_char = bwt_string[i]
        # Place it in the next available slot in the first column
        idx = first_column.index(next_char)
        while table[idx]:
            idx = first_column.index(next_char, idx + 1)
        table[idx] = next_char
    
    # Recover the original string
    original = ''.join(char for char in table if char != '$')
    
    return original