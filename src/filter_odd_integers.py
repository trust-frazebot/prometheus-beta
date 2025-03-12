def filter_and_sort_odd_integers(numbers):
    """
    Filter a list of integers to return only odd integers, sorted in ascending order.

    Args:
        numbers (list): A list of integers to filter and sort.

    Returns:
        list: A new list containing only the odd integers from the input list, 
              sorted in ascending order.

    Examples:
        >>> filter_and_sort_odd_integers([1, 2, 3, 4, 5, 6, 7, 8, 9])
        [1, 3, 5, 7, 9]
        >>> filter_and_sort_odd_integers([2, 4, 6, 8])
        []
        >>> filter_and_sort_odd_integers([])
        []
    """
    # Filter only odd numbers and sort them in ascending order
    return sorted([num for num in numbers if num % 2 != 0])