class SuffixTree:
    """
    A Suffix Tree implementation for efficient string matching.
    
    The Suffix Tree allows for fast substring search and pattern matching 
    with a time complexity of O(m) for search, where m is the length of the search pattern.
    """
    
    class Node:
        """
        Internal node class for the Suffix Tree.
        """
        def __init__(self, start=-1, end=-1):
            """
            Initialize a node with start and end indices.
            
            Args:
                start (int): Starting index of the substring edge
                end (int): Ending index of the substring edge
            """
            self.children = {}
            self.suffix_link = None
            self.start = start
            self.end = end
            self.leaf_index = -1  # Track the original suffix index for occurrence finding
    
    def __init__(self, text):
        """
        Construct a Suffix Tree for the given text.
        
        Args:
            text (str): Input text to build the suffix tree for
        """
        # Handle empty string edge case
        if not text:
            self.text = ""
            self.root = self.Node()
            return
        
        # Append a unique terminator to handle edge cases
        self.text = text + '$'
        self.root = self.Node()
        self._build_suffix_tree()
    
    def _build_suffix_tree(self):
        """
        Build the Suffix Tree by adding all suffixes.
        
        Time Complexity: O(n^2)
        """
        for i in range(len(self.text)):
            self._add_suffix(i)
    
    def _add_suffix(self, suffix_start):
        """
        Add a suffix to the tree.
        
        Args:
            suffix_start (int): Starting index of the suffix
        """
        current = self.root
        for j in range(suffix_start, len(self.text)):
            current_char = self.text[j]
            
            # If character doesn't exist in current node's children, create new edge
            if current_char not in current.children:
                # Create a leaf node for this new suffix
                new_leaf = self.Node(start=j, end=len(self.text)-1)
                new_leaf.leaf_index = suffix_start
                current.children[current_char] = new_leaf
                break
            
            # Move to next node
            current = current.children[current_char]
    
    def search(self, pattern):
        """
        Search for a pattern in the Suffix Tree.
        
        Args:
            pattern (str): Pattern to search for
        
        Returns:
            bool: True if pattern exists in the text, False otherwise
        """
        if not pattern or not self.text:
            return False
        
        current = self.root
        for char in pattern:
            if char not in current.children:
                return False
            current = current.children[char]
        
        return True
    
    def find_all_occurrences(self, pattern):
        """
        Find all occurrences of a pattern in the text.
        
        Args:
            pattern (str): Pattern to search for
        
        Returns:
            list: Indices of all occurrences of the pattern
        """
        if not pattern or not self.text:
            return []
        
        # First, find the node corresponding to the pattern
        current = self.root
        for char in pattern:
            if char not in current.children:
                return []
            current = current.children[char]
        
        # Collect all leaf indices under this node
        return self._collect_leaf_indices(current)
    
    def _collect_leaf_indices(self, node):
        """
        Collect all leaf indices under a given node.
        
        Args:
            node (Node): Node to collect indices from
        
        Returns:
            list: Indices of all suffixes under the node
        """
        indices = []
        
        # If node is a leaf, add its index
        if node.leaf_index != -1:
            indices.append(node.leaf_index)
        
        # Recursively collect from children
        for child in node.children.values():
            indices.extend(self._collect_leaf_indices(child))
        
        return indices