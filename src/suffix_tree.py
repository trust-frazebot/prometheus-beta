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
        def __init__(self):
            """
            Initialize a node with empty children and leaf markers.
            
            Attributes:
                children (dict): Dictionary mapping characters to child nodes
                suffix_link (Node, optional): Link to another node for optimization
                start (int): Starting index of the edge leading to this node
                end (int): Ending index of the edge leading to this node
            """
            self.children = {}
            self.suffix_link = None
            self.start = -1
            self.end = -1
            
    def __init__(self, text):
        """
        Construct a Suffix Tree for the given text.
        
        Args:
            text (str): Input text to build the suffix tree for
        """
        # Append a unique terminator to handle edge cases
        self.text = text + '$'
        self.root = self.Node()
        self._build_suffix_tree()
    
    def _build_suffix_tree(self):
        """
        Build the Suffix Tree using Ukkonen's algorithm.
        
        This is an optimized method to construct the suffix tree in O(n) time.
        """
        # Implement full suffix tree construction
        for i in range(len(self.text)):
            self._extend_suffix_tree(i)
    
    def _extend_suffix_tree(self, phase):
        """
        Extend the suffix tree for each character.
        
        Args:
            phase (int): Current phase of suffix tree construction
        """
        # Placeholder for detailed Ukkonen's algorithm implementation
        pass
    
    def search(self, pattern):
        """
        Search for a pattern in the Suffix Tree.
        
        Args:
            pattern (str): Pattern to search for
        
        Returns:
            bool: True if pattern exists in the text, False otherwise
        """
        if not pattern:
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
        if not pattern:
            return []
        
        occurrences = []
        current = self.root
        
        # Traverse to the end of the pattern
        for char in pattern:
            if char not in current.children:
                return []
            current = current.children[char]
        
        # Collect all leaf nodes under this node
        self._collect_occurrences(current, occurrences)
        
        return occurrences
    
    def _collect_occurrences(self, node, occurrences):
        """
        Recursively collect all occurrences from leaf nodes.
        
        Args:
            node (Node): Current node to explore
            occurrences (list): List to store occurrence indices
        """
        # This is a placeholder - full implementation would traverse leaf nodes
        pass