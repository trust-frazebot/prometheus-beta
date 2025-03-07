def lz77_compress(data):
    """
    Implement the LZ77 compression algorithm.
    
    Args:
        data (str or bytes): The input data to compress.
    
    Returns:
        list: A list of tuples representing compressed data, where each tuple is 
              (offset, length, next_char):
              - offset: distance to the previous occurrence of a substring
              - length: length of the matched substring
              - next_char: the next character after the matched substring
    
    Raises:
        TypeError: If input is not a string or bytes-like object.
    """
    # Convert input to bytes if it's a string
    if isinstance(data, str):
        data = data.encode('utf-8')
    
    # Validate input type
    if not isinstance(data, (bytes, bytearray)):
        raise TypeError("Input must be a string or bytes-like object")
    
    # If input is empty, return empty list
    if not data:
        return []
    
    # Compression result
    compressed = []
    
    # Sliding window parameters
    window_size = 4096  # Typical sliding window size
    look_ahead_buffer_size = 16  # Typical look-ahead buffer size
    
    # Indexes
    current_index = 0
    
    while current_index < len(data):
        # Find the longest match in the sliding window
        best_length = 0
        best_offset = 0
        
        # Calculate start of search window (don't go before beginning of data)
        search_start = max(0, current_index - window_size)
        
        # Look for the longest match
        for offset in range(current_index - search_start):
            match_length = 0
            
            # Try to extend the match
            while (match_length < look_ahead_buffer_size and 
                   current_index + match_length < len(data) and 
                   data[current_index - offset + match_length - 1] == 
                   data[current_index + match_length]):
                match_length += 1
            
            # Update best match if found
            if match_length > best_length:
                best_length = match_length
                best_offset = offset + 1
        
        # If no match found, encode as literal
        if best_length == 0:
            compressed.append((0, 0, data[current_index]))
            current_index += 1
        else:
            # Encode the match and the next character
            next_char = data[current_index + best_length] if current_index + best_length < len(data) else None
            compressed.append((best_offset, best_length, next_char))
            current_index += best_length + 1
    
    return compressed

def lz77_decompress(compressed_data):
    """
    Decompress data compressed with the LZ77 algorithm.
    
    Args:
        compressed_data (list): Compressed data in the format of 
                                [(offset, length, next_char), ...]
    
    Returns:
        bytes: Decompressed data
    
    Raises:
        TypeError: If input is not a list
        ValueError: If compressed data is malformed
    """
    # Validate input
    if not isinstance(compressed_data, list):
        raise TypeError("Input must be a list of compression tuples")
    
    # If input is empty, return empty bytes
    if not compressed_data:
        return b''
    
    # Decompression result
    decompressed = bytearray()
    
    for offset, length, next_char in compressed_data:
        # Handle literal character (no offset)
        if offset == 0 and length == 0:
            if next_char is None:
                raise ValueError("Literal must have a character")
            decompressed.append(next_char)
        else:
            # Validate match parameters
            if offset <= 0 or length < 0:
                raise ValueError(f"Invalid match: offset={offset}, length={length}")
            
            # Copy matched substring
            start = len(decompressed) - offset
            for i in range(length):
                if start + i < 0:
                    raise ValueError("Invalid match: start index out of bounds")
                decompressed.append(decompressed[start + i])
            
            # Append next character if exists
            if next_char is not None:
                decompressed.append(next_char)
    
    return bytes(decompressed)