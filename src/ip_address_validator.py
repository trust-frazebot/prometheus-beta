def validate_single_digit_ip(ip_address: str) -> bool:
    """
    Validate if the input is a valid IP address with single-digit octets.
    
    Args:
        ip_address (str): The IP address string to validate
    
    Returns:
        bool: True if the IP address is valid, False otherwise
    
    Validates that:
    - The IP address has exactly 4 octets separated by dots
    - Each octet is a single digit (0-9)
    """
    # Check if the input is a string
    if not isinstance(ip_address, str):
        return False
    
    # Split the IP address into octets
    octets = ip_address.split('.')
    
    # Check if there are exactly 4 octets
    if len(octets) != 4:
        return False
    
    # Validate each octet
    for octet in octets:
        # Check if the octet is a single digit
        if (len(octet) != 1 or 
            not octet.isdigit() or 
            int(octet) < 0 or 
            int(octet) > 9):
            return False
    
    return True