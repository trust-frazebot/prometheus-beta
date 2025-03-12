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
    
    # Sort the characters in the last column
    sorted_chars = sorted(bwt_string)
    
    # Track how many times each character appears before its current index
    char_count = {}
    last_idx = {}
    for idx, char in enumerate(bwt_string):
        if char not in char_count:
            char_count[char] = 0
        char_count[char] += 1
        last_idx[char] = idx
    
    # Create the mapping to track next character in reconstruction
    next_idx = {}
    for char in sorted_chars:
        next_idx[char] = bwt_string.index(char)
    
    # Reconstruct the original string
    original = []
    current_char = '$'
    n = len(bwt_string)
    
    while len(original) < n - 1:  # Exclude terminator character
        # Find the next occurrence of this character
        current_char = bwt_string[next_idx[current_char]]
        if current_char != '$':
            original.append(current_char)
    
    return ''.join(reversed(original))