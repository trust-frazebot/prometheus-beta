import random
from typing import List, TypeVar

T = TypeVar('T')

def bogosort(arr: List[T]) -> List[T]:
    """
    Implement the bogosort (permutation sort) algorithm.
    
    Bogosort is an extremely inefficient sorting algorithm that works by randomly 
    shuffling the input list until it becomes sorted. This implementation is 
    meant for educational purposes and should NEVER be used in production.
    
    Args:
        arr (List[T]): The input list to be sorted
    
    Returns:
        List[T]: A sorted version of the input list
    
    Raises:
        TypeError: If the input is not a list
        ValueError: If the list contains elements that cannot be compared
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Create a copy to avoid modifying the original list
    working_list = arr.copy()
    
    # Track number of attempts to prevent infinite loops
    max_attempts = 1000
    attempts = 0
    
    # Continue shuffling until the list is sorted
    while not is_sorted(working_list) and attempts < max_attempts:
        random.shuffle(working_list)
        attempts += 1
    
    # Check if sorting was successful
    if not is_sorted(working_list):
        raise RuntimeError("Failed to sort list within maximum attempts")
    
    return working_list

def is_sorted(arr: List[T]) -> bool:
    """
    Check if a list is sorted in ascending order.
    
    Args:
        arr (List[T]): The list to check for sortedness
    
    Returns:
        bool: True if the list is sorted, False otherwise
    """
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))