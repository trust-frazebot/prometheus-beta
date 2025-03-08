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
    longest_substring = ""
    current_substring = ""
    
    for char in s:
        # If character is already in current substring, 
        # reset current substring to start after the first occurrence
        if char in current_substring:
            # Find the index of the first occurrence
            index = current_substring.index(char)
            current_substring = current_substring[index+1:] + char
        else:
            current_substring += char
        
        # Update longest substring if current is longer
        if len(current_substring) > len(longest_substring):
            longest_substring = current_substring
    
    return longest_substring