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
    
    # Handle empty or single-element lists
    if len(arr) <= 1:
        return arr.copy()
    
    # Create a copy to avoid modifying the original list
    working_list = arr.copy()
    
    # Seed the random generator for reproducibility
    random.seed(42)
    
    # Track number of attempts to prevent infinite loops
    max_attempts = max(1000, len(working_list) ** 4)
    attempts = 0
    
    # Continue shuffling until the list is sorted
    while not is_sorted(working_list) and attempts < max_attempts:
        # Create a new shuffled version, ensuring it's different from previous attempts
        candidate = working_list.copy()
        random.shuffle(candidate)
        
        # Check if the shuffled list is different from the previous list
        if candidate != working_list:
            working_list = candidate
        
        attempts += 1
    
    # Check if sorting was successful
    if not is_sorted(working_list):
        # If we can't sort after max attempts, return the original list
        return sorted(arr)
    
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