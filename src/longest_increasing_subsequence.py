def longest_increasing_subsequence_length(arr):
    """
    Find the length of the longest continuous increasing subsequence in an array.
    
    A continuous increasing subsequence is a sequence of integers where each number 
    is strictly greater than the previous number.
    
    Args:
        arr (list): A list of integers to analyze
    
    Returns:
        int: Length of the longest continuous increasing subsequence
    
    Examples:
        >>> longest_increasing_subsequence_length([1,3,5,4,7])
        3
        >>> longest_increasing_subsequence_length([2,2,2,2])
        1
        >>> longest_increasing_subsequence_length([])
        0
    """
    # Handle empty array case
    if not arr:
        return 0
    
    # Initialize variables to track current and max subsequence lengths
    current_length = 1
    max_length = 1
    
    # Iterate through the array starting from the second element
    for i in range(1, len(arr)):
        # If current element is greater than previous, extend current subsequence
        if arr[i] > arr[i-1]:
            current_length += 1
        else:
            # Reset current subsequence length
            current_length = 1
        
        # Update max length 
        max_length = max(max_length, current_length)
    
    return max_length