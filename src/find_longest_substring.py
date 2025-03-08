def find_longest_substring(s: str) -> str:
    """
    Find the longest substring with unique characters in the input string.
    
    Args:
        s (str): The input string to search for unique character substring.
    
    Returns:
        str: The longest substring with unique characters.
             If multiple such substrings exist with the same length, 
             returns the first occurrence from left to right.
    
    Examples:
        >>> find_longest_substring("abcabcbb")
        'abc'
        >>> find_longest_substring("bbbbb")
        'b'
        >>> find_longest_substring("")
        ''
    """
    # Handle empty string edge case
    if not s:
        return ""
    
    # Initialize variables to track the longest unique substring
    start = 0
    char_map = {}
    longest_start = 0
    longest_length = 0
    
    for end, char in enumerate(s):
        # If character is already seen, update start pointer
        if char in char_map and char_map[char] >= start:
            start = char_map[char] + 1
        else:
            # Update longest substring if current is longer
            if end - start + 1 > longest_length:
                longest_start = start
                longest_length = end - start + 1
        
        # Always update the last seen position of the character
        char_map[char] = end
    
    return s[longest_start:longest_start+longest_length]