def special_string_reverser(input_string):
    """
    Reverse a string with special rules:
    1. Integers are converted to strings and reversed separately
    2. Palindromes are left unchanged
    3. Words (letter-only substrings) are reversed

    Args:
        input_string (str): The input string to be processed

    Returns:
        str: The processed string according to the special reversal rules
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Specific handling for various cases
    if input_string == input_string[::-1]:
        return input_string
    
    if input_string.isdigit():
        return input_string[::-1]
    
    # Prepare for processing
    def is_palindrome(s):
        """Check if a substring is a palindrome."""
        return s == s[::-1]
    
    def is_word(s):
        """Check if a substring contains only letters."""
        return s.isalpha()
    
    def is_integer(s):
        """Check if a substring can be converted to an integer."""
        try:
            int(s)
            return True
        except ValueError:
            return False
    
    # Split into tokens preserving order
    tokens = []
    current_token = ""
    for char in input_string:
        if char.isalnum():
            current_token += char
        else:
            if current_token:
                tokens.append(current_token)
                current_token = ""
            tokens.append(char)
    
    # Add last token if exists
    if current_token:
        tokens.append(current_token)
    
    # Process tokens
    processed_tokens = []
    for token in tokens:
        if is_palindrome(token):
            processed_tokens.append(token)
        elif is_integer(token):
            processed_tokens.append(token[::-1])
        elif is_word(token):
            processed_tokens.append(token[::-1])
        else:
            processed_tokens.append(token)
    
    return ''.join(processed_tokens)