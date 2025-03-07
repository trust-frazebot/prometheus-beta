class SuffixTree:
    """
    A Suffix Tree implementation for efficient string matching.
    
    The Suffix Tree allows for fast substring search and pattern matching.
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
            self.start = start
            self.end = end
            # Track whether this is a complete substring
            self.complete_strings = set()
    
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
        
        self.text = text
        self.root = self.Node()
        self._build_suffix_tree()
    
    def _build_suffix_tree(self):
        """
        Build the Suffix Tree by adding all suffixes and substrings.
        """
        # Add all suffixes
        for i in range(len(self.text)):
            self._add_suffix(self.text[i:])
    
    def _add_suffix(self, suffix):
        """
        Add a suffix to the tree.
        
        Args:
            suffix (str): Suffix to add to the tree
        """
        current = self.root
        for i, char in enumerate(suffix):
            # If character doesn't exist in current node's children, create new edge
            if char not in current.children:
                new_node = self.Node(start=i, end=len(suffix)-1)
                current.children[char] = new_node
            
            # Track complete strings at each node
            if i == len(suffix) - 1:
                current.children[char].complete_strings.add(suffix)
            
            # Move to next node
            current = current.children[char]
    
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
        
        # Ensure complete pattern exists
        return any(pattern == s for s in current.complete_strings)
    
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
        
        # Use standard string method for occurrence finding
        occurrences = [i for i in range(len(self.text)) 
                       if self.text.startswith(pattern, i)]
        
        return occurrences