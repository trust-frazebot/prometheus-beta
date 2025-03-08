from typing import List, Tuple

def find_longest_increasing_subsequence(arr: List[int]) -> Tuple[int, List[int]]:
    """
    Find the longest increasing subsequence in the given array.
    
    Args:
        arr (List[int]): Input array of integers
    
    Returns:
        Tuple[int, List[int]]: A tuple containing:
        - Length of the longest increasing subsequence
        - The actual longest increasing subsequence
    
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    
    Edge Cases:
    - Empty array returns (0, [])
    - Single element array returns (1, [that element])
    """
    # Handle edge cases
    if not arr:
        return 0, []
    
    # Length of the input array
    n = len(arr)
    
    # Dynamic programming arrays
    # lengths[i] stores the length of LIS ending at index i
    lengths = [1] * n
    
    # predecessors to track the actual subsequence
    predecessors = [None] * n
    
    # Variables to track the overall longest subsequence
    max_length = 1
    max_index = 0
    
    # Compute longest increasing subsequence
    for i in range(1, n):
        for j in range(i):
            # If current element can extend the previous subsequence
            if arr[i] > arr[j] and lengths[i] < lengths[j] + 1:
                # Specifically verify the strictly increasing condition
                if predecessors[j] is None or arr[predecessors[j]] < arr[i]:
                    lengths[i] = lengths[j] + 1
                    predecessors[i] = j
        
        # Update the max length and index if needed
        if lengths[i] > max_length:
            max_length = lengths[i]
            max_index = i
    
    # Reconstruct the subsequence
    subsequence = []
    current = max_index
    while current is not None:
        subsequence.insert(0, arr[current])
        current = predecessors[current]
    
    return max_length, subsequence