def get_unique_coordinate_combinations(coordinate_pairs):
    """
    Generate a list of unique x and y values from coordinate pairs in ascending order.

    Args:
        coordinate_pairs (list): A list of coordinate pairs [(x1, y1), (x2, y2), ...]

    Returns:
        list: A list of unique [x, y] combinations sorted in ascending order

    Raises:
        TypeError: If input is not a list or contains invalid coordinate pairs
        ValueError: If coordinate pairs are not valid (must be numeric)
    """
    # Validate input
    if not isinstance(coordinate_pairs, list):
        raise TypeError("Input must be a list of coordinate pairs")
    
    # Check for valid coordinate pairs
    for pair in coordinate_pairs:
        if not (isinstance(pair, (list, tuple)) and len(pair) == 2):
            raise TypeError("Each coordinate must be a pair (list or tuple)")
        if not (isinstance(pair[0], (int, float)) and isinstance(pair[1], (int, float))):
            raise ValueError("Coordinates must be numeric")
    
    # Extract unique x and y values
    x_values = sorted(set(pair[0] for pair in coordinate_pairs))
    y_values = sorted(set(pair[1] for pair in coordinate_pairs))
    
    # Generate unique combinations
    unique_combinations = [[x, y] for x in x_values for y in y_values]
    
    return unique_combinations