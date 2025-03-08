from typing import List, Tuple

def cleanRoom(grid: List[List[int]], r: int, c: int, direction: int) -> int:
    """
    Clean a grid-based room and return the minimum number of steps required.
    
    Args:
    - grid (List[List[int]]): 2D grid representing the room 
      (0 = empty cell, 1 = obstacle)
    - r (int): Starting row position of the robot
    - c (int): Starting column position of the robot
    - direction (int): Initial facing direction (0: North, 1: East, 2: South, 3: West)
    
    Returns:
    - int: Minimum number of steps required to clean the entire room
    
    Raises:
    - ValueError: If input parameters are invalid
    """
    # Input validation
    if not grid or not grid[0]:
        raise ValueError("Grid cannot be empty")
    
    if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
        raise ValueError("Starting position is out of grid bounds")
    
    if direction < 0 or direction > 3:
        raise ValueError("Invalid direction. Must be 0, 1, 2, or 3")
    
    # Check if starting position is an obstacle
    if grid[r][c] == 1:
        return 0
    
    # Directions: North, East, South, West
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    # Track visited cells and total cleaned cells
    visited = set()
    total_clean_cells = sum(row.count(0) for row in grid)
    
    def is_valid_move(x: int, y: int) -> bool:
        """Check if move is within grid and not an obstacle"""
        return (0 <= x < len(grid) and 
                0 <= y < len(grid[0]) and 
                grid[x][y] == 0)
    
    def dfs(x: int, y: int, current_dir: int, steps: int) -> int:
        """
        Depth-first search to clean the room
        
        Args:
        - x (int): Current row
        - y (int): Current column
        - current_dir (int): Current direction
        - steps (int): Current number of steps
        
        Returns:
        - int: Minimum steps to clean the room
        """
        # Mark current cell as visited
        visited.add((x, y))
        
        # Try all 4 directions
        min_steps = float('inf')
        for i in range(4):
            # Calculate new direction and position
            new_dir = (current_dir + i) % 4
            dx, dy = directions[new_dir]
            new_x, new_y = x + dx, y + dy
            
            # If move is valid and not visited
            if is_valid_move(new_x, new_y) and (new_x, new_y) not in visited:
                # Recursive call
                result = dfs(new_x, new_y, new_dir, steps + 1)
                min_steps = min(min_steps, result)
        
        # If all cells are visited, return current steps
        return steps if len(visited) == total_clean_cells else min_steps
    
    # Start cleaning from initial position
    return dfs(r, c, direction, 0)