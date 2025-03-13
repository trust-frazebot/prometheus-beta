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
    
    # Whole string handling
    if input_string.isdigit():
        return input_string[::-1]
    
    # Prepare for multistep processing
    def process_tokens(tokens):
        # Process each token
        processed_tokens = []
        for token in tokens:
            if token.isalpha():
                processed_tokens.append(token[::-1])
            elif token.isdigit():
                processed_tokens.append(token[::-1])
            else:
                processed_tokens.append(token)
        return processed_tokens
    
    # Split tokens
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
    processed_tokens = process_tokens(tokens)
    
    # Return the result
    return ''.join(processed_tokens)