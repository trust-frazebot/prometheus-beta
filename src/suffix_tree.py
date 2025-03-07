class SuffixTree:
    """
    A Suffix Tree implementation for efficient string matching.
    
    The Suffix Tree allows for fast substring search and pattern matching.
    """
    
    def __init__(self, text):
        """
        Construct a Suffix Tree for the given text.
        
        Args:
            text (str): Input text to build the suffix tree for
        """
        # Handle empty string edge case
        if not text:
            self.text = ""
            return
        
        # Append $ to handle full string matching
        self.text = text + '$'
        self._build_suffixes()
    
    def _build_suffixes(self):
        """
        Build all suffixes as a list for efficient searching.
        """
        self._suffixes = [self.text[i:] for i in range(len(self.text))]
    
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
        
        # Check if pattern appears in any of the suffixes
        return any(pattern == suffix[:len(pattern)] for suffix in self._suffixes)
    
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
        
        # Find all starting indices of the pattern
        return [i for i in range(len(self.text) - 1) 
                if self.text.startswith(pattern, i)]