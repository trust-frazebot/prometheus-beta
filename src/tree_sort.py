class TreeNode:
    """
    A class representing a node in a binary search tree for tree sort algorithm.
    
    Attributes:
        value: The value stored in the node
        left: Reference to the left child node
        right: Reference to the right child node
    """
    def __init__(self, value):
        """
        Initialize a TreeNode with a given value.
        
        Args:
            value: The value to be stored in the node
        """
        self.value = value
        self.left = None
        self.right = None

def tree_sort(arr):
    """
    Implement the tree sort algorithm to sort a list in ascending order.
    
    Tree sort works by:
    1. Creating a binary search tree from the input list
    2. Performing an in-order traversal to extract sorted elements
    
    Args:
        arr (list): The input list to be sorted
    
    Returns:
        list: A new sorted list in ascending order
    
    Raises:
        TypeError: If input is not a list
        ValueError: If list contains elements that cannot be compared
    
    Time Complexity: O(n log n) on average, O(n^2) in worst case
    Space Complexity: O(n)
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty list or single-element list
    if len(arr) <= 1:
        return arr.copy()
    
    # Create the root of the binary search tree
    root = None
    
    # Insert each element into the binary search tree
    for item in arr:
        root = insert_node(root, item)
    
    # Collect sorted elements via in-order traversal
    sorted_list = []
    in_order_traversal(root, sorted_list)
    
    return sorted_list

def insert_node(root, value):
    """
    Insert a value into the binary search tree.
    
    Args:
        root (TreeNode): The root of the current subtree
        value: The value to be inserted
    
    Returns:
        TreeNode: The root of the updated subtree
    """
    # If tree is empty, create a new node
    if root is None:
        return TreeNode(value)
    
    # Recursively insert into left or right subtree
    try:
        if value < root.value:
            root.left = insert_node(root.left, value)
        else:
            root.right = insert_node(root.right, value)
    except TypeError:
        raise ValueError("List contains elements that cannot be compared")
    
    return root

def in_order_traversal(node, result):
    """
    Perform in-order traversal to collect sorted elements.
    
    Args:
        node (TreeNode): Current node in the traversal
        result (list): List to store sorted elements
    """
    if node is not None:
        # Traverse left subtree
        in_order_traversal(node.left, result)
        
        # Add current node's value
        result.append(node.value)
        
        # Traverse right subtree
        in_order_traversal(node.right, result)