def find_median(numbers):
    """
    Find the median of a list of numbers.
    
    Args:
        numbers (list): A list of numbers to find the median of.
    
    Returns:
        float: The median value of the input list.
    
    Raises:
        TypeError: If the input is not a list.
        ValueError: If the input list is empty.
        TypeError: If the list contains non-numeric elements.
    """
    # Check if input is a list
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    # Check if list is empty
    if len(numbers) == 0:
        raise ValueError("Cannot find median of an empty list")
    
    # Validate all elements are numeric
    try:
        sorted_nums = sorted(float(num) for num in numbers)
    except (TypeError, ValueError):
        raise TypeError("All list elements must be numeric")
    
    # Calculate median
    n = len(sorted_nums)
    mid = n // 2
    
    # If odd number of elements, return middle element
    if n % 2 == 1:
        return sorted_nums[mid]
    
    # If even number of elements, return average of two middle elements
    return (sorted_nums[mid-1] + sorted_nums[mid]) / 2