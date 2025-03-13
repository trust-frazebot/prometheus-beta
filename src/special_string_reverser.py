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
    
    # If the entire string is a palindrome, return it as-is
    if input_string == input_string[::-1]:
        return input_string
    
    # Track the reversal state for each token
    tokens = []
    current_token = ""
    
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
    
    for char in input_string:
        # If character is alphanumeric, add to current token
        if char.isalnum():
            current_token += char
        else:
            # Process and add current token before non-alphanumeric char
            if current_token:
                # Determine how to process the token
                if is_palindrome(current_token):
                    tokens.append(current_token)
                elif is_integer(current_token):
                    tokens.append(current_token[::-1])
                elif is_word(current_token):
                    tokens.append(current_token[::-1])
                else:
                    tokens.append(current_token)
                current_token = ""
            # Add non-alphanumeric character as-is
            tokens.append(char)
    
    # Process the last token if exists
    if current_token:
        # Determine how to process the token
        if is_palindrome(current_token):
            tokens.append(current_token)
        elif is_integer(current_token):
            tokens.append(current_token[::-1])
        elif is_word(current_token):
            tokens.append(current_token[::-1])
        else:
            tokens.append(current_token)
    
    # Join and return the processed tokens
    return ''.join(tokens)