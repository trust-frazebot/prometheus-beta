def alternating_title_case(input_string):
    """
    Convert a string to alternating title case.
    
    Args:
        input_string (str): The input string to be converted.
    
    Returns:
        str: A string with words alternating between title case and lowercase.
    
    Raises:
        TypeError: If input is not a string.
    
    Examples:
        >>> alternating_title_case("hello world python")
        'Hello world Python'
        >>> alternating_title_case("this is a test")
        'This is A test'
        >>> alternating_title_case("")
        ''
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string case
    if not input_string:
        return ""
    
    # Split the string into words
    words = input_string.split()
    
    # Apply alternating title case
    converted_words = [
        word.title() if idx % 2 == 0 else word.lower()
        for idx, word in enumerate(words)
    ]
    
    # Join the words back together
    return ' '.join(converted_words)