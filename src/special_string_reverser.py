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
    
    # If the entire string is a palindrome, return it as-is
    if is_palindrome(input_string):
        return input_string
    
    # Split the string into tokens
    tokens = []
    current_token = ""
    
    for char in input_string:
        # If character is alphanumeric, add to current token
        if char.isalnum():
            current_token += char
        else:
            # Add non-empty token before adding non-alphanumeric character
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
            # Leave palindromes unchanged
            processed_tokens.append(token)
        elif is_integer(token):
            # Reverse integers as strings
            processed_tokens.append(token[::-1])
        elif is_word(token):
            # Reverse words
            processed_tokens.append(token[::-1])
        else:
            # Non-alphanumeric or mixed tokens remain unchanged
            processed_tokens.append(token)
    
    # Join processed tokens
    return ''.join(processed_tokens)