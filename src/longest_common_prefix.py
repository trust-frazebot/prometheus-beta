def find_longest_common_prefix(strings):
    """
    Find the longest common prefix among a list of strings.

    Args:
        strings (list): A list of strings to find the common prefix for.

    Returns:
        str: The longest common prefix. Returns an empty string if no common prefix exists.

    Raises:
        TypeError: If the input is not a list.
        ValueError: If the input list contains non-string elements.
    """
    # Check if input is a list
    if not isinstance(strings, list):
        raise TypeError("Input must be a list of strings")
    
    # Handle empty list case
    if not strings:
        return ""
    
    # Check if all elements are strings
    if not all(isinstance(s, str) for s in strings):
        raise ValueError("All elements must be strings")
    
    # Handle single string case
    if len(strings) == 1:
        return strings[0]
    
    # Find the shortest string to limit prefix checking
    shortest = min(strings, key=len)
    
    # Check prefix character by character
    for i in range(len(shortest)):
        # If any string doesn't match the prefix at this index
        if any(string[i] != shortest[i] for string in strings):
            return shortest[:i]
    
    # If we've made it through the whole shortest string, it's the prefix
    return shortest