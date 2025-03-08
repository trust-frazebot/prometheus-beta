def sort_nums(numbers):
    """
    Initial sorting function with a known bug.
    
    This function uses bubble sort with an intentional inefficiency.
    
    Args:
        numbers (list): A list of numbers to be sorted.
    
    Returns:
        list: A sorted list of numbers (potentially with a bug).
    """
    n = len(numbers)
    for i in range(n):
        # Intentional bug: Always compares adjacent elements, 
        # even when no swap is needed
        for j in range(0, n-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers

def optimal_sort(numbers):
    """
    Improved sorting function with better time complexity.
    
    Uses Python's built-in sorted() function which implements 
    Timsort - a hybrid sorting algorithm derived from merge sort 
    and insertion sort with O(n log n) time complexity.
    
    Args:
        numbers (list): A list of numbers to be sorted.
    
    Returns:
        list: A sorted list of numbers.
    """
    return sorted(numbers)