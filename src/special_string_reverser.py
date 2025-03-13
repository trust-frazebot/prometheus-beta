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
    
    # Special handling for complete numeric string
    if input_string.isdigit():
        return input_string[::-1]
    
    # Prepare for token processing
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
    
    # Work through the tokens
    processed_tokens = []
    current_word = ""
    current_integer = ""
    
    for char in input_string:
        if char.isalpha():
            # If we had an integer token, process it
            if current_integer:
                processed_tokens.append(current_integer[::-1])
                current_integer = ""
            # Build word
            current_word += char
        elif char.isdigit():
            # If we had a word token, process it
            if current_word:
                processed_tokens.append(current_word[::-1])
                current_word = ""
            # Build integer
            current_integer += char
        else:
            # Process any existing word or integer
            if current_word:
                processed_tokens.append(current_word[::-1])
                current_word = ""
            if current_integer:
                processed_tokens.append(current_integer[::-1])
                current_integer = ""
            # Add non-alphanumeric token
            processed_tokens.append(char)
    
    # Process last tokens if they exist
    if current_word:
        processed_tokens.append(current_word[::-1])
    if current_integer:
        processed_tokens.append(current_integer[::-1])
    
    return ''.join(processed_tokens)