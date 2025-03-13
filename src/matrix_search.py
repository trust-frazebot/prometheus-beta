def search_matrix(matrix, target):
    """
    Search for a target integer in an M x N matrix.
    
    Args:
        matrix (list[list[int]]): A 2D matrix of integers
        target (int): The integer to search for
    
    Returns:
        bool: True if the target exists in the matrix, False otherwise
    
    Time Complexity: O(m * n), where m is the number of rows and n is the number of columns
    Space Complexity: O(1) as we're using only iteration
    
    Edge Cases:
    - Empty matrix returns False
    - Matrix with empty rows returns False
    """
    # Check for empty matrix or empty rows
    if not matrix or not matrix[0]:
        return False
    
    # Iterate through each row and column
    for row in matrix:
        for num in row:
            if num == target:
                return True
    
    # Target not found
    return False